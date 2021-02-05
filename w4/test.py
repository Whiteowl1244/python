import os
goods = [0,0,0]
def show():
    print('สินค้ามีดังนี้\n \tแอปเปิ้ล 40บาท/กิโลกรัม\n \tกล้วย 50บาท/กิโลกรัม\n \tส้ม 60บาท/กิโลกรัม\n')

def sell():    
    sells= int(input('กดเลือกซื้อสินค้าตามหมายเลข'))
    if sells == 1 :
        sell_apple = int(input('กรุณากรอกกิโลกรัมของแอปเปิ้ลที่ท่านต้องการ'))
        goods[0] = sell_apple
    elif sells == 2 :
        sell_banana = int(input('กรุณากรอกกิโลกรัมของกล้วยที่ท่านต้องการ'))
        goods[1] = sell_banana
    elif sells == 3:
        sell_orage = int(input('กรุณากรอกกิโลกรัมของส้มที่ท่านต้องการ'))
        goods[2] = sell_orage
    print('ข้อมูลของท่านได้รับการยืนยันแล้ว')

def show_bill():
    print('รายการที่ท่านสั่งซื้อคือ')
    print('แอปเปิ้ล {} กิโลกรัม  ราคา {} บาท'.format(goods[0],goods[0]*40))
    print('กล้วย {} กิโลกรัม  ราคา {} บาท'.format(goods[1],goods[1]*50))
    print('ส้ม {} กิโลกรัม  ราคา {} บาท'.format(goods[2],goods[2]*60))
    print('สรุปราคาทั้งหมดคือ : {} บาท'.format((goods[0]*40)+(goods[1]*50)+(goods[2]*60)))

while True :
    a = int(input('ร้านขายผลไม้ออนไลน์\n กรุณาเลือกเมนู \n1.แสดงรายการสินค้า \n2.เลือกซื้อสินค้า \n3.แสดงรายการสินค้าที่เลือก \n4.ปิดโปรแกรม'))
    if a == 1:
        os.system('cls')
        show()
    elif a == 2:
        os.system('cls')
        show()
        sell()
    elif a == 3:
        os.system('cls')
        show_bill()
    elif a == 4:
        b=input('ท่านต้องการปิดโปรแกรมใช่หรือไม่ (y/n)')
        if b=='y' or b=='Y':
            break
        elif b=='n' or b=='N':
            continue




