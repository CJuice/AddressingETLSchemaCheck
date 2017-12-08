"""
Identifies schema changes in address point feature classes by comparing required/expected fields to
fields present in the data. The results of the check are printed. If required fields are missing the county data
will not work properly with later steps in the ETL process that depend on the required field(s) being present.
Modified from original script by CJuice on 20171208
"""

# IMPORTS
from arcpy import GetMessages
from arcpy import ListFields
from arcpy import ListFeatureClasses
from arcpy import env
from os import path
from collections import OrderedDict
import logging
import datetime

# VARIABLES
strPSAFeatureClassNotPresent = " {} Not Present\n"
strPSAPathBeingExamined = " {}"
strPSAAllRequiredFieldsPresent = "\tMeets Requirements\n"
strPSAFieldsNotPresentInSubmittedData = "\tRequired Fields Not In Submitted Data:\n\t\t{}\n"
strPSAErrorListFeatureClasses = "Error generating list of feature class field names: {}\n"
strPSAGeoprocessingError = "GP Error: {}"
lsFeatureClassesInMasterGDB = None
strRootGeodatabasePath = r"E:\Addressing_FMEProject\Raw data\ConsolidatedAddressData_Summer2017.gdb"

    # Logging setup
strInfo = "info"
strWarning = "warning"
strError = "error"
strLogFileName = r"LogFiles\SchemaCheck.log"
tupTodayDateTime = datetime.datetime.utcnow().timetuple()
strTodayDateTimeForLogging = "{}/{}/{} UTC[{}:{}:{}]".format(tupTodayDateTime[0]
                                                          , tupTodayDateTime[1]
                                                          , tupTodayDateTime[2]
                                                          , tupTodayDateTime[3]
                                                          , tupTodayDateTime[4]
                                                          , tupTodayDateTime[5])
logging.basicConfig(filename=strLogFileName,level=logging.INFO)
strPSAForLogging_ScriptInitiated = " {} - Schema Check Initiated".format(strTodayDateTimeForLogging)


    # NOTE: format of dictionary is {county feature class name (no spaces!) : list of required fields for that county}
