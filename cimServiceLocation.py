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

import cimWorkLocation
import serialization

class ServiceLocation(cimWorkLocation.WorkLocation):
    def __init__(self, mRID):
        cimWorkLocation.WorkLocation.__init__(self, mRID)
        self.description = "ServiceLocation"
        self.aliasName = "Anschlussobjekt"

    def serialize(self):
        self.sTagOpen = serialization.serialIndent + "<cim:ServiceLocation rdf:ID=\"" + self.mRID + "\">" + '\n'
        self.sContent = cimWorkLocation.WorkLocation.serialize(self)
        self.sTagClose = serialization.serialIndent + "</cim:ServiceLocation>" + '\n'
        return self.sTagOpen + self.sContent + self.sTagClose