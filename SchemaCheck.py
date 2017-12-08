# This script is used to identify schema changes that exist in processed county data by comparing a list of
# fields required by the ETL (required fields) to a list of fields present in the processed county data (fieldlist).
# The results of the check will be retured via IDLE.  If any required fields are reported back for a given county,
# the county data will not work properly with the ETL because it expects the required field(s) to be present.

import arcpy
import sys
import re
import string

arcpy.AddMessage("Running Schema Check")

# Hardcoded UNC to the location of the processed Allegany County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\Allegany"

### For Allegany County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'objectid',u'streetsuf',u'siteaddid',u'preaddrnum',u'addrnum',u'addrnumsuf',u'prefix',u'streetname',u'postdir',u'fullname',u'unittype',u'unitid',u'msag',u'zip',u'addrclass']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Allegany County Has All Required Fields!")
else:    
    print ("Allegany County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)



    
# Hardcoded UNC to the location of the processed Anne Arundel County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\AnneArundel"

### For Anne Arundel County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'BMC_ID',u'ST_TYPE',u'ST_NAME',u'ST_NUMSUFF',u'ST_PREFIXD',u'ST_SUFFIXD',u'UNIT_TYPE',u'UNITNUM',u'UNIT_ADDR',u'FULL_ADDRE',u'BLDG_NAME',u'CITY_NAME',u'ZIPCODE',u'GlobalID',u'ST_NUMBER']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Anne Arundel County Has All Required Fields!")
else:    
    print ("Anne Arundel County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)




# Hardcoded UNC to the location of the processed Baltimore City data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\BaltimoreCity"

### For Baltimore City, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'ADDRPT_ID',u'ST_NAME',u'ST_DIR',u'ADDR_FRAC',u'ZIP_CODE',u'ADDR_NUMBE',u'ST_TYPE']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Baltimore City Has All Required Fields!")
else:    
    print ("Baltimore City Fields That Do Not Exist In Submitted Data:")
    print (checkfields)




# Hardcoded UNC to the location of the processed Baltimore County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\BaltimoreCounty"

### For Baltimore County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'ST_TYPE',u'ST_NAME',u'ST_PREFIXTYPE',u'ST_NUMSUFFIX',u'ST_PREMOD',u'ST_PREFIXDIR',u'ST_SUFFIXDIR',u'ST_POSTMOD',u'ADDRLABEL',u'CITY_POSTAL',u'STATE',u'ZIP',u'ADDRESSUSE',u'ST_NUMBER']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Baltimore County Has All Required Fields!")
else:    
    print ("Baltimore County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)




    
# Hardcoded UNC to the location of the processed Calvert County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\Calvert"

### For Calvert County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'PREMSNUM',u'PREMSDIR',u'PREMSNAM',u'PREMSTYP',u'ALPHA',u'PREMCITY',u'PREMZIP']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Calvert County Has All Required Fields!")
else:    
    print("Calvert County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)




# Hardcoded UNC to the location of the processed Caroline County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\Caroline"

### For Caroline County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'STRT_ADD',u'STRT_PFX',u'STRT_NAME',u'UNIT',u'COMMUNITY',u'ZIP',u'TYP',u'TYPE']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Caroline County Has All Required Fields!")
else:    
    print("Caroline County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)



# Hardcoded UNC to the location of the processed Carroll County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\Carroll"

### For Carroll County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'ST_TYPE',u'ST_NAME',u'ST_NUM_SUF',u'ST_PREFIX',u'ST_SUFFIX',u'UNIT_TYPE',u'UNIT_NUMBE',u'County',u'ZIPCODE',u'ST_NUMBER']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Carroll County Has All Required Fields!")
else:    
    print ("Carroll County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)




    
# Hardcoded UNC to the location of the processed Cecil County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\Cecil"

### For Cecil County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'STRT_ADD',u'STRT_PFX',u'STRT_NAME',u'STRT_SUF',u'UNIT',u'Comment',u'COMMUNITY',u'TYP',u'TYPE',u'NAME']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Cecil County Has All Required Fields!")
else:    
    print ("Cecil County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)




### Hardcoded UNC to the location of the processed Charles County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\Charles"

### For Charles's County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'NEWCITY',u'NUMBER_',u'Street_Pre',u'Street_Nam',u'Street_typ',u'Street_Suf',u'ZIP',u'Addl_Info']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Charles County Has All Required Fields!")
else:    
    print ("Charles County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)



    
### Hardcoded UNC to the location of the processed Dorchester County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\Dorchester"

### For Dorchester County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'STRTTYP',u'STRTNUM',u'STRTDIR',u'STRTNAM',u'STRTSFX',u'STRTUNT',u'COMMUNITY']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Dorchester County Has All Required Fields!")
else:    
    print ("Dorechester County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)




### Hardcoded UNC to the location of the processed Frederick County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\Frederick"

### For Frederick County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'ST_TYPE',u'ST_NUM',u'ST_NUM_SUFFIX',u'ST_PREFIX',u'ST_NAME',u'ST_SUFFIX',u'UNIT_TYPE',u'UNIT_NUM',u'CITY',u'STATE',u'ZIP_STNM',u'ADDR_TYPE']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Frederick County Has All Required Fields!")
else:    
    print ("Frederick County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)




### Hardcoded UNC to the location of the processed Garrett County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\Garrett"

### For Garrett County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'STRUCTURE_NUMBER',u'STRUCTURE_NUMBER_SUFFIX',u'PREFIX_DIRECTIONAL',u'STREET_NAME',u'STREET_TYPE',u'SUFFIX_DIRECTIONAL',u'UNIT_TYPE',u'UNIT_NUMBER',u'CITY',u'COMMUNITY',u'STATE',u'ZIP_CODE']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Garrett County Has All Required Fields!")
else:    
    print ("Garrett County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)




# Hardcoded UNC to the location of the processed Harford County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\Harford"

### For Harford County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'P_ST_TYPE',u'P_ST_NAME',u'P_ST_SUF',u'P_ST_DIREC',u'P_CITY',u'P_Z_1',u'P_ST_NO']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Harford County Has All Required Fields!")
else:    
    print ("Harford County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)





 # Hardcoded UNC to the location of the processed Howard County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\Howard"

### For Howard County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'PREMSTYP',u'PREMSNAM',u'PREMSNAM',u'STREETNAME',u'SUBADDRESS',u'PREMCITY',u'PREMZIP',u'ADDRESSNO']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Howard County Has All Required Fields!")
else:    
    print ("Howard County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)




    
# Hardcoded UNC to the location of the processed Kent County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\Kent"

### For Kent County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'TYP',u'STRT_ADD',u'STRT_PFX',u'STRT_NAME',u'STREET',u'UNIT',u'COMMUNITY',u'TYPE']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Kent County Has All Required Fields!")
else:    
    print ("Kent County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)



    
### Hardcoded UNC to the location of the processed Montgomery County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\Montgomery"

### For Montgomery County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'ADDRNUM',u'PRE_DIR',u'STREET_NAM',u'STREET_TYP',u'SUF_DIR',u'POSTAL_CIT',u'ZIP']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Montgomery County Has All Required Fields!")
else:    
    print ("Montgomery County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)





### Hardcoded UNC to the location of the processed Prince George's County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\PrinceGeorges"

### For Prince George's County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'ADDRESS_NUMBER_PREFIX',u'ADDRESS_NUMBER',u'ADDRESS_NUMBER_SUFFIX',u'STREET_NAME_PRE_MODIFIER',u'STREET_NAME_PRE_DIRECTIONAL',u'STREET_NAME_PRE_TYPE',u'STREET_NAME',u'STREET_NAME_POST_DIRECTIONAL',u'STREET_NAME_POST_MODIFIER',u'COMPLETE_STREET_NAME',u'SUBADDRESS_TYPE1',u'SUBADDRESS_IDENTIFIER1',u'LANDMARK_NAME1',u'COMPLETE_LANDMARK_NAME',u'PLACE_NAME',u'STATE_NAME',u'ZIP_CODE']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Prince George's County Has All Required Fields!")
else:    
    print ("Prince George's County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)




### Hardcoded UNC to the location of the processed Queen Anne's County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\QueenAnnes"

### For Queen Anne's County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'STRT_ADD',u'STRT_PFX',u'TYP',u'STRT_NAME',u'STRT_SFX',u'STREET',u'UNIT',u'COMMUNITY',u'TYPE']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Queen Anne's County Has All Required Fields!")
else:    
    print ("Queen Anne's County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)




### Hardcoded UNC to the location of the processed Somerset County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\Somerset"

### For Somerset County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'STRNUM',u'STRTYPE',u'STRDIR',u'STRNAM',u'UNITTYPE',u'UNIT',u'CITY',u'ZIP',u'MYPROPERTY']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Somerset County Has All Required Fields!")
else:    
    print ("Somerset County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)




# Hardcoded UNC to the location of the processed St. Mary's County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\StMarys"

### For St Mary's County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'ST_TYPE',u'HOUSE_NO',u'ST_DIR',u'ST_NAME',u'APT_NO',u'ZIP']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("St Mary's County Has All Required Fields!")
else:    
    print ("St Mary's County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)




# Hardcoded UNC to the location of the processed Talbot County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\Talbot"

### For Talbot County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'STRT_ADDR',u'PREF_DIR',u'STREET',u'SUFF_TYPE',u'SUFF_DIR',u'STREET_NAM',u'UNIT_APT',u'COMMUNITY',u'B_TYPE']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Talbot County Has All Required Fields!")
else:    
    print ("Talbot County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)




### Hardcoded UNC to the location of the processed Washington County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\Washington"

### For Washington County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'STRUCTURE_',u'STRUCTURE1',u'PREFIX_DIR',u'STREET_TYP',u'STREET_NAM',u'SUFFIX_DIR',u'UNIT_TYPE',u'SITE_TYPE',u'UNIT_NUMBE',u'COMMUNITY',u'STATE',u'ZIP_CODE']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Washington County Has All Required Fields!")
else:    
    print ("Washington County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)




# Hardcoded UNC to the location of the processed Wicomico County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\Wicomico"

### For Wicomico County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'STRTNUM',u'ADDRESS',u'NAME',u'STRTTYP',u'STRTDIR',u'STRTNAM',u'STRTSFX',u'STRTUNT',u'CITY',u'ZIPCODE']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Wicomico County Has All Required Fields!")
else:    
    print ("Wicomico County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)




### Hardcoded UNC to the location of the processed Worcester County data.
submittedFC = r"D:\ETL\Addresses\Data\SubmittedData.gdb\Worcester"

### For Worcester County, check schema by comparing list of submitted feature class' field names with the original feature class' field names.

fieldlist = [f.name for f in arcpy.ListFields(submittedFC)]
requiredfields = [u'OBJECTID',u'ST_TYPE',u'ST_NUMBER',u'ST_NUM_SUFFIX',u'ST_PREFIX',u'ST_NAME',u'ST_SUFFIX',u'UNIT_TYPE',u'UNIT_NUMBER',u'comunity_l',u'ZIPcode']
checkfields = []
count = 0

while count < len(requiredfields):
    if requiredfields[count] in fieldlist:
        checkfields = checkfields
    else:
        checkfields.append(requiredfields[count])
    count = count + 1

checkfields = re.sub("u'",'',str(checkfields))
checkfields = re.sub("',"," ",checkfields)

if len(checkfields) == 2:
    print ("Worcester County Has All Required Fields!")
else:    
    print ("Worcester County Fields That Do Not Exist In Submitted Data:")
    print (checkfields)
