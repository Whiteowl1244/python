import os
class nisit :
    def __init__(self,name,id,sex,year,department,school,province):
        self.name = name
        self.id = id
        self.sex = sex
        self.year = year
        self.department = department
        self.province = province
        self.school = school

    def showInfo(self):
        print('*'*25,'ข้อมูล','*'*25)
        print('Name : ',self.name)
        print('Student ID : ',self.id)
        print('Sex : ',self.sex)
        print('Year : ',self.year)
        print('Department : ',self.department)
        print('School : ',self.school)
        print('Province : ',self.province)

print('*'*25,'กรุณากรอกข้อมูล','*'*25)
names = input('Name : ')
ids  = input('Student ID : ')
sexs = input('Sex : ')
years = input('Year : ')
departments = input('Department : ')
schools = input('School :')
provinces = input('Province : ')

a = nisit(names,ids,sexs,years,departments,provinces,schools)
a.showInfo()