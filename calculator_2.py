#!/usr/bin/env python3

import sys
#judge the parameters,if false,break down
if len(sys.argv)<2:
	print("Parameter Error")
	exit(1)
#tranlate the parameter to what I need
def handle_Parameters():
	id=[]
	salary=[]
	for i in range(1,len(sys.argv)):
		id_salary=sys.argv[i].split(":")
		id.append(int(id_salary[0]))
		salary.append(int(id_salary[1]))
	return id,salary
#calc each employee's salary
def op(id,salary):
	base=3500
	base_rate=0.165
	salary_After=[]
	for i in range(len(salary)):
		tax_Base=salary[i]-salary[i]*base_rate-base
		if tax_Base<=0:
			salary_After.append(salary[i]-salary[i]*base_rate)
		elif tax_Base<=1500:
			tax_Paid=tax_Base*0.03
			salary_After.append(salary[i]-salary[i]*base_rate-tax_Paid)
		elif tax_Base<=4500:
			tax_Paid=tax_base*0.1-105
			salary_After.append(salary[i]-salary[i]*base_rate-tax_Paid)
		elif tax_Base<=9000:
			tax_Paid=tax_Base*0.2-555
			salary_After.append(salary[i]-salary[i]*base_rate-tax_Paid)
		elif tax_Base<=35000:
			tax_Paid=tax_Base*0.25-1005
			salary_After.append(salary[i]-salary[i]*base_rate-tax_Paid)
		elif tax_base<=55000:
			tax_Paid=tax_base*0.3-2755
			salary_After.append(salary[i]-salary[i]*base_rate-tax_Paid)
		elif tax_Base<=80000:
			tax_Paid=tax_Base*0.35-5505
			salary_After.append(salary[i]-salary[i]*base_rate-tax_Paid)
		else:
			tax_Paid=tax_Base*0.45-13505
			salary_After.append(salary[i]-salary[i]*base_rate-tax_Paid)
	for i in range(len(salary)):
		print("{}:{:.2f}".format(id[i],salary_After[i]))


if __name__=='__main__':
	id=[]
	salary=[]
	id,salary=handle_Parameters()
	op(id,salary)
