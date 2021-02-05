print('\tโปรแกรมคิดค่าระยะทาง')
print('+'*33)
print('\tกด 1 เลือกจ่ายเพิ่ม')
print('\tกด 2 เลือกเหมาจ่าย')
print('+'*33)
fx = int(input(print('เลือกเมนูเพื่อทำรายการ')))
if fx == 1 :
    km =int(input(print('กรุณาบอกระยะทาง')))
    if km <= 25 :
        print('25 บาท')
    else :
        print('80 บาท')
if fx == 2 :
    km =int(input(print('กรุณาบอกระยะทาง')))
    if km <= 25 :
        print('25 บาท')
    else :
        print('55 บาท')
        
