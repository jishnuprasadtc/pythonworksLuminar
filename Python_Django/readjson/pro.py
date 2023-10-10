#FROM EXTENTION IMPORT LOAD // USE * FOR IMPORT THE ALL
from json import load
path="C:\\Users\\DELL\\OneDrive\\Desktop\\Python_Django\\readjson\\data.json"
with open(path) as f:  #** WITH OPEN (PATH OF FILE) AS F
    record=load(f)
# print(record)

#1ST STOR IN VARIABLE

# fw=[f.get("name") for r in record]
# print(fw)


topfw=max(record,key=lambda d: d.get("rating"))
print(topfw)




