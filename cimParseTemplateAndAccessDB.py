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

import pyodbc
from xml.dom.minidom import parse, parseString

class Isu_Stammdaten_Adressen:
    def __init__(self):
        self.tableName = "Isu_Stammdaten_Adressen"
        self.colL = ["Anschl-obj", "Vstelle", "Anlage", "Vertrag", "Gesch-part", "SART",
                    "Ao-Ort", "Ao-Plz", "Ao-Strasse", "Ao-Nr", "Gem", "Branche", "Adrzeile1",
                    "Adrzeile2", "Adrzeile3", "Abrk", "Tariftyp", "L"]


def parseTemplate(templateFile):
    isudom = parse(templateFile)
##    for node in isudom.getElementsByTagName('cim:ServiceLocation'):
##        print node.toxml()
    return isudom

def readAccessDBAll(databaseFile):
    cIsu = Isu_Stammdaten_Adressen()
    sISUMDCols = ''
    for c in cIsu.colL:
        if sISUMDCols != '':
            sISUMDCols = sISUMDCols + ", "
        sISUMDCols = sISUMDCols + "[" + c + "]"

    connectionString = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=%s" % databaseFile
    dbConnection   = pyodbc.connect(connectionString)
    cursor = dbConnection.cursor()

    cursor.execute("select "+ sISUMDCols + " from Isu_Stammdaten_Adressen ORDER by [Anschl-obj]")
    tMaster = cursor.fetchall()

    cursor.execute("select * " + "from Gemeindetext")
    tGem = cursor.fetchall()

    cursor.execute("select * " + "from Branchentexte_Anlage")
    tBranch = cursor.fetchall()

    dbConnection.close()

    return [tMaster, tGem, tBranch]


def readAccessDB(databaseFile, colSELECT, table):
    connectionString = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=%s" % databaseFile
    dbConnection   = pyodbc.connect(connectionString)
    cursor = dbConnection.cursor()
    cursor.execute("select " + colSELECT + " from " + table)
    rows = cursor.fetchall()
    dbConnection.close()

    return rows


def readAccessDBValue(databaseFile, table, keyCol, tgtCol, value):
    connectionString = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=%s" % databaseFile
    dbConnection   = pyodbc.connect(connectionString)
    cursor = dbConnection.cursor()
    cursor.execute("select " + tgtCol + " from " + table + " where " + keyCol + "=" + value)
    rows = cursor.fetchall()
    dbConnection.close()

    return rows