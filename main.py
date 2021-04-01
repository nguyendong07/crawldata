import textwrap
import requests
import json
import pyodbc
import pandas as pd
server = 'ADMIN'
database = 'NNLogin'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
cursor = cnxn.cursor()
insert_query = textwrap.dedent('''
      INSERT INTO danh_muc (id, name, image, description) 
      VALUES (?, ?, ?, ?);
  ''')
URL = "https://api-smartapp.namdinh.gov.vn/api/articles/categories"
# sending get request and saving the response as response object
headers = {'CLIENTAPIKEY': '5ce554c2-1332-481e-97c2-5856d9612433'}
r = requests.get(url=URL,  headers = headers)
# extracting data in json format
data = r.json()
x = json.dumps(data)
json_object = json.loads(x)
n = len(json_object["results"]["data"])
price_data = []
for i in range(n):
    data = [json_object["results"]["data"][i]["id"], json_object["results"]["data"][i]["name"],json_object["results"]["data"][i]["image"],json_object["results"]["data"][i]["description"]]
    price_data.append(data)
    i = i+1;

print(price_data)
for index, row in enumerate(price_data):
    # define an insert query with place holders for the values.
    insert_query = textwrap.dedent('''
        INSERT INTO danh_muc (id, name, image, description)
        VALUES (?,?, ?, ?);
    ''')
    # define the values
    values = (row[0], row[1], row[2], row[3])
    # insert the data into the database
    cursor.execute(insert_query, values)
# commit the inserts.
cnxn.commit()
# grab all the rows from the table
cursor.execute('SELECT * FROM danh_muc')
for row in cursor:
    print(row)
# close the cursor and connection
cursor.close()
cnxn.close()
# for driver in pyodbc.drivers():
#     print(driver)