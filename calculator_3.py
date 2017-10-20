#!/usr/bin/env python3

import sys
import json

class op(object):
	def get_list(sys_argv):
		args=sys_argv[1:]
		employee_list={}
		calc_list={}
		cfg=args[args.index('-c')+1]
		user=args[args.index('-d')+1]
		with open(cfg) as file:
			for line in file:
				lines=line.split('=')
				calc_list[lines[0]]=float(lines[1][:-1])
		with open(user) as file:
			for line in file:
				lines=line.split(',')
				employee_list[int(lines[0])]=float(lines[1][:-1])
		return employee_list,calc_list
	def calc_tax(employee,calc):
		enen=[]
		base=3500
		base_rate=0.165
		for user in employee.keys():
			salary_list=[]
			base_insurance=0
			#employee's income
			salary=employee[user]
			#add basic salary
			salary_list.append(int(salary))
			#add normal social insurance
			if salary<=calc['JiShuL']:
				base_insurance=calc['JiShuL']*base_rate
				salary_list.append(base_insurance)
			elif salary>=calc['JiShuH']:
				base_insurance=calc['JiShuH']*base*rate
				salary_list.append(base_insurance)
			else:
				salary_list.append(float(salary*base_rate))
			#add basic tax and after_salary
			tax_Base=salary-salary*base_rate-base
			if tax_Base<0:#salary is smaller than 3500
				salary_list.append(0.00)
				if salary<=calc['JiShuL']:
					salary_list.append(salary)
				else:
					salary_list.append(salary-salary*base_rate)
			elif tax_Base<=1500:
				tax_Paid=tax_Base*0.03
				salary_list.append(tax_Paid)
				salary_list.append(salary-salary*base_rate-tax_Paid)
			elif tax_Base<=4500:
				tax_Paid=tax_Base*0.1-105
				salary_list.append(tax_Paid)
				salary_list.append(salary-salary*base_rate-tax_Paid)       
			elif tax_Base<=9000:
				tax_Paid=tax_Base*0.2-555
				salary_list.append(tax_Paid)
				salary_list.append(salary-salary*base_rate-tax_Paid)
			elif tax_Base<=35000:
				tax_Paid=tax_Base*0.25-1005
				salary_list.append(tax_Paid)
				if salary >= calc['JiShuH']:
					salary_list.append(salary-base_insurence-tax_Paid)
				else:
					salary_list.append(salary*(1-base_rate)-tax_Paid)
			elif tax_Base<=55000:
				tax_Paid=tax_Base*0.3-2755
				salary_list.append(tax_Paid)
				salary_list.append(salary-base_insurance-tax_Paid)
			elif tax_Base<80000:
				tax_Paid=salary*0.35-5505
				salary_list.append(tax_Paid)
				salary_list.append(salary-base_insurance-tax_Paid)
			else:
				tax_Paid=tax_Base*0.45-13505
				salary_list.append(tax_Paid)
				salary_list.append(salary-base_insurance-tax_Paid)
			salary_list.insert(0,user)
			enen.append(salary_list)
		return enen
	def ppp(sys_argv,hentai):
		args=sys_argv[1:]
		filename=args[args.index('-o')+1]
		with open(filename,'w') as file:
			for ii in hentai:
				length=1
				for i in ii:
					if length==len(ii):
						file.write(str(i)+'\n')
					else:
						file.write(str(i)+',')
						length+=1
				
				
	
			

if __name__=='__main__':
	
	employee,calc=op.get_list(sys.argv)
	result=op.calc_tax(employee,calc)
	op.ppp(sys.argv,result)
#	with open('salary.csv','w') as file:
#		for i in result:
#			file.write(json.dumps(i))
		
	

