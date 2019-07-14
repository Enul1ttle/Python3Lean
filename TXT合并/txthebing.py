# -*- coding:utf-8*-
import sys
import imp
imp.reload(sys)


import os
import os.path
import time
time1=time.time()



##########################合并同一个文件夹下多个txt################
def MergeTxt(filepath,outfile):
    k = open(filepath+outfile, 'a+')
    for parent, dirnames, filenames in os.walk(filepath):
        for filepath in filenames:
            txtPath = os.path.join(parent, filepath)  # txtpath就是所有文件夹的路径
            f = open(txtPath,encoding='gbk', errors='ignore')
            ##########换行写入##################
            k.write(f.read()+"\n")

    k.close()



if __name__ == '__main__':
    filepath="C:\\Users\\Administrator\\Desktop\\dit"
    outfile="result.txt"
    MergeTxt(filepath,outfile)
    time2 = time.time()
    print (str(time2 - time1) + 's')
