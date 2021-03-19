import sqlite3
import os
def show():
   print('{0:<10}{1:<25}{2}'.format('ลำดับ','ชื่อ','นามสกุล'))
   with sqlite3.connect(r"D:\Sittipong_Python\example.db") as con:
        con.row_factory = sqlite3.Row
        show1="SELECT * FROM proInfo"
        for row in con.execute(show1):
            print('{0:<10}{1:<25}{2}'.format(row['id'],row['Fname'],row['Lname']))
def showInfo():
      print('\t\t******ดูข้อมูลนักเรียน******') 
      show()
      print('*'*45)
      choiceNum = input('\tกรอกลำดับที่ต้องการทราบข้อมูล: ') #ตัวบังคับโชว์
      while True:
            print('*'*45)
            print('\t\t******ดูข้อมูลนักเรียน******')
            print('\t\t1.ข้อมูลส่วนตัว\n\t\t2.สภาพครอบครัว\n\t\t3.ด้านเศรษฐกิจ\n\t\t4.การเดินทาง\n\t\t5.ความประพฤติ\n\t\tกลับสู่หน้าหลัก [x]')
            choiceInfo = input('กรุณาเลือกส่วนของข้อมูลที่ต้องการทราบ: ')
            print('*'*45)
            CHOICENUM = choiceNum
            if choiceInfo == '1':
                  print('\t***ข้อมูลส่วนตัว***')   
                  print('{0:<10}\t{1:13}\t{2:<15}\t{3:<7}\t{4:<15}\t{5:<15}\t{6:<10}\t{7:<7}\t{8:<7}\t{9:<7}\t{10:<7}\t{11:<7}\t{12:<13}\t{13:<13}\t{14:<13}\t{15}'
                  .format('ชื่อ','นามสกุล','วันเดือนปีเกิด','อายุ','โรคประจำตัว','กลุ่มเลือด','บ้านเลขที่','หมู่','บ้าน','ตำบล','อำเภอ','จังหวัด','ชื่อบิดา','นามสกุลบิดา','ชื่อมารดา','นามสกุลมารดา'))
                  conn = sqlite3.connect(r'D:\Sittipong_Python\example.db')
                  c = conn.cursor()
                  sql = "SELECT * FROM proInfo WHERE id =" + "\"{}\"".format(CHOICENUM)
                  c.execute(sql)
                  result = c.fetchall()
                  for row in result:
                        print('{0:<10}\t{1:<13}\t{2:<15}\t{3:<7}\t{4:<10}\t{5:<5}\t{6:<6}\t{7:<7}\t{8:<7}\t{9:<7}\t{10:<7}\t{11:<7}\t{12:<13}\t{13:<13}\t{14:<13}\t{15}'
                              .format(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16]))
                  c.close()
            elif choiceInfo == '2':
                  print('\t***สภาพครอบครัว***')
                  print('{0:<30}{1:<30}{2:<20}{3:<20}{4:<20}{5}'.format('สถานะผู้ปกครอง','ปัจจุบันนักเรียนอาศัยอยู่กับ','จำนวนพี่น้อง','หญิง','ชาย','เป็นบุตรคนที่'))
                  conn = sqlite3.connect(r'D:\Sittipong_Python\example.db')
                  c = conn.cursor()
                  sql = "SELECT * FROM family WHERE id =" + "\"{}\"".format(CHOICENUM)
                  c.execute(sql)
                  result = c.fetchall()
                  for row in result:
                        print('{0:<30}\t{1:<30}\t{2:<20}\t{3:<20}\t{4:<20}\t{5}'.format(row[1],row[2],row[3],row[4],row[5],row[6]))
                  c.close()
            elif choiceInfo == '3':
                  print('\t***ด้านเศรษฐกิจ***')
                  print('{0:<30}{1:<30}{2:<30}{3:<30}{4}'.format('บิดาประกอบอาชีพ','รายได้ของบิดา','บิดาประกอบอาชีพ','รายได้ของบิดา','จำนวนเงินที่นักเรียนได้ต่อวัน'))
                  conn = sqlite3.connect(r'D:\Sittipong_Python\example.db')
                  c = conn.cursor()
                  sql = "SELECT * FROM economy WHERE id =" + "\"{}\"".format(CHOICENUM)
                  c.execute(sql)
                  result = c.fetchall()
                  for row in result:
                        print('{0:<30}\t{1:<30}\t{2:<30}\t{3:<30}\t{4}'.format(row[1],row[2],row[3],row[4],row[5]))
                  c.close()
            elif choiceInfo == '4':
                  print('\t***การเดินทาง***')
                  print('{0:<30}{1}'.format('นักเรียนเดินทางโดย','ระยะทาง'))
                  conn = sqlite3.connect(r'D:\Sittipong_Python\example.db')
                  c = conn.cursor()
                  sql = "SELECT * FROM goSchool WHERE id =" + "\"{}\"".format(CHOICENUM)
                  c.execute(sql)
                  result = c.fetchall()
                  for row in result:
                        print('{0:<30}\t{1}'.format(row[1],row[2]))
                  c.close()
            elif choiceInfo == '5':
                  print('\t***ความประพฤติ***')
                  print('{0:<30}{1:<30}{2:<30}{3}'.format('คุณธรรมและจริยธรรม','จิตอาสา','ความสนใจด้านการเรียน','ความเป็นผู้นำ'))
                  conn = sqlite3.connect(r'D:\Sittipong_Python\example.db')
                  c = conn.cursor()
                  sql = "SELECT * FROM conduct WHERE id =" + "\"{}\"".format(CHOICENUM)
                  c.execute(sql)
                  result = c.fetchall()
                  for row in result:
                        print('{0:<30}\t{1:<30}\t{2:<30}\t{3}'
                              .format(row[1],row[2],row[3],row[4]))
                  c.close()
            elif choiceInfo == 'x' or choiceInfo == 'X':
                  os.system('cls')
                  b=input('ท่านต้องการกลับสู่หน้าหลักใช่หรือไม่ (y/n)')
                  if b=='y' or b=='Y':
                        break
                  elif b=='n' or b=='N':
                        continue
