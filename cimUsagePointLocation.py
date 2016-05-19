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

import cimLocation
import serialization

class UsagePointLocation(cimLocation.Location):

    def __init__(self, mRID):
        cimLocation.Location.__init__(self, mRID)
        self.description = "UsagePointLocation"
        self.aliasName = "Verbrauchsstelle"

    def serialize(self):
        self.sTagOpen = serialization.serialIndent + "<cim:UsagePointLocation rdf:ID=\"" + self.mRID + "\">" + '\n'
        self.sContent = cimLocation.Location.serialize(self)
        self.sTagClose = serialization.serialIndent + "</cim:UsagePointLocation>" + '\n'
        return self.sTagOpen + self.sContent + self.sTagClose