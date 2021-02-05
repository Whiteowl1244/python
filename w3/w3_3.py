food = []
i = 1
print('ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม')
while (i>0) :
    a = input(print('อาหารโปรดอันดับที่ ',i,' คือ'))
    food.append(a)
    i += 1
    if a == 'exit' :
        break
food.remove('exit')
print('อาหารสุดโปรดของคุณตามลำดับมีดังนี้')
for x in food :
    print(x)