
import os
choice = 0
filename = ''

def menu():
    global choice
    print('Menu\n 1.Open Microsoft Word\n 2.Open Notepad\n 3.Exit')
    choice = input('Select Menu : ')


def openword():
        filename = 'C:\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
        print('Wirting word %s' %filename)
        os.system(filename)

def opennotepad():
        filename = '%windir%\\system32\\notepad.exe'
        print('Memorandum writing %s' %filename)
        os.system(filename)

while True:
    menu()
    if choice == '1':
        openword()
    elif choice == '2':
        opennotepad()
    else:
        break 
