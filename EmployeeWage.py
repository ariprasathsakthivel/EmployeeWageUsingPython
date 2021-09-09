'''
@Author: Ariprasath
@Date: 2021-09-08 20:51:00
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-09
@Title : calculating wages for 20 working days or 100 hours
'''


import random

def emp_hours():
    '''
    Description:
        calculates the total employee working hours untill an employee working days of the month reaches 20 or total working hours of the month reaches 100 hours.
    parameter:
        None
    Return:
        working_hours(int): Total working hours in a month
    '''
    day=0
    working_hours=0
    while day<20 and working_hours<=100:
        num=random.randint(0,2)
        if num==0:
            working_hours=working_hours+8
        elif num==1:
            working_hours=working_hours+4
        day+=1
    return working_hours

if __name__=="__main__":
    wage_per_hour=20
    total_emp_wage=emp_hours()*wage_per_hour
    print(f"Total employee wage is {total_emp_wage}")