import textwrap
import requests
import json
import pyodbc
import pandas as pd
import urllib
server = 'ADMIN'
database = 'NNLogin'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
cursor = cnxn.cursor()

headers = {'CLIENTAPIKEY': '5ce554c2-1332-481e-97c2-5856d9612433'}
a = 0;
detail_data = []
all_cover_url = []
# for x in range (int(22199/20)):
URL = "https://api-smartapp.namdinh.gov.vn/api/articles/?limit=20&offset=22180"
r = requests.get(url=URL, headers=headers)
data = r.json()
x = json.dumps(data)
json_object = json.loads(x)
n = len(json_object["results"]["data"])
for i in range(n):
    category = json_object["results"]["data"][i]["category"]
    cover_url = json_object["results"]["data"][i]["cover_url"]
    place_name = json_object["results"]["data"][i]["place_name"]
    title = json_object["results"]["data"][i]["title"]
    content = json_object["results"]["data"][i]["content"]
    extra_info = json_object["results"]["data"][i]["extra_info"]
    website = json_object["results"]["data"][i]["website"]
    phone_contact = json_object["results"]["data"][i]["phone_contact"]
    latitude = json_object["results"]["data"][i]["latitude"]
    longitude = json_object["results"]["data"][i]["longitude"]
    date_start = json_object["results"]["data"][i]["date_start"]
    time_start = json_object["results"]["data"][i]["time_start"]
    date_end = json_object["results"]["data"][i]["date_end"]
    time_end = json_object["results"]["data"][i]["time_end"]
    data = [category,cover_url,place_name,title,content,extra_info,website,phone_contact,latitude,longitude,date_start,time_start,date_end,time_end]
    print(cover_url)
    all_cover_url.append(cover_url)
    detail_data.append(data)
    i = i+1;
    # a = a + 20
b = 0;
print(detail_data)
# for x in range(len(all_cover_url)):
#     if all_cover_url[b] is not None:
#         img_name = all_cover_url[x].split("/")[-1]
#         urllib.request.urlretrieve(all_cover_url[x], "C:/Users/Admin/Desktop/anh/" + img_name)
#         b = b + 1;
#     else:
#         b = b + 1;
# for index, row in enumerate(detail_data):
#     # define an insert query with place holders for the values.
#     insert_query = textwrap.dedent('''
#         INSERT INTO dia_diem (category,
#         cover_url,
#         place_name,
#         title,content,
#         extra_info,
#         website,
#         phone_contact,
#         latitude,
#         longitude,
#         date_start,
#         time_start,
#         date_end,
#         time_end)
#         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);
#     ''')
#     # define the values
#     values = (row[0], row[1], row[2], row[3],row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
#     # insert the data into the database
#     cursor.execute(insert_query, values)
# # commit the inserts.
# cnxn.commit()
# # grab all the rows from the table
# cursor.execute('SELECT * FROM dia_diem')
# # for row in cursor:
# #     print(row)
# # close the cursor and connection
# cursor.close()
# cnxn.close()
# print("done!")
#


