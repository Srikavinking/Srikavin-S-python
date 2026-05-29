'''a=open(r"D:\Srikavin local files\SK(kop).txt",'w')
print('file created')
a.write("Hi I am Srikavin")
a.flush()
a.close()
print('file writer')'''

a=open(r"D:\Srikavin local files\SK(kop).txt",'r')
print(a.readline())
print(a.readlines())
import os
os.remove(r"D:\Srikavin local files\SK(kop).txt")
