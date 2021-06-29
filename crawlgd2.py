import urllib.parse
import textwrap
import requests
import json
import pyodbc
import pandas as pd
import urllib
headers = {'CLIENTAPIKEY': '5ce554c2-1332-481e-97c2-5856d9612433'}



detail_data = []
server = 'ADMIN'
database = 'NNLogin'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
cursor = cnxn.cursor()

url_job = "https://api-smartapp.namdinh.gov.vn/api/law_database"
r = requests.get(url=url_job, headers=headers)
data = r.json()
x = json.dumps(data)
json_object_category = json.loads(x)
print(json_object_category)
n = len(json_object_category["results"]["data"])
print(n)
for i in range(19):
     url_job = "https://api-smartapp.namdinh.gov.vn/api/law_database/"+str(i+1)
     r = requests.get(url=url_job, headers=headers)
     data = r.json()
     x = json.dumps(data)
     json_object_category = json.loads(x)
     id = json_object_category["results"]["data"]["id"]
     name = json_object_category["results"]["data"]["name"]
     code =  json_object_category["results"]["data"]["code"]
     created_at = json_object_category["results"]["data"]["created_at"]
     cover_url = json_object_category["results"]["data"]["cover_url"]
     date_issued = json_object_category["results"]["data"]["date_issued"]
     effective_date = json_object_category["results"]["data"]["effective_date"]
     signer = json_object_category["results"]["data"]["signer"]
     abstract = json_object_category["results"]["data"]["abstract"]
     agency_issued = json_object_category["results"]["data"]["agency_issued"]
     classify = json_object_category["results"]["data"]["classify"]
     file = json_object_category["results"]["data"]["file"]
     data = [id, name, cover_url, code, date_issued, effective_date, signer, abstract, agency_issued, classify, file, created_at]
     detail_data.append(data)
#     wage = json_object_category["results"]["data"][i]["wage"]
#     application_deadline = json_object_category["results"]["data"][i]["application_deadline"]
#     address =  json_object_category["results"]["data"][i]["address"]
#     cover_url = json_object_category["results"]["data"][i]["cover_url"]
#     form_of_work_name = json_object_category["results"]["data"][i]["form_of_work_name"]
#     number_of_job = json_object_category["results"]["data"][i]["number_of_job"]
#     position_name = json_object_category["results"]["data"][i]["position_name"]
#     gender_name = json_object_category["results"]["data"][i]["gender_name"]
#     created_at = json_object_category["results"]["data"][i]["created_at"]

#     data = [status,job,career_name,company,wage,application_deadline,address,cover_url,form_of_work_name,number_of_job,position_name,gender_name,created_at]

print(detail_data)
for index, row in enumerate(detail_data):
#     # define an insert query with place holders for the values.
    insert_query = textwrap.dedent('''
         INSERT INTO LawDataBaseDetail (id_lawdatabase,
         name,
         cover_url,
         code,
         date_issued,
         effective_date,
         signer,
         abstract,
         agency_issued,
         classify,
         files,
         created_at)
         VALUES (?,?,?,?,?,?,?,?,?,?,?,?);
     ''')
#     # define the values
    values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
    # insert the data into the database
    cursor.execute(insert_query, values)
# commit the inserts.
cnxn.commit()
# grab all the rows from the table
cursor.execute('SELECT * FROM LawDataBaseDetail')
# for row in cursor:
#     print(row)
# close the cursor and connection
cursor.close()
# cnxn.close()
# print("done!")
#
#
#
