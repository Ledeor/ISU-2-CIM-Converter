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

import cimLocation

class WorkLocation(cimLocation.Location):
    def __init__(self, mRID):
        cimLocation.Location.__init__(self, mRID)

    def serialize(self):
        return cimLocation.Location.serialize(self)