# import textwrap
# import requests
# import json
# import pyodbc
# import pandas as pd
# import urllib
#
# # headers = {'CLIENTAPIKEY': '5ce554c2-1332-481e-97c2-5856d9612433'}
# # a = 0;
# # detail_data = []
# # all_cover_url = []
# # # for x in range (int(22199/20)):
# # URL = "https://api-smartapp.namdinh.gov.vn/api/articles/?limit=20&offset=22180"
# # r = requests.get(url=URL, headers=headers)
# # data = r.json()
# # x = json.dumps(data)
# # json_object = json.loads(x)
# # n = len(json_object["results"]["data"])
# # for i in range(n):
# #     category = json_object["results"]["data"][i]["category"]
# #     cover_url = json_object["results"]["data"][i]["cover_url"]
# #     place_name = json_object["results"]["data"][i]["place_name"]
# #     title = json_object["results"]["data"][i]["title"]
# #     content = json_object["results"]["data"][i]["content"]
# #     extra_info = json_object["results"]["data"][i]["extra_info"]
# #     website = json_object["results"]["data"][i]["website"]
# #     phone_contact = json_object["results"]["data"][i]["phone_contact"]
# #     latitude = json_object["results"]["data"][i]["latitude"]
# #     longitude = json_object["results"]["data"][i]["longitude"]
# #     date_start = json_object["results"]["data"][i]["date_start"]
# #     time_start = json_object["results"]["data"][i]["time_start"]
# #     date_end = json_object["results"]["data"][i]["date_end"]
# #     time_end = json_object["results"]["data"][i]["time_end"]
# #     data = [category,cover_url,place_name,title,content,extra_info,website,phone_contact,latitude,longitude,date_start,time_start,date_end,time_end]
# #     print(cover_url)
# #     all_cover_url.append(cover_url)
# #     detail_data.append(data)
# #     i = i+1;
# #     # a = a + 20
# # b = 0;
# # for x in range(len(all_cover_url)):
# #     if all_cover_url[b] is not None:
# #         img_name = all_cover_url[x].split("/")[-1]
# #         urllib.request.urlretrieve(all_cover_url[x], "C:/Users/Admin/Desktop/anh/" + img_name)
# #         b = b + 1;
# #     else:
# #         b = b + 1;
# # for index, row in enumerate(detail_data):
# #     # define an insert query with place holders for the values.
# #     insert_query = textwrap.dedent('''
# #         INSERT INTO dia_diem (category,
# #         cover_url,
# #         place_name,
# #         title,content,
# #         extra_info,
# #         website,
# #         phone_contact,
# #         latitude,
# #         longitude,
# #         date_start,
# #         time_start,
# #         date_end,
# #         time_end)
# #         VALUES (?,?,?,?,?,?,?,?,?,?,?,?`,?,?);
# #     ''')
# #     # define the values`
# #     values = (row[0], row[1], row[2], row[3],row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
# #     # insert the data into the database
# #     cursor.execute(insert_query, values)
# # # commit the inserts.
# # cnxn.commit()
# # # grab all the rows from the table
# # cursor.execute('SELECT * FROM dia_diem')
# # # for row in cursor:
# # #     print(row)
# # # close the cursor and connection
# # cursor.close()
# # cnxn.close()
# # print("done!")
# detail_data = []
# _data = []
# server = 'ADMIN'
# database = 'NNLogin'
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
# cursor = cnxn.cursor()
# with open('GT_NOTICE_BOARD_TYPE.json') as json_file:
#     data = json.load(json_file)
#     print(data[1]['Icon'])
#     detail_data.append(data[1]['Icon'])
#     print(detail_data)
#     n = len(data)
#     for i in range(n):
#         Type_ID = str(data[i]['Type_ID']),
#         category = data[i]['category'],
#         Icon = data[i]['Icon'],
#         IsDelete = str(data[i]['IsDelete'])
#         # detail_data.append(data)
# # print(detail_data)
# for index, row in enumerate(detail_data):
#     # define an insert query with place holders for the values.
#     insert_query = textwrap.dedent('''
#         INSERT INTO loai_bien_bao (Type_ID,
#         category,
#         Icon,
#         IsDelete
#         )
#         VALUES (?,?,?,?);
#     ''')
#     # define the values`
#     values = (row[0], row[1], row[2], row[3])
#     # insert the data into the database
#     cursor.execute(insert_query, values)
# # commit the inserts.
# cnxn.commit()
# # grab all the rows from the table
# cursor.execute('SELECT * FROM loai_bien_bao')
# # for row in cursor:
# #     print(row)
# # close the cursor and connection
# cursor.close()
# cnxn.close()
# print("done!")
#
#
#
# # print(len(data))
# # print(data[1]['Type_ID'])
#
#
#

###code loai bien giao thong
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