dictRequiredFields = {
    "Allegany":             [u'objectid',u'streetsuf',u'siteaddid',u'preaddrnum',u'addrnum',u'addrnumsuf',u'prefix',u'streetname',u'postdir',u'fullname',u'unittype',u'unitid',u'msag',u'zip',u'addrclass']
    , "AnneArundel":        [u'OBJECTID',u'BMC_ID',u'ST_TYPE',u'ST_NAME',u'ST_NUMSUFF',u'ST_PREFIXD',u'ST_SUFFIXD',u'UNIT_TYPE',u'UNITNUM',u'UNIT_ADDR',u'FULL_ADDRE',u'BLDG_NAME',u'CITY_NAME',u'ZIPCODE',u'GlobalID',u'ST_NUMBER']
    , "BaltimoreCity":      [u'OBJECTID',u'ADDRPT_ID',u'ST_NAME',u'ST_DIR',u'ADDR_FRAC',u'ZIP_CODE',u'ADDR_NUMBE',u'ST_TYPE']
    , "BaltimoreCounty":    [u'OBJECTID',u'ST_TYPE',u'ST_NAME',u'ST_PREFIXTYPE',u'ST_NUMSUFFIX',u'ST_PREMOD',u'ST_PREFIXDIR',u'ST_SUFFIXDIR',u'ST_POSTMOD',u'ADDRLABEL',u'CITY_POSTAL',u'STATE',u'ZIP',u'ADDRESSUSE',u'ST_NUMBER']
    , "Calvert":            [u'OBJECTID',u'PREMSNUM',u'PREMSDIR',u'PREMSNAM',u'PREMSTYP',u'ALPHA',u'PREMCITY',u'PREMZIP']
    , "Caroline":           [u'OBJECTID',u'STRT_ADD',u'STRT_PFX',u'STRT_NAME',u'UNIT',u'COMMUNITY',u'ZIP',u'TYP',u'TYPE']
    , "Carroll":            [u'OBJECTID',u'ST_TYPE',u'ST_NAME',u'ST_NUM_SUF',u'ST_PREFIX',u'ST_SUFFIX',u'UNIT_TYPE',u'UNIT_NUMBE',u'County',u'ZIPCODE',u'ST_NUMBER']
    , "Cecil":              [u'OBJECTID',u'STRT_ADD',u'STRT_PFX',u'STRT_NAME',u'STRT_SUF',u'UNIT',u'Comment',u'COMMUNITY',u'TYP',u'TYPE',u'NAME']
    , "Charles":            [u'OBJECTID',u'NEWCITY',u'NUMBER_',u'Street_Pre',u'Street_Nam',u'Street_typ',u'Street_Suf',u'ZIP',u'Addl_Info']
    , "Dorchester":         [u'OBJECTID',u'STRTTYP',u'STRTNUM',u'STRTDIR',u'STRTNAM',u'STRTSFX',u'STRTUNT',u'COMMUNITY']
    , "Frederick":          [u'OBJECTID',u'ST_TYPE',u'ST_NUM',u'ST_NUM_SUFFIX',u'ST_PREFIX',u'ST_NAME',u'ST_SUFFIX',u'UNIT_TYPE',u'UNIT_NUM',u'CITY',u'STATE',u'ZIP_STNM',u'ADDR_TYPE']
    , "Garrett":            [u'OBJECTID',u'STRUCTURE_NUMBER',u'STRUCTURE_NUMBER_SUFFIX',u'PREFIX_DIRECTIONAL',u'STREET_NAME',u'STREET_TYPE',u'SUFFIX_DIRECTIONAL',u'UNIT_TYPE',u'UNIT_NUMBER',u'CITY',u'COMMUNITY',u'STATE',u'ZIP_CODE']
    , "Harford":            [u'OBJECTID',u'P_ST_TYPE',u'P_ST_NAME',u'P_ST_SUF',u'P_ST_DIREC',u'P_CITY',u'P_Z_1',u'P_ST_NO']
    , "Howard":             [u'OBJECTID',u'PREMSTYP',u'PREMSNAM',u'PREMSNAM',u'STREETNAME',u'SUBADDRESS',u'PREMCITY',u'PREMZIP',u'ADDRESSNO']
    , "Kent":               [u'OBJECTID',u'TYP',u'STRT_ADD',u'STRT_PFX',u'STRT_NAME',u'STREET',u'UNIT',u'COMMUNITY',u'TYPE']
    , "Montgomery":         [u'OBJECTID',u'ADDRNUM',u'PRE_DIR',u'STREET_NAM',u'STREET_TYP',u'SUF_DIR',u'POSTAL_CIT',u'ZIP']
    , "PrinceGeorges":      [u'OBJECTID',u'ADDRESS_NUMBER_PREFIX',u'ADDRESS_NUMBER',u'ADDRESS_NUMBER_SUFFIX',u'STREET_NAME_PRE_MODIFIER',u'STREET_NAME_PRE_DIRECTIONAL',u'STREET_NAME_PRE_TYPE',u'STREET_NAME',u'STREET_NAME_POST_DIRECTIONAL',u'STREET_NAME_POST_MODIFIER',u'COMPLETE_STREET_NAME',u'SUBADDRESS_TYPE1',u'SUBADDRESS_IDENTIFIER1',u'LANDMARK_NAME1',u'COMPLETE_LANDMARK_NAME',u'PLACE_NAME',u'STATE_NAME',u'ZIP_CODE']
    , "QueenAnnes":         [u'OBJECTID',u'STRT_ADD',u'STRT_PFX',u'TYP',u'STRT_NAME',u'STRT_SFX',u'STREET',u'UNIT',u'COMMUNITY',u'TYPE']
    , "Somerset":           [u'OBJECTID',u'STRNUM',u'STRTYPE',u'STRDIR',u'STRNAM',u'UNITTYPE',u'UNIT',u'CITY',u'ZIP',u'MYPROPERTY']
    , "StMarys":            [u'OBJECTID',u'ST_TYPE',u'HOUSE_NO',u'ST_DIR',u'ST_NAME',u'APT_NO',u'ZIP']
    , "Talbot":             [u'OBJECTID',u'STRT_ADDR',u'PREF_DIR',u'STREET',u'SUFF_TYPE',u'SUFF_DIR',u'STREET_NAM',u'UNIT_APT',u'COMMUNITY',u'B_TYPE']
    , "Washington":         [u'OBJECTID',u'STRUCTURE_',u'STRUCTURE1',u'PREFIX_DIR',u'STREET_TYP',u'STREET_NAM',u'SUFFIX_DIR',u'UNIT_TYPE',u'SITE_TYPE',u'UNIT_NUMBE',u'COMMUNITY',u'STATE',u'ZIP_CODE']
    , "Wicomico":           [u'OBJECTID',u'STRTNUM',u'ADDRESS',u'NAME',u'STRTTYP',u'STRTDIR',u'STRTNAM',u'STRTSFX',u'STRTUNT',u'CITY',u'ZIPCODE']
    , "Worcester":          [u'OBJECTID',u'ST_TYPE',u'ST_NUMBER',u'ST_NUM_SUFFIX',u'ST_PREFIX',u'ST_NAME',u'ST_SUFFIX',u'UNIT_TYPE',u'UNIT_NUMBER',u'comunity_l',u'ZIPcode']}
    # Make an ordered dictionary so that the datasets are processed in alphabetical. Makes for more readable output.
