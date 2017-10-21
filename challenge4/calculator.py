#!/usr/bin/env python3

import sys
import json
from multiprocessing import Process,Value,Queue,Pipe
queue=Queue()
class op(object):
	def get_list(sys_argv):
		args=sys_argv[1:]
		employee_list={}
		calc_list={}
		cfg=args[args.index('-c')+1]
		user=args[args.index('-d')+1]
		try:
			with open(cfg) as file:
				for line in file:
					lines=line.split('=')
					if len(lines)==2:
						calc_list[lines[0].strip()]=float(lines[1][:-1].strip())
					else:
						print("Lolita.cfg:File Format Error")
						sys.exit(-1)
		except FileNotFoundError:
			print("cfg file not found")
			sys.exit(-1)
		try:
			with open(user) as file:
				for line in file:
					lines=line.split(',')
					if len(lines)==2:
						employee_list[int(lines[0])]=float(lines[1][:-1])
					else:
						print("user.scv: File Format Error")
						sys.exit(-1)
		except FileNotFoundError:
			print("user file not Found")
			sys.exit(-1)
		#return employee_list,calc_list
		queue.put(employee_list)
		queue.put(calc_list)
	def calc_tax():#calc_tax(employee,calc)
		employee=queue.get()
		calc=queue.get()
		all_list=[]
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
				tax_Base=salary-base_insurance-base
				salary_list.append("{:.2f}".format(base_insurance))
			elif salary>=calc['JiShuH']:
				base_insurance=calc['JiShuH']*base_rate
				tax_Base=salary-base_insurance-base
				salary_list.append("{:.2f}".format(base_insurance))
			else:
				salary_list.append("{:.2f}".format(salary*base_rate))
				tax_Base=salary-salary*base_rate-base
			#add basic tax and after_salary
			#tax_Base=salary-salary*base_rate-base
			if tax_Base<0:#salary is smaller than 3500
				salary_list.append("{:.2f}".format(0.00))
				if salary<=calc['JiShuL']:
					salary_list.append("{:.2f}".format(salary-base_insurance))
				else:
					salary_list.append("{:.2f}".format(salary-salary*base_rate))
			elif tax_Base<=1500:
				tax_Paid=tax_Base*0.03
				salary_list.append("{:.2f}".format(tax_Paid))
				salary_list.append("{:.2f}".format(salary-salary*base_rate-tax_Paid))
			elif tax_Base<=4500:
				tax_Paid=tax_Base*0.1-105
				salary_list.append("{:.2f}".format(tax_Paid))
				salary_list.append("{:.2f}".format(salary-salary*base_rate-tax_Paid))
			elif tax_Base<=9000:
				tax_Paid=tax_Base*0.2-555
				salary_list.append("{:.2f}".format(tax_Paid))
				salary_list.append("{:.2f}".format(salary-salary*base_rate-tax_Paid))
			elif tax_Base<=35000:
				tax_Paid=tax_Base*0.25-1005
				salary_list.append("{:.2f}".format(tax_Paid))
				if salary >= calc['JiShuH']:
					salary_list.append("{:.2f}".format(salary-base_insurance-tax_Paid))
				else:
					salary_list.append("{:.2f}".format(salary*(1-base_rate)-tax_Paid))
			elif tax_Base<=55000:
				tax_Paid=tax_Base*0.3-2755
				salary_list.append("{:.2f}".format(tax_Paid))
				salary_list.append("{:.2f}".format(salary-base_insurance-tax_Paid))
			elif tax_Base<80000:
				tax_Paid=salary*0.35-5505
				salary_list.append("{:.2f}".format(tax_Paid))
				salary_list.append("{:.2f}".format(salary-base_insurance-tax_Paid))
			else:
				tax_Paid=tax_Base*0.45-13505
				salary_list.append("{:.2f}".format(tax_Paid))
				salary_list.append("{:.2f}".format(salary-base_insurance-tax_Paid))
			salary_list.insert(0,user)
			all_list.append(salary_list)
		#return all_list
		queue.put(all_list)
	def ppp_(sys_argv):#ppp_(sys_argv,hentai)
		hentai=queue.get()
		args=sys_argv[1:]
		filename=args[args.index('-o')+1]
		with open(filename,'w') as file:
			hentai.sort()
			for ii in hentai:
				length=1
				for i in ii:
					if length==len(ii):
						file.write(i+'\n')
					else:
						file.write(str(i)+',')
						length+=1
					
				
				
	
			

if __name__=='__main__':
	
	p=Process(target=op.get_list,args=(sys.argv,))
	p.start()
	pp=Process(target=op.calc_tax)
	pp.start()
	pp.join()
	ppp=Process(target=op.ppp_,args=(sys.argv,))
	ppp.start()

		
#	employee,calc=op.get_list(sys.argv)
#	result=op.calc_tax(employee,calc)
#	op.ppp(sys.argv,result)
#	with open('salary.csv','w') as file:
#		for i in result:
#			file.write(json.dumps(i))
		
	

