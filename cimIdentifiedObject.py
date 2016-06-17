#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      roddi
#
# Created:     17.03.2016
# Copyright:   (c) roddi 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import serialization

class IdentifiedObject:
    def __init__(self, mRID):
        self.description = "IdentifiedObject"
        self.mRID = mRID
        self.name = ""
        self.aliasName = ""

    def serialize(self):
        self.sDescription = serialization.serialIndent + serialization.serialIndent + "<cim:IdentifiedObject.description>" + self.description + "</cim:IdentifiedObject.description>" + '\n'
        #self.sMRID = serialization.serialIndent + "<cim:IdentifiedObject.mRID>" + self.mRID + "</cim:IdentifiedObject.mRID>" + '\n'
        self.sName = serialization.serialIndent + serialization.serialIndent + "<cim:IdentifiedObject.name>" + self.name + "</cim:IdentifiedObject.name>" + '\n'
        self.sAliasName = serialization.serialIndent + serialization.serialIndent + "<cim:IdentifiedObject.aliasName>" + self.aliasName + "</cim:IdentifiedObject.aliasName>" + '\n'
        return self.sDescription + self.sName + self.sAliasName
