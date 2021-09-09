'''
@Author: Ariprasath
@Date: 2021-09-08 20:51:00
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-09
@Title : calculating wages for 20 working days or 100 hours and also storing the daily wage of  an employee
'''


import random

def emp_hour_daily_wage(wage_per_hour):
    '''
    Description:
        calculates the total employee working hours untill an employee working days of the month reaches 20 or total working hours of the month reaches 100 hours.
    parameter:
        wage_per_hour(int): Wage per hour
    Return:
        A Tuple that contains the following values
        working_hours(int): Total working hours in a month
        daily_wage(list): contains daily wage of an employee
    '''
    day=0
    working_hours=0
    daily_wage=list()
    while day<20 and working_hours<=100:
        num=random.randint(0,2)
        if num==0:
            working_hours=working_hours+8
            daily_wage.append(8*wage_per_hour)
        elif num==1:
            working_hours=working_hours+4
            daily_wage.append(8*wage_per_hour)
        else:
            daily_wage.append(0)
        day+=1
    return working_hours,daily_wage

if __name__=="__main__":
    wage_per_hour=20
    total_emp_wage=emp_hour_daily_wage(wage_per_hour)[0]*wage_per_hour
    print(f"Total employee wage is {total_emp_wage}")
    print(f"Daily employee wage\n {emp_hour_daily_wage(wage_per_hour)[1]}")