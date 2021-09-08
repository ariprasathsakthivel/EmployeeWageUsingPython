'''
@Author: Ariprasath
@Date: 2021-09-08 20:51:00
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-08 20:00:00
@Title : Check employee is present or absent
'''


import random

wage_per_hour=20
num=random.randint(0,1)
if num==0:
    print(f"Employee is present; Total employee wage is {8*wage_per_hour}")
else:
    print("Employee is absent; otal employee wage is 0")