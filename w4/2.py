import os
choice = 0
goodss = [0,0,0,0,0]
choose = 0

def menu():
    global choice
    print('+'*25)
    print('\tร้านไพ่ทาโร่ออนไลน์')
    print('+'*25)
    print('1.แสดงรายการสินค้า\n 2.หยิบสินค้ารายการ\n 3.แสดงรายจำนวนและราคาสินค้าที่หยิบ\n 4.นำสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม')
    print('+'*25)
    choice = input('กรุณาเลือกรายการ : ')
    screen_clear()

def menu1():
    print('*'*25)
    print('\t1.Rider-Waite Tarot 730B.\n \t2.Star Spinner Tarot 815B.\n \t3.Witches tarot 950B.\n \t4.Wizard tarot 960B.\n \t 5.The Llewellyn Tarot 960B.\n')
    print('*'*25)
        

def menu2():
    global choose
    print('*'*50)
    print('\t1.Rider-Waite Tarot \n \t2.Star Spinner Tarot \n \t3.Witches tarot \n \t4.Wizard tarot\n \t5.The Llewellyn Tarot')
    print('*'*50)
    choose = int(input('เลือกหยิบจากหมายเลข : '))
    if choose == 1:
        goodss[0] += 1
    elif choose == 2 :
        goodss[1] += 1
    elif choose == 3:
        goodss[2] += 1
    elif choose == 4 :
        goodss[3] += 1
    elif choose == 5 :
        goodss[4] += 1
    screen_clear()

def menu3():
   print('สินค้าของคุณมีดังนี้')
   print('สินค้า*****************จำนวน**************ราคา')
   print('1.Rider-Waite Tarot*******',goodss[0],'****',goodss[0]*730,'****')
   print('2.Star Spinner Tarot******',goodss[1],'****',goodss[1]*815,'****')
   print('3.Witches tarot***********',goodss[2],'****',goodss[2]*950,'****')
   print('4.Wizard tarot************',goodss[3],'****',goodss[3]*960,'****')
   print('5.The Llewellyn Taro******',goodss[4],'****',goodss[4]*960,'****')

def menu4():
    print('เลือกสินค้าที่จะนำออก')
    print('*'*50)
    print('\t1.Rider-Waite Tarot \n \t2.Star Spinner Tarot \n \t3.Witches tarot \n \t4.Wizard tarot\n \t5.The Llewellyn Tarot')
    print('*'*50)
    choose = int(input('เลือกหยิบจากหมายเลข : '))
    if choose == 1:
        goodss[0] -= 1
    elif choose == 2 :
        goodss[1] -= 1
    elif choose == 3:
        goodss[2] -= 1
    elif choose == 4 :
        goodss[3] -= 1
    elif choose == 5 :
        goodss[4] -= 1
    screen_clear()

def screen_clear():
    clearscreen = os.system('cls')

while True:
    menu()
    if choice == '1':
        screen_clear()
        menu1()
    elif choice == '2':
        screen_clear
        menu2()
    elif choice == '3':
        menu3()
    elif choice == '4':
        menu4()
    elif choice == '5':
        c = input('ต้องการใช้งานโปรแกรมต่อหรือไม่ y/n : ')
        if c.lower() == 'y':
            screen_clear
        elif c.lower() == 'n':
            screen_clear()
            break