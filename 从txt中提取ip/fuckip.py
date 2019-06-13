#! /usr/bin/python
# coding:utf-8
'''
从test.txt 提取ip存放进ip.txt
'''
import re

li =[]

f = open('test.txt','r',encoding='UTF-8')
w = open('ip.txt','w')
for s in f.readlines():
	li.append(''.join(re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", s)))
	#利用list中的set()去重
	ip = list(set(li))
#保存结果	
w.write('\n'.join(ip))
print('\n'.join(ip))
	
	
