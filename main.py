#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      roddi
#
# Created:     17.03.2016
# Copyright:   (c) roddi 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import gc
import sys
import datetime

import cimServiceLocation
import cimUsagePoint
import cimUsagePointLocation
import cimCustomerAgreement
import cimServiceCategory
import cimCustomer
import cimPricingStructure

import cimParseTemplateAndAccessDB
import serialization

#databaseFile  = "P:\\SAP_PROJ\\Tp_energ\\Laufender Betrieb\\Stammdaten_Backup.mdb"
#databaseFile = "..\\Stammdaten.mdb"
databaseFile = "..\\testISU.mdb"
#templateFile = "..\\ISU.CIM.TEMPLATE"
tmpFileDirectory = "C:\\temp\\"

curTarifTypList = []
curSARTList = []

def main():
    #cimParseTemplateAndAccessDB.parseTemplate(templateFile)

    print datetime.datetime.now().strftime("%I:%M%p") + " Executing query..."
    [rows, sGems, sBranches] = cimParseTemplateAndAccessDB.readAccessDBAll(databaseFile)

    print datetime.datetime.now().strftime("%I:%M%p") + " Creating CIM target model..."
    curAOID = ""
    curUPL = ""
    curUP = ""
    curVER = ""
    curSART = ""
    curGP = ""
    curTarifTyp = ""
    markedDELETE = ""
    sOutput = ""
    iLoop = 0
    iTempFiles = 0
    for row in rows:

        # do some formatting to ensure comparison
        rowAOID = str(row.__getattribute__('Anschl-obj'))
        rowVS = str(row.__getattribute__('Vstelle'))
        rowANL = str(row.__getattribute__('Anlage'))
        rowVER = str(row.__getattribute__('Vertrag'))
        rowSART = str(row.__getattribute__('SART'))
        rowGP = str(row.__getattribute__('Gesch-part'))
        rowTarifTyp = str(row.__getattribute__('Tariftyp'))
        rowmarkedDELETE = str(row.__getattribute__('L'))

        if rowmarkedDELETE <> 'None': # Skip all entries that are marked DELETE
            pass
        else:

            # Anschlussobjekt -> ServiceLocation
            if curAOID <> rowAOID:
                curAOID = rowAOID
                sl = cimServiceLocation.ServiceLocation(curAOID)
                gemKey = str(row.__getattribute__('Gem'))
                sGem = ""
                for gem in sGems:
                    if str(gem.__getattribute__('Gem')) == gemKey:
                        sGem = gem.__getattribute__('Gemeinde')
                        break

                sl.setMainAddress(row.__getattribute__('Ao-Strasse'),
                                  row.__getattribute__('Ao-Nr'),
                                  row.__getattribute__('Ao-Ort'),
                                  row.__getattribute__('Ao-Plz'),
                                  sGem)
                sOutput = sOutput + sl.serialize()

            # Verbrauchsstelle -> UsagePointLocation
            if curUPL <> rowVS:
                curUPL = rowVS
                upl = cimUsagePointLocation.UsagePointLocation(curUPL)
                sOutput = sOutput + upl.serialize()

            # Serviceart -> ServiceCategory
            if curSART <> rowSART:
                curSART = rowSART
                sa = cimServiceCategory.ServiceCategory(curSART)
                if curSART in curSARTList: # Avoid multiple serialization of the same kind (LIEF, NETZ)
                    pass
                else:
                    curSARTList.append(curSART)
                    sOutput = sOutput + sa.serialize()

            # Tariftyp -> PricingStructure
            if curTarifTyp <> rowTarifTyp:
                curTarifTyp = rowTarifTyp
                ps = cimPricingStructure.PricingStructure(curTarifTyp)
                ps.setCode(row.__getattribute__('Abrk'))
                ps.setServiceCategory(sa)
                if curTarifTyp in curTarifTypList: # Avoid multiple serialization of the same tariff type
                    pass
                else:
                    curTarifTypList.append(curTarifTyp)
                    sOutput = sOutput + ps.serialize()


            # Geschaeftspartner -> Customer
            if curGP <> rowGP:
                curGP = rowGP
                cust = cimCustomer.Customer(curGP)
                adr = serialization.serialEncode(row.__getattribute__('Adrzeile1')) + "," +\
                    serialization.serialEncode(row.__getattribute__('Adrzeile2')) + "," +\
                    serialization.serialEncode(row.__getattribute__('Adrzeile3'))
                cust.setName(adr)
                branchKey = str(row.__getattribute__('Branche'))
                sBranch = ""
                for branch in sBranches:
                    if str(branch.__getattribute__('Branche')) == branchKey:
                        sBranch = branch.__getattribute__('Bez_Einnahmegruppe')
                        break
                cust.setKind(sBranch)
                sOutput = sOutput + cust.serialize()

            # Vertrag -> CustomerAgreement
            if curVER <> rowVER:
                curVER = rowVER
                ca = cimCustomerAgreement.CustomerAgreement(curVER)
                ca.setServiceCategory(sa)
                ca.setCustomer(cust)
                sOutput = sOutput + ca.serialize()

            # Anlage -> UsagePoint
            if curUP <> rowANL:
                curUP = rowANL
                up = cimUsagePoint.UsagePoint(curUP)
                up.setServiceLocation(sl)
                up.setUsagePointLocation(upl)
                up.setCustomerAgreement(ca)
                up.setPricingStructure(ps)
                sOutput = sOutput + up.serialize()
        #//if rowmarkedDELETE <> 'None'

        iLoop = iLoop + 1
        if iLoop % 1000 == 0:
            sys.stdout.write("-")
            sys.stdout.flush()
        if iLoop % 10000 == 0:
            sys.stdout.write("|" + str(iLoop) + "|")
            sys.stdout.flush()
            gc.collect()

        if iLoop % 10000 == 0:
            iTempFiles = iTempFiles + 1
            print datetime.datetime.now().strftime("%I:%M%p") + " Writing output file " + tmpFileDirectory + "nis.cim.tmp" + str(iTempFiles)
            with open(tmpFileDirectory + "nis.cim.tmp" + str(iTempFiles), 'w') as f:
                f.write(sOutput)
                f.close()
            sOutput = ""
            gc.collect()

    sys.stdout.write("\n")
    # Compile ISU.CIM
    print datetime.datetime.now().strftime("%I:%M%p") + " Writing output file " + serialization.serialFileName + "..."

    with open(serialization.serialFileName, 'a') as f:
        f.truncate()
        f.write(serialization.serialHeader)
        if iTempFiles > 0:
            i = 1
            while i <= iTempFiles:
                with open(tmpFileDirectory + "nis.cim.tmp" + str(i), 'r') as t:
                    print "nis.cim.tmp" + str(i) + "..."
                    f.write(t.read())
                    t.close()
                i = i + 1;
        else:
            f.write(sOutput)
        f.write(serialization.serialFooter)
        f.close()
        print "...done"


    print datetime.datetime.now().strftime("%I:%M%p") + " ...done."


if __name__ == '__main__':
    main()
