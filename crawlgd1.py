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
LevelCourseId = 0
for x in range(len(url_job)):
    r = requests.get(url_job[x], headers=headers)
    url_tail = url_job[x].split("=")[1]
    #print(url_tail)
    data = r.json()
    x = json.dumps(data)
    json_object_category = json.loads(x)
    n = len(json_object_category["results"]["data"])
    for a in range(n):
        json_object_category["results"]["data"][a]["LevelCourseId"] = 0
        name = json_object_category["results"]["data"][a]["name"]
        # print(json_object_category["results"]["data"][a])
        #print(name)
        # if (url_tail == "Kinh doanh, Khởi nghiệp"):
        #     json_object_category["results"]["data"][a]["LevelCourseId"] = 1
        # elif (url_tail == "Kỹ năng mềm"):
        #     json_object_category["results"]["data"][a]["LevelCourseId"] = 2
        # elif (url_tail == "Ẩm Thực"):
        #     json_object_category["results"]["data"][a]["LevelCourseId"] = 3
#         # print(json_object_category["results"]["data"][a]["LevelCourseId"])
#         LevelCourseId = json_object_category["results"]["data"][a]["LevelCourseId"]
#         data = [LevelCourseId, name]
#         detail_data.append(data)
# #print(detail_data)
        # elif (url_tail == "Trình độ - B2"):
        #     json_object_category["results"]["data"][a]["LevelCourseId"] = 7
        # elif (url_tail == "Trình độ - C1"):
        #     json_object_category["results"]["data"][a]["LevelCourseId"] = 8
        #k = len(json_object_category["results"]["data"])
        k = len(json_object_category["results"]["data"][a]["videos"])
        print(k)
        for b in range(k):
            json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 0
            title = json_object_category["results"]["data"][a]["videos"][b]["title"]
            image = json_object_category["results"]["data"][a]["videos"][b]["image"]
            source = json_object_category["results"]["data"][a]["videos"][b]["source"]
            view_quantity = json_object_category["results"]["data"][a]["videos"][b]["view_quantity"]
            created_at = json_object_category["results"]["data"][a]["videos"][b]["created_at"]


            if (url_tail == "Ẩm Thực" and name == "Eat Clean chuẩn cho người Việt"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 22
            elif (url_tail == "Ẩm Thực" and name == "Tự tay làm 20 loại bánh quy Tết độc đáo"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 23
            elif (url_tail == "Ẩm Thực" and name == "Tự làm 18 loại bánh tại nhà không cần lò nướng"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 24
            elif (url_tail == "Ẩm Thực" and name == "20 công thức bánh thuần chay tốt cho sức khỏe"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 25

            elif (url_tail == "Kỹ năng mềm" and name == "Nghệ thuật làm chủ cảm xúc"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 26
            elif (url_tail == "Kỹ năng mềm" and name == "Bí quyết lập kế hoạch và triển khai công việc hiệu quả"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 27
            elif (url_tail == "Kỹ năng mềm" and name == "Đọc vị đối phương trong đàm phán - thương lượng"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 28

            elif (url_tail == "Kinh doanh, Khởi nghiệp" and name == "Khởi nghiệp nên bắt đầu từ đâu"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 29
            elif (url_tail == "Kinh doanh, Khởi nghiệp" and name == "Chinh phục 8 thách thức khi khởi nghiệp"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 30
            elif (url_tail == "Kinh doanh, Khởi nghiệp" and name == "Hậu khởi nghiệp - Tồn tại hay chỉ là hoang tưởng?"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 31

            elif (url_tail == "Kinh doanh, Khởi nghiệp" and name == "Khởi nghiệp và bán hàng trên Internet thành công"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 32
            elif (url_tail == "Kinh doanh, Khởi nghiệp" and name == "Khởi nghiệp thực chiến từ A-Z"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 33
            elif (url_tail == "Kinh doanh, Khởi nghiệp" and name == "CEO Internet"):
                json_object_category["results"]["data"][a]["videos"][b]["CoursesListId"] = 34

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
    values = (row[0], row[1], row[2], row[3],row[4])
    # insert the data into the database
    cursor.execute(insert_query, values)
# commit the inserts.
cnxn.commit()
# grab all the rows from the table
cursor.execute('SELECT * FROM VideoCourse')
for row in cursor:
    print(row)
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
