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

import sys
#sys.path.append('./DOM')
import cimIdentifiedObject
import serialization

class TownDetail:
    def __init__(self, name, code, stateOrProvince):
        self.name = name
        self.code = code
        self.stateOrProvince = stateOrProvince

class StreetDetail:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class StreetAddress:
    def __init__(self, streetName, streetNr, townName, townCode, state):
        self.streetDetail = StreetDetail(streetName, streetNr)
        self.townDetail = TownDetail(townName, townCode, state)

class Location(cimIdentifiedObject.IdentifiedObject):

    def __init__(self, mRID):
        cimIdentifiedObject.IdentifiedObject.__init__(self, mRID)
        self.mainAddress = StreetAddress("", "", "", "", "")
        self.secondaryAddress = ""

    def setMainAddress(self, streetName, streetNr, townName, townCode, stateOrProvince):
        self.mainAddress.streetDetail.name = serialization.serialEncode(streetName)
        self.mainAddress.streetDetail.number = serialization.serialEncode(streetNr)
        self.mainAddress.townDetail.name = serialization.serialEncode(townName)
        self.mainAddress.townDetail.code = serialization.serialEncode(townCode)
        self.mainAddress.townDetail.stateOrProvince = serialization.serialEncode(stateOrProvince)

    def setSecondaryAddress(self, sAddr):
        self.secondaryAddress = serialization.serialEncode(sAddr)


    def getMainAddress(self):
        mAddrL = []
        mAddrL.append(self.mainAddress.streetDetail.name)
        mAddrL.append(self.mainAddress.streetDetail.number)
        mAddrL.append(self.mainAddress.townDetail.name)
        mAddrL.append(self.mainAddress.townDetail.code)
        mAddrL.append(self.mainAddress.townDetail.stateOrProvince)
        return mAddrL

    def serialize(self):
        sContent = cimIdentifiedObject.IdentifiedObject.serialize(self)
        sMainAddress = serialization.serialIndent + serialization.serialIndent + "<cim:Location.mainAddress>"
        sMainAddress =  sMainAddress + ",".join(self.getMainAddress())
        sMainAddress = sMainAddress + "</cim:Location.mainAddress>" + '\n'
        return sContent + sMainAddress