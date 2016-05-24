#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      roddi
#
# Created:     22.03.2016
# Copyright:   (c) roddi 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import cimIdentifiedObject
import serialization

class CustomerAgreement(cimIdentifiedObject.IdentifiedObject):
    def __init__(self, mRID):
        cimIdentifiedObject.IdentifiedObject.__init__(self, mRID)
        self.description = "CustomerAgreement"
        self.aliasName = "Vertrag"
        self.resSC = None
        self.resCust = None

    def setServiceCategory(self, sc):
        self.resSC = sc

    def setCustomer(self, cust):
        self.resCust = cust

    def serialize(self):
        self.sTagOpen = serialization.serialIndent + "<cim:CustomerAgreement rdf:ID=\"" + self.mRID + "\">" + '\n'
        self.sContent = cimIdentifiedObject.IdentifiedObject.serialize(self)

        # ServiceCategory associated?
        if self.resSC <> None:
            self.sSC = serialization.serialIndent + serialization.serialIndent + "<cim:CustomerAgreement.ServiceCategory rdf:resource=\"#" + self.resSC.mRID + "\"/>" + '\n'
        else:
            self.sSC = ""

        # Customer associated?
        if self.resCust <> None:
            self.resCust = serialization.serialIndent + serialization.serialIndent + "<cim:CustomerAgreement.Customer rdf:resource=\"#" + self.resCust.mRID + "\"/>" + '\n'
        else:
            self.resCust = ""

        self.sTagClose = serialization.serialIndent + "</cim:CustomerAgreement>" + '\n'
        return self.sTagOpen + self.sContent + self.sSC + self.resCust + self.sTagClose