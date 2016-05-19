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

import cimIdentifiedObject
import serialization

class UsagePoint(cimIdentifiedObject.IdentifiedObject):
    def __init__(self, mRID):
        cimIdentifiedObject.IdentifiedObject.__init__(self, mRID)
        self.description = "UsagePoint"
        self.aliasName = "Versorgungsanlage"
        self.outageRegion = "unknown"
        self.nominalServiceVoltage = "-1"
        self.ratedPower = "-1"
        self.ratedCurrent = "-1"
        self.resSL = None
        self.resUPL = None
        self.resCA = None
        self.resPS = None

    def setServiceLocation(self, sl):
        self.resSL = sl

    def setUsagePointLocation(self, upl):
        self.resUPL = upl

    def setCustomerAgreement(self, ca):
        self.resCA = ca

    def setPricingStructure(self, ps):
        self.resPS = ps

    def serialize(self):
        self.sTagOpen = serialization.serialIndent + "<cim:UsagePoint rdf:ID=\"" + self.mRID + "\">" + '\n'
        self.sContent = cimIdentifiedObject.IdentifiedObject.serialize(self)
        self.sOutageRegion = serialization.serialIndent + serialization.serialIndent + "<cim:UsagePoint.outageRegion>" + self.outageRegion + "</cim:UsagePoint.outageRegion>" + '\n'
        self.sNSV = serialization.serialIndent + serialization.serialIndent + "<cim:UsagePoint.nominalServiceVoltage>" + self.nominalServiceVoltage + "</cim:UsagePoint.nominalServiceVoltage>" + '\n'
        self.sRatedPower = serialization.serialIndent + serialization.serialIndent + "<cim:UsagePoint.ratedPower>" + self.ratedPower + "</cim:UsagePoint.ratedPower>" + '\n'
        self.sRatedCurrent = serialization.serialIndent + serialization.serialIndent + "<cim:UsagePoint.ratedCurrent>" + self.ratedCurrent + "</cim:UsagePoint.ratedCurrent>" + '\n'

        # ServiceLocation associated?
        if self.resSL <> None:
            self.sSl = serialization.serialIndent + serialization.serialIndent
            self.sSl = self.sSl + "<cim:UsagePoint.ServiceLocation rdf:resource=\"#" + self.resSL.mRID + "\"/>" + '\n'
        else:
            self.sSl = ""

        # UsagePointLocation associated?
        if self.resUPL <> None:
            self.sUpl = serialization.serialIndent + serialization.serialIndent + "<cim:UsagePoint.UsagePointLocation rdf:resource=\"#" + self.resUPL.mRID + "\"/>" + '\n'
        else:
            self.sUpl = ""

        # CustomerAgreement associated?
        if self.resCA <> None:
            self.sCA = serialization.serialIndent + serialization.serialIndent + "<cim:UsagePoint.CustomerAgreement rdf:resource=\"#" + self.resCA.mRID + "\"/>" + '\n'
        else:
            self.sCA = ""

        # PricingStructure associated?
        if self.resPS <> None:
            self.resPS = serialization.serialIndent + serialization.serialIndent + "<cim:UsagePoint.PricingStructure rdf:resource=\"#" + self.resPS.mRID + "\"/>" + '\n'
        else:
            self.resPS = ""

        self.sTagClose = serialization.serialIndent + "</cim:UsagePoint>" + '\n'
        return self.sTagOpen + self.sContent + self.sOutageRegion + self.sNSV + self.sRatedPower + self.sRatedCurrent + self.sSl + self.sUpl + self.sCA + self.resPS + self.sTagClose
