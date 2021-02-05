student = int(input('กรุณากรอกจำนวนนักเรียน :'))
print('*'*25)
total =[0,0,0,0,0,0]
score = ['90-100 :','80-89 :','70-79 :','60-69 : ','50-59 : ','0-49 :']
x = 1
while x <= student :
    x = x+1
    point = int(input('กรุณากรอกคะแนน : '))
    if point <= 100 and point >= 90 :
        total[0]+= 1
    elif point < 90 and point >= 80 :
        total[1]+= 1
    elif point < 80 and point >= 70 :
        total[2]+= 1
    elif point < 70 and point >= 60 :
        total[3]+= 1
    elif point < 60 and point >= 50 :
        total[4]+= 1
    elif point < 50 and point >= 0 :
        total[5]+= 1    
for x in range(0,6) :
    print(score[x],'*'*total[x]) 



'''
a=[]
while True:
    b = input('----ไพ่ทาโร่-----\n เพิ่ม [a]\n แสดง [s]\n ออกจากระบบ [x]\n')
    b = b.lower()
    if b=='a':
        c=input('ป้อนรายการลูกค้า(รหัส : ชื่อ : จังหวัด)')
        a.append(c)
        print('\n ******ข้อมูลได้เข้าสู่ระบบแล้ว******\n')
    elif b=='s' :
        print('{0:-<6}{0:-<10}{0:-<10}'.format(''))
        print('{0:-<8}{1:-<10}{2:10}'.format('รหัส','ชื่อ','จังหวัด'))
        print('{0:-<6}{0:-<10}{0:-<10}'.format(''))
        for d in a:
            e = d.split(':')
            print('{0[0]:<6} {0[1]:<10}({0[2]:<10})'.format(e))
            continue
    elif b== 'x':
        break
print('ทำคำสั่ง')

info = []
while (True) :
    print('+'*30)
    print('\tร้านไพ่ทาโร่')
    print('\tเพิ่ม [ 1 ]')
    print('\tแสดง [ 2 ]')
    print('\tออกจากระบบ [ 0 ]')
    print('+'*30)
    f = int(input(print('เลือกโปรแกรม')))
    if f == 1 : #ถ้า 1 เท่ากับ f 
               
        a = input(print('ป้อนรายการลูกค้า(รหัส : ชื่อ : จังหวัด)')) #ตัวแปลข้อมูลลูกค้า
    info.append(a)
    print('*'*6,'ข้อมูลได้เข้าสู่ระบบแล้ว','*'*6)
    if f == 2 :
        print('+'*30)
        print('\tรหัส---ชื่อ---จังหวัด')
        print('+'*30)
        #print(info)