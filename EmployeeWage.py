'''
@Author: Ariprasath
@Date: 2021-09-08 20:51:00
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-08 20:00:00
@Title : Check employee is present or absent
'''


import random

wage_per_hour=20
num=random.randint(0,2)
full_day_wage=8*wage_per_hour
half_day_work=4*wage_per_hour
switcher={
    0:
    "Employee is present; Total employee wage is 160",
    1:
    "Employee is present for half day; Total employee wage is 80",
    2:
    "Employee is absent; Total employee wage is 0"
}

print(switcher.get(num))