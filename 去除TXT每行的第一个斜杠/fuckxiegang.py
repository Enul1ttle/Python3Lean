f = open('1.txt','r',encoding='UTF-8')
w = open('2.txt','w',encoding='UTF-8')
for s in f.readlines():
	if((s[0:1]) == '/'):
		a = (s.strip("\n")[1:])
		w.write(a+"\n")
		print(a)
	else:
		w.write(s)
