import os 
Dictionaly = {}
i=0
def add():
    word = input('Add word : ')
    types = input('Type of the word : ')
    mean = input('Mean of the word : ')
    Dictionaly[word] = '{0:<15}{1:<15}'.format(types,mean)
    print('Add word completed!!')
def show():
    print('\n\t All Word\n{0: <11}{1: <8}{2}'.format('Word','Type','Mean'))
    for key in Dictionaly:
        print('{}{:<3}{}'.format(key,'',Dictionaly[key]))
    
def delete():
    delet = input('Delete Word : ')
    x = input('Do you want to delete '+delet+' ? (y/n) :')
    if x == 'y' or x == 'Y':
        Dictionaly.pop(delet)
        print('Delete',delet,'completed')
    elif x == 'n' or x == 'N':
        print(' ')
while True:
    print('\t พจนานุกรมออนไลน์ \n \t1.addword\n \t2.showword\n \t3.deletword\n \t4.exit')
    choice = int(input('Input Choice : '))
    if choice == 1:
        add()
        i+=1
    elif choice == 2:
        show()
    elif choice == 3:
        delete()
        i-=1
    elif choice == 4:
        exits = input('Do you want to close the program?')
        if exits == 'y' or 'Y':
            break
        elif exits == 'n' or 'N':
            continue