def add():
      conn =sqlite3.connect(r'D:\Sittipong_Python\example.db')
      print('*'*45)
      print('!!!!กรุณากรอกให้เสร็จก่อนออกจากโปรแกรมหรือปิดโปรแกรม!!!!')
      print('\t\t******ข้อมูลส่วนตัว******')
      FNAME = input('กรุณากรอกชื่อ: ')
      LNAME = input('กรุณากรอกนามสกุล: ')
      BIRTHDAY = input('กรุณากรอกวันเดือนปีเกิด เช่น 01/12/2544: ')
      AGE = input('กรุณากรอกอายุ: ')
      SELFDIS = input('กรุณากรอกโรคประจำตัว: ')
      BLOODGROUP = input('กรุณากรอกกลุ่มเลือด: ')
      HOMENUM = input('กรุณากรอกบ้านเลขที่: ')
      HOMEMOO = input('กรุณากรอกหมู่ที่: ')
      HOME = input('กรุณากรอกชื่อหมู่บ้าน: ')
      TUMBON = input('กรุณากรอกตำบล: ')
      AUMPER = input('กรุณากรอกอำเภอ: ')
      JANGWAT = input('กรุณากรอกจังหวัด: ')
      FNAMEDAD = input('กรุณากรอกชื่อบิดา: ')
      LNAMEDAD = input('กรุณากรอกนามสกุลบิดา: ')
      FNAMEMOM = input('กรุณากรอกชื่อมารดา: ')
      LNAMEMOM = input('กรุณากรอกนามสกุลมารดา: ')
      print('\t******ระบบได้บันทึกข้อมูลของคุณแล้ว******\n\n')
      print('*'*45)
      print('\t\t******สภาพครอบครัว******')
      STATUSFAMILY = input('กรุณากรอกว่า บิดาเสียชีวิต/มารดารเสียชีวิต/บิดา-มารดาเสียชีวิต/บิดาแยกกันอยู่/บิดามารดาอยู่ด้วยกัน: ')
      STUDENTLIVEWITH = input('อาศัยอยู่กับ: ')
      HOWMUCH = input('จำนวนพี่น้อง: ')
      BOY = input('ชาย: ')
      GIRL = input('หญิง: ')
      NOSTUDENT = input('เป็นบุตรคนที่: ')
      print('\t******ระบบได้บันทึกข้อมูลของคุณแล้ว******\n\n')
      print('*'*45)
      print('\t\t******ด้านเศรษฐกิจ******')
      JOBDAD = input('กรุณากรอกอาชีพบิดา: ')
      MONEYDAD = input('กรุณากรอกเงินเดือนของบิดา: ')
      JOBMOM = input('กรุณากรอกอาชีพของมารดา: ')
      MONEYMOM = input('กรุณากรอกเงินเดือนของมารดา: ')   
      MONEYSTUDENT = input('กรุณากรอกจำนวนที่นักเรียนได้รับต่อวัน: ')
      print('******\tระบบได้บันทึกข้อมูลของคุณแล้ว******\n\n')
      print('*'*45)
      print('******\t\tการเดินทาง******')
      HOWTOGO = input('กรุณากรอกวิธีการเดินมาโรงเรียน(เดินเท้า/รถจักยานยนต์/รถจักรยาน/รถรับส่ง/อื่น...): ')
      DISTANCE = input('กรุณากรอกระยะทาง(กิโมเมตร): ')
      print('******\tระบบได้บันทึกข้อมูลของคุณแล้ว******\n\n')
      print('*'*45)
      print('******\t\tความประพฤติ******\n\tเกณฑ์การประเมิน\n\tมากที่สุด[5]\n\tมาก[4]n\tปานกลาง[3]\n\tน้อย[2]\n\tน้อยมาก[1]')
      DRARMA = input('คุณธรรมและจริยธรรม: ')
      PUBMIND = input('จิตอาสา: ')
      LOVELEARN = input('ความสนใจด้านการเรียนการเรียน: ')
      LEADER = input('ความเป็นผู้นำ: ')
      print('\t******ระบบได้บันทึกข้อมูลของคุณแล้ว******')
      print('*'*45)
      allproInfo =(FNAME,LNAME,BIRTHDAY,AGE,SELFDIS,BLOODGROUP,HOMENUM,HOMEMOO,HOME,TUMBON,AUMPER,JANGWAT,FNAMEDAD,LNAMEDAD,FNAMEMOM,LNAMEMOM)
      allfamily =(STATUSFAMILY,STUDENTLIVEWITH,HOWMUCH,BOY,GIRL,NOSTUDENT)
      alleconomy =(JOBDAD,MONEYDAD,JOBMOM,MONEYMOM,MONEYSTUDENT)
      allgoschool =(HOWTOGO,DISTANCE)
      allconduct =(DRARMA,PUBMIND,LOVELEARN,LEADER)
      c = conn.cursor()
      c.execute('''INSERT INTO proInfo VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',allproInfo)
      c.execute('''INSERT INTO family VALUES (NULL,?,?,?,?,?,?)''',allfamily)
      c.execute('''INSERT INTO economy VALUES (NULL,?,?,?,?,?)''',alleconomy)
      c.execute('''INSERT INTO goSchool VALUES (NULL,?,?)''',allgoschool)
      c.execute('''INSERT INTO conduct VALUES (NULL,?,?,?,?)''',allconduct)
      conn.commit()
      conn.close()
      os.system('cls')
def edid():
      print('\t\t******แก้ไขข้อมูลนักเรียน******') 
      show()
      print('*'*45)
      choiceNumEdid = input('\tกรอกลำดับที่ต้องการแก้ไขข้อมูล: ') #ตัวบังคับแก้ไข
      print('*'*45)
      while True:
            print('\t\t******แก้ไขข้อมูลนักเรียน******') 
            print('\t\t1.ข้อมูลส่วนตัว\n\t\t2.สภาพครอบครัว\n\t\t3.ด้านเศรษฐกิจ\n\t\t4.การเดินทาง\n\t\t5.ความประพฤติ\n\t\tกลับสู่หน้าหลัก [x]')
            choiceInfo = input('กรุณาเลือกส่วนของข้อมูลที่ต้องการแก้ไข: ')
            print('*'*45)
            if choiceInfo == '1':
                  os.system('cls')
                  conn =sqlite3.connect(r'D:\Sittipong_Python\example.db')
                  print('!!!!กรุณากรอกให้เสร็จก่อนออกจากโปรแกรมหรือปิดโปรแกรม!!!!')
                  print('*'*45)
                  print('\t\t******ข้อมูลส่วนตัว******')
                  FNAME = input('กรุณากรอกชื่อ: ')
                  LNAME = input('กรุณากรอกนามสกุล: ')
                  BIRTHDAY = input('กรุณากรอกวันเดือนปีเกิด เช่น 01/12/2544: ')
                  AGE = input('กรุณากรอกอายุ: ')
                  SELFDIS = input('กรุณากรอกโรคประจำตัว: ')
                  BLOODGROUP = input('กรุณากรอกกลุ่มเลือด: ')
                  HOMENUM = input('กรุณากรอกบ้านเลขที่: ')
                  HOMEMOO = input('กรุณากรอกหมู่ที่: ')
                  HOME = input('กรุณากรอกชื่อหมู่บ้าน: ')
                  TUMBON = input('กรุณากรอกตำบล: ')
                  AUMPER = input('กรุณากรอกอำเภอ: ')
                  JANGWAT = input('กรุณากรอกจังหวัด: ')
                  FNAMEDAD = input('กรุณากรอกชื่อบิดา: ')
                  LNAMEDAD = input('กรุณากรอกนามสกุลบิดา: ')
                  FNAMEMOM = input('กรุณากรอกชื่อมารดา: ')
                  LNAMEMOM = input('กรุณากรอกนามสกุลมารดา: ')
                  print('\t******ระบบได้บันทึกข้อมูลของคุณแล้ว******\n\n')
                  print('*'*45)
                  allproInfo =(FNAME,LNAME,BIRTHDAY,AGE,SELFDIS,BLOODGROUP,HOMENUM,HOMEMOO,HOME,TUMBON,AUMPER,JANGWAT,FNAMEDAD,LNAMEDAD,FNAMEMOM,LNAMEMOM,choiceNumEdid)
                  c = conn.cursor()
                  c.execute('''UPDATE proInfo SET Fname =?,Lname =?,birthday =?,age =?,selfDis =?,bloodGroup =?,homeNum =?, homeMoo =?,home =?,tumbon =?,aumpre =?,jangwat =?,
                        Fnamedad =?,Lnamedad =?,Fnamemom =?, lnamemom =? WHERE id = ?''',allproInfo)
                  conn.commit()
                  conn.close()
            elif choiceInfo == '2':
                  os.system('cls')
                  conn =sqlite3.connect(r'D:\Sittipong_Python\example.db')
                  print('!!!!กรุณากรอกให้เสร็จก่อนออกจากโปรแกรมหรือปิดโปรแกรม!!!!')
                  print('*'*45)
                  print('\t\t******สภาพครอบครัว******')
                  STATUSFAMILY = input('กรุณากรอกว่า บิดาเสียชีวิต/มารดารเสียชีวิต/บิดา-มารดาเสียชีวิต/บิดาแยกกันอยู่/บิดามารดาอยู่ด้วยกัน: ')
                  STUDENTLIVEWITH = input('อาศัยอยู่กับ: ')
                  HOWMUCH = input('จำนวนพี่น้อง: ')
                  BOY = input('ชาย: ')
                  GIRL = input('หญิง: ')
                  NOSTUDENT = input('เป็นบุตรคนที่: ')
                  print('\t******ระบบได้บันทึกข้อมูลของคุณแล้ว******\n\n')
                  print('*'*45)
                  allfamily =(STATUSFAMILY,STUDENTLIVEWITH,HOWMUCH,BOY,GIRL,NOSTUDENT,choiceNumEdid)
                  c = conn.cursor()
                  c.execute('''UPDATE family SET statusFamily =?,studentLiveWith =?,howMuch =?,boy =?,girl =?,noStudent =? WHERE id = ?''',allfamily)
                  conn.commit()
                  conn.close()
            elif choiceInfo == '3':
                  os.system('cls')
                  conn =sqlite3.connect(r'D:\Sittipong_Python\example.db')
                  print('*'*45)
                  print('!!!!กรุณากรอกให้เสร็จก่อนออกจากโปรแกรมหรือปิดโปรแกรม!!!!')
                  print('\t\t******ด้านเศรษฐกิจ******')
                  JOBDAD = input('กรุณากรอกอาชีพบิดา: ')
                  MONEYDAD = input('กรุณากรอกเงินเดือนของบิดา: ')
                  JOBMOM = input('กรุณากรอกอาชีพของมารดา: ')
                  MONEYMOM = input('กรุณากรอกเงินเดือนของมารดา: ')   
                  MONEYSTUDENT = input('กรุณากรอกจำนวนที่นักเรียนได้รับต่อวัน: ')
                  print('******\tระบบได้บันทึกข้อมูลของคุณแล้ว******\n\n')
                  print('*'*45)
                  alleconomy =(JOBDAD,MONEYDAD,JOBMOM,MONEYMOM,MONEYSTUDENT,choiceNumEdid)
                  c = conn.cursor()
                  c.execute('''UPDATE economy SET jobDad =?,moneyDad =?,jobMom =?,moneyMom =?,moneyStudent =? WHERE id = ?''',alleconomy)
                  conn.commit()
                  conn.close()
            elif choiceInfo == '4':
                  os.system('cls')
                  conn =sqlite3.connect(r'D:\Sittipong_Python\example.db')
                  print('!!!!กรุณากรอกให้เสร็จก่อนออกจากโปรแกรมหรือปิดโปรแกรม!!!!')
                  print('*'*45)
                  print('******\t\tการเดินทาง******')
                  HOWTOGO = input('กรุณากรอกวิธีการเดินมาโรงเรียน(เดินเท้า/รถจักยานยนต์/รถจักรยาน/รถรับส่ง/อื่น...): ')
                  DISTANCE = input('กรุณากรอกระยะทาง(กิโมเมตร): ')
                  print('******\tระบบได้บันทึกข้อมูลของคุณแล้ว******\n\n')
                  print('*'*45)
                  allgoschool =(HOWTOGO,DISTANCE,choiceNumEdid)
                  c = conn.cursor()
                  c.execute('''UPDATE goSchool SET howToGo =?,distance =? WHERE id = ?''',allgoschool)
                  conn.commit()
                  conn.close()
            elif choiceInfo == '5':
                  os.system('cls')
                  conn =sqlite3.connect(r'D:\Sittipong_Python\example.db')
                  print('!!!!กรุณากรอกให้เสร็จก่อนออกจากโปรแกรมหรือปิดโปรแกรม!!!!')
                  print('*'*45)
                  print('******\t\tความประพฤติ******\n\tเกณฑ์การประเมิน\n\tมากที่สุด[5]\n\tมาก[4]n\tปานกลาง[3]\n\tน้อย[2]\n\tน้อยมาก[1]')
                  DRARMA = input('คุณธรรมและจริยธรรม: ')
                  PUBMIND = input('จิตอาสา: ')
                  LOVELEARN = input('ความสนใจด้านการเรียนการเรียน: ')
                  LEADER = input('ความเป็นผู้นำ: ')
                  print('\t******ระบบได้บันทึกข้อมูลของคุณแล้ว******')
                  print('*'*45)
                  allconduct =(DRARMA,PUBMIND,LOVELEARN,LEADER,choiceNumEdid)
                  c = conn.cursor()
                  c.execute('''UPDATE conduct SET dharma =?,pubMind =?,lovelearn =?,leader =? WHERE id = ?''',allconduct)
                  conn.commit()
                  conn.close()
            elif choiceInfo == 'x' or choiceInfo == 'X':
                  os.system('cls')
                  b=input('ท่านต้องการกลับสู่หน้าหลักใช่หรือไม่ (y/n)')
                  if b=='y' or b=='Y':
                        break
                  elif b=='n' or b=='N':
                        continue
def delete():
      print('\t\t*****ลบข้อมูลนักเรียน******') 
      show()
      print('*'*45)
      print('\t\t\t ***หมายเหตุ \n\t\t\t\tส่วนของข้อมูลที่ลบจะหายไปทั้งหมด')
      choiceNumDelete = input('\tกรอกลำดับที่ต้องการลบข้อมูล: ')
      conn = sqlite3.connect(r'D:\Sittipong_Python\example.db')
      c = conn.cursor()
      c.execute('DELETE FROM proInfo WHERE id =?',choiceNumDelete)
      conn.commit()
      conn.close()
      conn = sqlite3.connect(r'D:\Sittipong_Python\example.db')
      c = conn.cursor()
      c.execute('DELETE FROM family WHERE id =?',choiceNumDelete)
      conn.commit()
      conn.close()
      conn = sqlite3.connect(r'D:\Sittipong_Python\example.db')
      c = conn.cursor()
      c.execute('DELETE FROM economy WHERE id =?',choiceNumDelete)
      conn.commit()
      conn.close()
      conn = sqlite3.connect(r'D:\Sittipong_Python\example.db')
      c = conn.cursor()
      c.execute('DELETE FROM goSchool WHERE id =?',choiceNumDelete)
      conn.commit()
      conn.close()
      conn = sqlite3.connect(r'D:\Sittipong_Python\example.db')
      c = conn.cursor()
      c.execute('DELETE FROM conduct WHERE id =?',choiceNumDelete)
      conn.commit()
      conn.close()
      print('*'*45)
      print('******ระบบได้ทำการลบข้อมูลแล้ว******')
      print('*'*45)
def reset():
      print('\t\t*****รีเซ็ตข้อมูลนักเรียนทั้งหมด******')
      show()
      print('*'*45)
      print('\t\t\t ***หมายเหตุ \n\t\t\t\tข้อมูลที่ลบจะหายไปทั้งหมด')
      print('*'*45)
      reset = input('******ท่านต้องการลบข้อมูลทั้งหมดหรือไม่[y/n]******')      
      if reset == 'y' or reset == 'Y':
            conn = sqlite3.connect(r'D:\Sittipong_Python\example.db')
            c = conn.cursor()
            c.execute('DELETE FROM proInfo')
            conn.commit()
            conn.close()
            conn = sqlite3.connect(r'D:\Sittipong_Python\example.db')
            c = conn.cursor()
            c.execute('DELETE FROM family')
            conn.commit()
            conn.close()
            conn = sqlite3.connect(r'D:\Sittipong_Python\example.db')
            c = conn.cursor()
            c.execute('DELETE FROM economy')
            conn.commit()
            conn.close()
            conn = sqlite3.connect(r'D:\Sittipong_Python\example.db')
            c = conn.cursor()
            c.execute('DELETE FROM goSchool')
            conn.commit()
            conn.close()
            conn = sqlite3.connect(r'D:\Sittipong_Python\example.db')
            c = conn.cursor()
            c.execute('DELETE FROM conduct')
            conn.commit()
            conn.close()
            print('******ระบบได้ทำการรีเซ็ตแล้ว******')          
while True:
      print('\t******ระบบข้อมูลช่วยเหลือนักเรียน******\n \t\tดูข้อมูลนักเรียน[a]\n \t\tเพิ่มข้อมูลนักเรียน[b]\n \t\tแก้ไขข้อมูลนักเรียน[c]\n \t\tลบข้อมูลนักเรียน[d]\n \t\tresetข้อมูลนักเรียนทั้งหมด[r]\n \t\tออกจากระบบ[x]')
      choice = input('กรุณาเลือกเมนู: ')
      if choice == 'a' or choice == 'A':
            os.system('cls')
            showInfo()
      elif choice == 'b' or choice == 'B':
            os.system('cls')
            add()
      elif choice == 'c' or choice == 'C':
            os.system('cls')
            edid()
      elif choice == 'd' or choice == 'D':
            os.system('cls')
            delete()
      elif choice == 'r' or choice == 'R':
            os.system('cls')
            reset()
      elif choice == 'x' or choice == 'X':
            os.system('cls')
            b=input('ท่านต้องการปิดโปรแกรมใช่หรือไม่ (y/n)')
            if b=='y' or b=='Y':
                  break
            elif b=='n' or b=='N':
                  continue