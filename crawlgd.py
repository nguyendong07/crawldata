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

url_job = ["https://api-smartapp.namdinh.gov.vn/api/apprentice/training_course?category=Ẩm Thực",
           "https://api-smartapp.namdinh.gov.vn/api/apprentice/training_course?category=Kỹ năng mềm",
           "https://api-smartapp.namdinh.gov.vn/api/apprentice/training_course?category=Kinh doanh, Khởi nghiệp"]
url_eng = ["https://api-smartapp.namdinh.gov.vn/api/englishes/lesson?level=Trình độ - A1",
           "https://api-smartapp.namdinh.gov.vn/api/englishes/lesson?level=Trình độ - A2",
           "https://api-smartapp.namdinh.gov.vn/api/englishes/lesson?level=Trình độ - B1",
           "https://api-smartapp.namdinh.gov.vn/api/englishes/lesson?level=Trình độ - B2",
           "https://api-smartapp.namdinh.gov.vn/api/englishes/lesson?level=Trình độ - C1"]
for x in range(len(url_eng)):
    r = requests.get(url_eng[x], headers=headers)
    url_tail = url_eng[x].split("=")[1]
    data = r.json()
    x = json.dumps(data)
    json_object_category = json.loads(x)
    n = len(json_object_category["results"]["data"])
    for a in range(n):
        name = json_object_category["results"]["data"][a]["name"]
        # if (url_tail == "Trình độ - A1"):
        #     json_object_category["results"]["data"][a]["LevelCourseId"] = 4
        # elif (url_tail == "Trình độ - A2"):
        #     json_object_category["results"]["data"][a]["LevelCourseId"] = 5
        # elif (url_tail == "Trình độ - B1"):
        #     json_object_category["results"]["data"][a]["LevelCourseId"] = 6
        # elif (url_tail == "Trình độ - B2"):
        #     json_object_category["results"]["data"][a]["LevelCourseId"] = 7
        # elif (url_tail == "Trình độ - C1"):
        #     json_object_category["results"]["data"][a]["LevelCourseId"] = 8
        k = len(json_object_category["results"]["data"][a]["videos"])
        for b in range(k):
            title = json_object_category["results"]["data"][a]["videos"][b]["title"]
            image = json_object_category["results"]["data"][a]["videos"][b]["image"]
            source = json_object_category["results"]["data"][a]["videos"][b]["source"]
            view_quantity = json_object_category["results"]["data"][a]["videos"][b]["view_quantity"]
            #created_at = json_object_category["results"]["data"][a]["videos"][b]["created_at"]


            if (url_tail == "Trình độ - A1" and name == "Beginner"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 7
            elif (url_tail == "Trình độ - A1" and name == "Everyday"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 8
            elif (url_tail == "Trình độ - A1" and name == "At Work"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 9
            elif (url_tail == "Trình độ - A1" and name == "Travel"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 10

            elif (url_tail == "Trình độ - A2" and name == "Everyday"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 11
            elif (url_tail == "Trình độ - A2" and name == "At Work"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 12
            elif (url_tail == "Trình độ - A2" and name == "Friends"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 13
            elif (url_tail == "Trình độ - A2" and name == "Travel"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 14


            elif (url_tail == "Trình độ - B1" and name == "Everyday"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 15
            elif (url_tail == "Trình độ - B1" and name == "Travel"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 16
            elif (url_tail == "Trình độ - B1" and name == "At Work"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 17
            elif (url_tail == "Trình độ - B1" and name == "Friends"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 18


            elif (url_tail == "Trình độ - B2" and name == "At Work"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 19
            elif (url_tail == "Trình độ - B2" and name == "Travel"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 20

            elif (url_tail == "Trình độ - C1" and name == "White House"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 21
            CoursesListId = json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"]
            #LevelCourseId = json_object_category["results"]["data"][a]["LevelCourseId"]
            data = [CoursesListId, title, image, source, view_quantity]
            detail_data.append(data)
for i in range(len(detail_data)):
    print(detail_data[i])
for index, row in enumerate(detail_data):
    # define an insert query with place holders for the values.
    insert_query = textwrap.dedent('''
        INSERT INTO VideoCourse (CoursesListId,
        Title,
        ImageVideo,
        Source,
        ViewQuantity
        )
        VALUES (?,?,?,?,?);
    ''')
    # define the values
    values = (row[0], row[1], row[2], row[3], row[4])
    print(insert_query)
    # insert the data into the database
    cursor.execute(insert_query, values)
# commit the inserts.
cnxn.commit()
# grab all the rows from the table
cursor.execute('SELECT * FROM VideoCourse')
# for row in cursor:
#     print(row)
# close the cursor and connection
cursor.close()
cnxn.close()
print("done!")




# server = 'ADMIN'
# database = 'NNLogin'
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
# cursor = cnxn.cursor()
#
# headers = {'CLIENTAPIKEY': '5ce554c2-1332-481e-97c2-5856d9612433'}
# a = 0;
# detail_data = []
# all_cover_url = []
# for x in range(1):
#     URL = "https://api-smartapp.namdinh.gov.vn/api/articles/?limit=20&offset=22180"
#     r = requests.get(url=URL, headers=headers)
#     data = r.json()
#     x = json.dumps(data)
#     json_object_category = json.loads(x)
#     n = len(json_object_category["results"]["data"])
#     a = a + 20
#     print(n)
#     for i in range(n):
#         category = json_object_category["results"]["data"][i]["category"]
#         cover_url = json_object_category["results"]["data"][i]["cover_url"]
#         place_name =  json_object_category["results"]["data"][i]["place_name"]
#         title = json_object_category["results"]["data"][i]["title"]
#         content = json_object_category["results"]["data"][i]["content"]
#         extra_info = json_object_category["results"]["data"][i]["extra_info"]
#         website =  json_object_category["results"]["data"][i]["website"]
#         phone_contact = json_object_category["results"]["data"][i]["phone_contact"]
#         latitude = json_object_category["results"]["data"][i]["latitude"]
#         longitude = json_object_category["results"]["data"][i]["longitude"]
#         date_start = json_object_category["results"]["data"][i]["date_start"]
#         time_start = json_object_category["results"]["data"][i]["time_start"]
#         date_end = json_object_category["results"]["data"][i]["date_end"]
#         time_end = json_object_category["results"]["data"][i]["time_end"]
#         if str(category) == "Điểm mua sắm":
#           json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 3
#         elif category == "Nhà hàng":
#           json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 1
#         elif category == "Bệnh viện":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 2
#         elif category == "Điểm đỗ xe":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 4
#         elif category == "Địa điểm nổi tiếng":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 5
#         elif category == "Di tích lịch sử":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 6
#         elif category == "Sự kiện dịp Tết":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 7
#         elif category == "Lễ hội":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 8
#         elif category == "Danh lam thắng cảnh":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 9
#         elif category == "Đền":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 10
#         elif category == "Chùa":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 11
#         elif category == "Hiệu thuốc":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 12
#         elif category == "Phòng khám":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 13
#         elif category == "Khách sạn":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 14
#         elif category == "Điểm đen giao thông":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 15
#         elif category == "Trạm thu phí":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 16
#         elif category == "Gara ô tô":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 17
#         elif category == "Trạm xăng":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 18
#         elif category == "Điểm ứng cứu TNGT":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 19
#         elif category == "Điểm khuyến mại":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 20
#         elif category == "Nhà thờ":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 21
#         elif category == "Bảo trợ xã hội":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 22
#         elif category == "Trạm y tế":
#          json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"] = 23
#         DanhMucTheoLinhVucId = json_object_category["results"]["data"][i]["DanhMucTheoLinhVucId"]
#         data = [DanhMucTheoLinhVucId,title,cover_url,time_start,place_name,latitude,longitude,phone_contact,website,extra_info,content]
#         detail_data.append(data)
# print(detail_data)
# for index, row in enumerate(detail_data):
#     # define an insert query with place holders for the values.
#     insert_query = textwrap.dedent('''
#         INSERT INTO DiaDiem (DanhMucTheoLinhVucId,
#         TenDiaDiem,
#         AnhDaiDien,
#         GioMoCua,
#         DiaChi,
#         ToaDoX,
#         ToaDoY,
#         SoDienThoai,
#         TrangWeb,
#         ThongTinThem,
#         MoTa)
#         VALUES (?,?,?,?,?,?,?,?,?,?,?);
#     ''')
#     # define the values
#     values = (row[0], row[1], row[2], row[3], row[4],row[5],row[6],row[7],row[8],row[9],row[10])
#     # insert the data into the database
#     cursor.execute(insert_query, values)
# # commit the inserts.
# cnxn.commit()
# # grab all the rows from the table
# cursor.execute('SELECT * FROM DiaDiem')
# # for row in cursor:
# #     print(row)
# # close the cursor and connection
# cursor.close()
# cnxn.close()
# print("done!")
#
#
#
