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
if num==0:
    print(f"Employee is present; Total employee wage is {8*wage_per_hour}")
elif num==1:
    print(f"Employee is present for half day; Total employee wage is {4*wage_per_hour}")
else:
    print("Employee is absent; Total employee wage is 0")