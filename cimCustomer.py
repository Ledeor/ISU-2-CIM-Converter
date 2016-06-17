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

class Customer(cimIdentifiedObject.IdentifiedObject):
    def __init__(self, mRID):
        cimIdentifiedObject.IdentifiedObject.__init__(self, mRID)
        self.description = "Customer"
        self.aliasName = "Geschaeftspartner"
        self.kind = "other"

    def setKind(self, k):
        self.kind = serialization.convertXMLpredefEntities(serialization.serialEncode(k))

    def setName(self, n):
        self.name = serialization.convertXMLpredefEntities(serialization.serialEncode(n))

    def serialize(self):
        self.sTagOpen = serialization.serialIndent + "<cim:Customer rdf:ID=\"" + self.mRID + "\">" + '\n'
        self.sContent = cimIdentifiedObject.IdentifiedObject.serialize(self)
        self.sKind = serialization.serialIndent + serialization.serialIndent + "<cim:Customer.kind>" + self.kind + "</cim:Customer.kind>" + '\n'
        self.sTagClose = serialization.serialIndent + "</cim:Customer>" + '\n'
        return self.sTagOpen + self.sContent + self.sKind + self.sTagClose
