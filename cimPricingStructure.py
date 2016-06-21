#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      roddi
#
# Created:     23.03.2016
# Copyright:   (c) roddi 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import cimIdentifiedObject
import serialization

# mRID = Tariftyp
class PricingStructure(cimIdentifiedObject.IdentifiedObject):
    def __init__(self, mRID):
        cimIdentifiedObject.IdentifiedObject.__init__(self, mRID)
        self.description = "PricingStructure"
        self.aliasName = "Tariftyp"
        self.code = ""
        self.resSC = None

    def setCode(self, c):
        self.code = serialization.convertXMLpredefEntities(serialization.serialEncode(c))

    def setServiceCategory(self, sc):
        self.resSC = sc

    def serialize(self):
        self.sTagOpen = serialization.serialIndent + "<cim:PricingStructure rdf:ID=\"" + self.mRID + "\">" + '\n'
        self.sContent = cimIdentifiedObject.IdentifiedObject.serialize(self)
        self.sCode = serialization.serialIndent + serialization.serialIndent + "<cim:PricingStructure.code>" + self.code + "</cim:PricingStructure.code>" + '\n'

        # ServiceCategory associated?
        if self.resSC != None:
            self.sSC = serialization.serialIndent + serialization.serialIndent + "<cim:PricingStructure.ServiceCategory rdf:resource=\"#" + self.resSC.mRID + "\"/>" + '\n'
        else:
            self.sSC = ""

        self.sTagClose = serialization.serialIndent + "</cim:PricingStructure>" + '\n'
        return self.sTagOpen + self.sContent + self.sCode + self.sSC + self.sTagClose