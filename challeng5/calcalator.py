#!/usr/bin/env python3

import sys,getopt,configparser
from multiprocessing import Process,Queue
import datetime  


class ppp(object):
	queue=Queue()
	def m1(sys_argv):	#parse the cfg and user file 
		args=sys_argv[1:]
		#read the commandline 
		try:
			list,args=getopt.getopt(args,'c:d:o:')
			command_list=dict(list)
#			print(list)
		except getopt.GetOptErroe as err:
			print(err)
			sys.exit(-1)
#		print()
#		print("*******************************************")
#		print()
		#read the cfg file
		config=configparser.ConfigParser()
		calc_list={}
		config.read(command_list['-c'])#paser Lolita.cfg
		for city in config.sections():
			calc={}
			for key in  config[city]:
				calc[key]=config[city][key]
			calc_list[city]=calc
#			print(calc)
#		for i,v in calc_list.items():
#			print(i,v)
		#read usr salary file users.csv
		user_list={}
		with open(command_list['-d']) as file:
			for line in file:
				lines=line.split(',')
				user_list[int(lines[0])]=int(lines[1][:-1])
#		print("::::::::::::::::::::::::::::")
#		print(user)
		return command_list,calc_list,user_list

		
	def m2(command,calc,user):
		print(command)
		print(calc)
		print(user)		
		








def main():
	command,calc,user=ppp.m1(sys.argv)
	ppp.m2(command,calc,user)


if __name__=='__main__':
	main()
	