# headers = {'CLIENTAPIKEY': '5ce554c2-1332-481e-97c2-5856d9612433'}
# a = 0;
# detail_data = []
# all_cover_url = []
# with open('GT_NOTICE_BOARD.json',  encoding='utf-8') as json_file:
#      data = json.load(json_file)
#      x = json.dumps(data)
#      json_object = json.loads(x)
#      n = len(json_object)
# for i in range(n):
#     Type_ID =  json_object_category["results"]["data"][i]["Type_ID"]
#     Name =  json_object_category["results"]["data"][i]["Name"]
#     NameEN =  json_object_category["results"]["data"][i]["NameEN"]
#     Detail =  json_object_category["results"]["data"][i]["Detail"]
#     Icon =  json_object_category["results"]["data"][i]["Icon"]
#     UpdateDay =  json_object_category["results"]["data"][i]["UpdateDay"]
#     IsDelete =  json_object_category["results"]["data"][i]["IsDelete"]
#
#     # if str(category) == "To??n b???":
#     #      json_object_category["results"]["data"][i]["id"] = 3
#     #     print( json_object_category["results"]["data"][i])
#     data = [Type_ID, Name, NameEN,Detail,Icon,UpdateDay,IsDelete]
#     detail_data.append(data)
# for index, row in enumerate(detail_data):
#     # define an insert query with place holders for the values.
#     insert_query = textwrap.dedent('''
#         INSERT INTO NoticeBoardDetail (Type_ID,
#         Name,
#         NameEN,
#         Detail,
#         Icon,
#         UpdateDay,
#         IsDelete)
#         VALUES (?,?,?,?,?,?,?);
#     ''')
#     # define the values
#     values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
#     # insert the data into the database
#     cursor.execute(insert_query, values)
# # commit the inserts.
# cnxn.commit()
# # grab all the rows from the table
# cursor.execute('SELECT * FROM NoticeBoardDetail')
# # for row in cursor:
# #     print(row)
# # close the cursor and connection
# cursor.close()
# cnxn.close()
# print("done!")

###code ????? d??? li???u c??c danh m???c
# import textwrap
# import requests
# import json
# import pyodbc
# import pandas as pd
# import urllib
# server = 'ADMIN'
# database = 'NNLogin'
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
# cursor = cnxn.cursor()
#
# headers = {'CLIENTAPIKEY': '5ce554c2-1332-481e-97c2-5856d9612433'}
# a = 0;
# detail_data = []
# all_cover_url = []
# with open('GT_NOTICE_BOARD_TYPE.json',  encoding='utf-8') as json_file:
#      data = json.load(json_file)
#      x = json.dumps(data)
#      json_object = json.loads(x)
#      n = len(json_object)

##c??ch vi???t kh??c
#
headers = {'CLIENTAPIKEY': '5ce554c2-1332-481e-97c2-5856d9612433'}
a = 0;
detail_data = []
all_cover_url = []
for x in range(1):
    URL = "https://api-smartapp.namdinh.gov.vn/api/articles/?limit=20&offset=22180"
    r = requests.get(url=URL, headers=headers)
    data = r.json()
    x = json.dumps(data)
    json_object_category = json.loads(x)
    n = len(json_object_category["results"]["data"])
    a = a + 20
    print(n)
    for i in range(n):
        category = json_object_category["results"]["data"][i]["category"]
        cover_url = json_object_category["results"]["data"][i]["cover_url"]
        place_name =  json_object_category["results"]["data"][i]["place_name"]
        title = json_object_category["results"]["data"][i]["title"]
        content = json_object_category["results"]["data"][i]["content"]
        extra_info = json_object_category["results"]["data"][i]["extra_info"]
        website =  json_object_category["results"]["data"][i]["website"]
        phone_contact = json_object_category["results"]["data"][i]["phone_contact"]
        latitude = json_object_category["results"]["data"][i]["latitude"]
        longitude = json_object_category["results"]["data"][i]["longitude"]
        date_start = json_object_category["results"]["data"][i]["date_start"]
        time_start = json_object_category["results"]["data"][i]["time_start"]
        date_end = json_object_category["results"]["data"][i]["date_end"]
        time_end = json_object_category["results"]["data"][i]["time_end"]
        if str(category) == "??i???m mua s???m":
          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 3
        elif category == "Nh?? h??ng":
          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 1
        elif category == "B???nh vi???n":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 2
        elif category == "??i???m ????? xe":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 4
        elif category == "?????a ??i???m n???i ti???ng":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 5
        elif category == "Di t??ch l???ch s???":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 6
        elif category == "S??? ki???n d???p T???t":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 7
        elif category == "L??? h???i":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 8
        elif category == "Danh lam th???ng c???nh":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 9
        elif category == "?????n":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 10
        elif category == "Ch??a":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 11
        elif category == "Hi???u thu???c":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 12
        elif category == "Ph??ng kh??m":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 13
        elif category == "Kh??ch s???n":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 14
        elif category == "??i???m ??en giao th??ng":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 15
        elif category == "Tr???m thu ph??":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 16
        elif category == "Gara ?? t??":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 17
        elif category == "Tr???m x??ng":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 18
        elif category == "??i???m ???ng c???u TNGT":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 19
        elif category == "??i???m khuy???n m???i":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 20
        elif category == "Nh?? th???":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 21
        elif category == "B???o tr??? x?? h???i":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 22
        elif category == "Tr???m y t???":
         json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 23
        DanhMucTheoLinhVucId = json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"]
        data = [DanhMucTheoLinhVucId,title,cover_url,time_start,place_name,latitude,longitude,phone_contact,website,extra_info,content]
        detail_data.append(data)
print(detail_data)
for index, row in enumerate(detail_data):
    # define an insert query with place holders for the values.
    insert_query = textwrap.dedent('''
        INSERT INTO DiaDiem (DanhMucTheoLinhVucId,
        TenDiaDiem,
        AnhDaiDien,
        GioMoCua,
        DiaChi,
        ToaDoX,
        ToaDoY,
        SoDienThoai,
        TrangWeb,
        ThongTinThem,
        MoTa)
        VALUES (?,?,?,?,?,?,?,?,?,?,?);
    ''')
    # define the values
    values = (row[0], row[1], row[2], row[3], row[4],row[5],row[6],row[7],row[8],row[9],row[10])
    # insert the data into the database
    cursor.execute(insert_query, values)
# commit the inserts.
cnxn.commit()
# grab all the rows from the table
cursor.execute('SELECT * FROM DiaDiem')
# for row in cursor:
#     print(row)
# close the cursor and connection
cursor.close()
cnxn.close()
print("done!")



