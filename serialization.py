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

import cgi
import sys

serialFileName = "ISU_CIM_Export_yyyymmdd.rdf"

serialIndent = "    "
#serialHeader = "</cim>"

serialHeader = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"+'\n'+"\
<rdf:RDF xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\"\
 xmlns:cim=\"http://iec.ch/TC57/2010/CIM-schema-cim15#\">" + '\n'

serialFooter = "</rdf:RDF>" + '\n'

encoding = 'utf-8'

# Convert 's' to an 'encoding' conform string
def serialEncode(s):
    retVal = ''
    if s is not None:
        try:
            retVal = str(s)
        except:
            sys.stdout.write("<Encoding exception: " + s + " " + str(type(s)) + ">")
            sys.stdout.flush()

    return retVal


def convertXMLpredefEntities(s):
    return str(cgi.escape(s).encode(encoding, "xmlcharrefreplace"))
