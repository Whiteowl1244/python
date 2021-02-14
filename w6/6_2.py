import sqlite3
import os

def add():
    conn =sqlite3.connect(r'D:\Sittipong_Python\example.db')
    Fname = input('add first name: ')
    Lname = input('add last name: ')
    Email = input('add E-mail: ')
    Sex = input('add sex: ')
    Age = input('add age: ')
    Year = input('add year: ')
    params =(Fname,Lname,Email,Sex,Age,Year)
    c = conn.cursor()
    c.execute('''INSERT INTO student VALUES (NULL,?,?,?,?,?,?)''',params)
    conn.commit()
    conn.close()
    print('ระบบได้เพิ่มข้อมูลเรียบร้อยแล้ว')
def show():
    print('{0:<8}{1:<15}{2:<15}{3:<27}{4:<10}{5:<10}{6}\n'.format('No','firstName','lastName','Email','Sex','Age','Year'))
    with sqlite3.connect(r"D:\Sittipong_Python\example.db") as con:
        con.row_factory = sqlite3.Row
        show1="SELECT * FROM student "
        for row in con.execute(show1):
            print('{0:<8}{1:<15}{2:<15}{3:<27}{4:<10}{5:<10}{6}'.format(row['id'],row['fname'],row['lname'],row['email'],row['sex'],row['age'],row['year']))
def edid():
    show()
    conn =sqlite3.connect(r'D:\Sittipong_Python\example.db')
    row = input('เลือกแถวที่ต้องการแก้ไข: ')
    newFName = input('กรอกชื่อที่ต้องการแก้ไข: ')
    newLName = input('กรอกนามสกุลที่ต้องการแก้ไข: ')
    newEmail = input('กรอกอีเมลที่ต้องการแก้ไข: ')
    newSex = input('กรอกเพศที่ต้องการแก้ไข: ')
    newAge = input('กรอกอายุที่ต้องการแก้ไข: ')
    newYear = input('กรอกชั้นปีที่ต้องการแก้ไข: ')
    allNew = (newFName,newLName,newEmail,newSex,newAge,newYear,row)
    c = conn.cursor()
    c.execute('''UPDATE student SET fname = ?,lname = ?,email = ?,sex = ?,age = ?,year = ? WHERE id = ?''',allNew)
    conn.commit()
    conn.close()
    print('ระบบได้แก้ไขข้อมูลแล้ว')
def delete():
    show()
    deleteRow = input('กรุฯณากรอกแถวที่ต้องการลบ(No.): ')
    conn =sqlite3.connect(r'D:\Sittipong_Python\example.db')
    c = conn.cursor()
    c.execute('''DELETE FROM student WHERE id = ?''',deleteRow)
    conn.commit()
    conn.close()
    print('ระบบได้ลบข้อมูลแล้ว')
while True:
    print('\t++++++++++++++++++++++++++++++\n\t******ระบบลงทะเบียนนักเรียน******\n\t++++++++++++++++++++++++++++++\n\tเพิ่มนักเรียน กด [a]\n\tแสดงข้อมูลนักเรียน[s]\n\tแก้ไขข้อมูลนักเรียน[e]\n\tลบข้อมูลนักเรียน[d]\n\tออกจากโปรแกรม[x]')
    choice = input('กรุณาเลือกฟังก์ชั่น: ')
    if choice == 'a' or choice == 'A':
        os.system('cls')
        add()
    elif choice == 's' or choice == 'S':
        os.system('cls')
        show()
    elif choice == 'e' or choice == 'E':
        os.system('cls')
        edid()  
    elif choice == 'd' or choice == 'D':
        os.system('cls')
        delete()
    elif choice == 'x' or choice == 'X':
        os.system('cls')
        b=input('ท่านต้องการปิดโปรแกรมใช่หรือไม่ (y/n)')
        if b=='y' or b=='Y':
            break
        elif b=='n' or b=='N':
            continue