'''
@Author: Ariprasath
@Date: 2021-09-08 20:51:00
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-08
@Title : calculating wages for 20 working days or 100 hours
'''


import random

wage_per_hour=20
day=0
total_emp_wage=0
working_hours=0
while day<20 and working_hours<=100:
    num=random.randint(0,2)
    if num==0:
        total_emp_wage=total_emp_wage+8*wage_per_hour
        working_hours=working_hours+8
    elif num==1:
        total_emp_wage=total_emp_wage+4*wage_per_hour
        working_hours=working_hours+4
    day+=1
print(f"Total employee wage is {total_emp_wage}")