dictRequiredFields_SORTED = OrderedDict(sorted(dictRequiredFields.items()))

# FUNCTIONS
def printAndLog(strMessage, strLogLevel):
    strMessage = strMessage.strip("\n")
    if strLogLevel is strInfo:
        logging.info(strMessage)
    elif strLogLevel is strWarning:
        logging.warning(strMessage)
    elif strLogLevel is strError:
        logging.warning(strMessage)
    print(strMessage)
    return

def checkSchema(strRootGeodatabasePath, strCountyName, lsRequiredFields, lsFeatureClassesInMasterGDB):
    """Check the fields of a feature class against a list of required fields"""
    count = 0
    lsFieldsToInvestigate_Unicode = []
    strSubmittedFCPath = path.join(strRootGeodatabasePath, strCountyName)

    # check that the feature class is part of the data submitted
    if strCountyName not in lsFeatureClassesInMasterGDB:
        printAndLog(strPSAFeatureClassNotPresent.format(strCountyName), strInfo)
        return
    printAndLog(strPSAPathBeingExamined.format(strCountyName), strInfo)

    # generate a list of field names from the list of fields output by the arcpy.ListFields function
    try:
        lsFieldList = [f.name for f in ListFields(strSubmittedFCPath)]
    except:
        printAndLog(strPSAErrorListFeatureClasses.format(strCountyName), strError)
        printAndLog(strPSAGeoprocessingError.format(GetMessages(2)), strError)
        exit()

    # step through every feature class field and see if it is in the required fields list
    while count < len(lsRequiredFields):
        # if in the list then move on. if not in the list then add it to the list of fields to investigate
        if lsRequiredFields[count] in lsFieldList:
            pass
        else:
            lsFieldsToInvestigate_Unicode.append(lsRequiredFields[count])
        count += 1

    # convert from unicode strings to byte strings (per previous version)
    lsFieldsToInvestigate = [field.encode("utf-8") for field in lsFieldsToInvestigate_Unicode]

    if len(lsFieldsToInvestigate) == 0:
        printAndLog(strPSAAllRequiredFieldsPresent, strInfo)
    else:
        printAndLog(strPSAFieldsNotPresentInSubmittedData.format(lsFieldsToInvestigate), strWarning)
    return

# FUNCTIONALITY
printAndLog(strPSAForLogging_ScriptInitiated, strInfo)

    # Is the gdb path valid
if not path.exists(strRootGeodatabasePath):
    printAndLog("Path {} does not exist.\n".format(strRootGeodatabasePath), strError)
    exit()
else:
    env.workspace = strRootGeodatabasePath
    # Make a list of the feature classes to know which ones are valid, for schema check process
lsFeatureClassesInMasterGDB = ListFeatureClasses(wild_card=None,feature_type="Point",feature_dataset=None)
for key, value in dictRequiredFields_SORTED.iteritems():
    checkSchema(strRootGeodatabasePath, key, value, lsFeatureClassesInMasterGDB)