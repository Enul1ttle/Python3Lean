d = {}
for line in open('a.txt',encoding='gbk', errors='ignore'):
    d[line] = d.get(line, 0) + 1 
fd = open('b.txt', 'w')
for k, v in d.items():
    if v > 3: #重复超三次保存
        fd.write(k)
fd.close()