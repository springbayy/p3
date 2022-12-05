import math
import random
import pylab
import numpy as np

def xex (x):
    return x * math.exp(-x)

def ex (x):
    if x<0:
        return 0
    else:
        return math.exp(-x)

def rand(delta):
    r=random.random()
    i=random.choice([-1,1])
    return i*r*delta

n0=200
n2=3
n3=100
stdlist=[0]*n2
deltlist=[0]*n2

for j in range (n2+1):

    delta=0.01*math.ceil((1000**(1/n2))**j)
    Nlist = [0] * (n3)
    diffList = [0] * n3
    it=20

    for k in range(n3):

        N=int((5000/n3)*(k+1))

        for m in range (it):
            list = [0] * (N+n0)
            list[0] = 1

            for i in range(1,N+n0):
                next=list[i-1]+rand(delta)
                r=random.random()

                if ex(next)/ex(list[i-1]) > r:
                    list[i]=next
                else:
                    list[i]=list[i-1]

            summa=0
            for i in range(n0, N+n0):
                summa+=list[i]
            avg=summa/(N)
            diffList[k]+=abs(avg-1)

        Nlist[k]=N
        diffList[k]=diffList[k]/it

    stringer1="Delta="+str(delta)
    pylab.plot(Nlist, diffList, label=stringer1)




title="n0="+str(n0)
pylab.xlabel("N")
pylab.ylabel("Difference to real value")
pylab.title(title)
pylab.legend()
pylab.show()
