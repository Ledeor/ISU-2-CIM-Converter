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

class ServiceCategory(cimIdentifiedObject.IdentifiedObject):
    def __init__(self, mRID):
        cimIdentifiedObject.IdentifiedObject.__init__(self, mRID)
        self.description = "ServiceCategory"
        self.aliasName = "Vertragsart"
        self.kind = "other"

    def serialize(self):
        self.sTagOpen = serialization.serialIndent + "<cim:ServiceCategory rdf:ID=\"" + self.mRID + "\">" + '\n'
        self.sContent = cimIdentifiedObject.IdentifiedObject.serialize(self)
        self.sKind = serialization.serialIndent + serialization.serialIndent + "<cim:ServiceCategory.kind>" + self.kind + "</cim:ServiceCategory.kind>" + '\n'
        self.sTagClose = serialization.serialIndent + "</cim:ServiceCategory>" + '\n'
        return self.sTagOpen + self.sContent + self.sTagClose