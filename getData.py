import numpy as np

x=3
t=50
print np.random.rand()
tt=[]

for i in range(t):
    line="\t".join([`np.random.rand()`,`np.random.rand()*30`,`np.random.rand()*100`])+"\n"
    print line
    tt.append(line)

a=open("123.txt",'w')
a.writelines(tt)
