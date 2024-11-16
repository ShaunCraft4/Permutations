import random
import math

def FindALL(m):
    m=str(m).lower()
    fl={}
    for i in m:
        if m.count(i)>1 and i not in fl:
            fl[i]=m.count(i)
    mult=1
    for i in fl.values():
        mult*=math.factorial(int(i))
    l=[]
    while True:
        nl=list(m)
        s=""
        for i in range(len(m)):
            val=random.choice(nl)
            s+=val
            nl.remove(val)
        if s not in l:
            l.append(s)
        if len(l)==math.factorial(len(m))/mult:
            break
    return l

def FindFrom0(m):
    m=str(m).lower()
    ML=[]
    i=0
    while i<=len(m):
        l=[]
        c=0
        while True:
            s=""
            wl=list(m)
            for j in range(len(m)-i):
                val=random.choice(wl)
                s+=val
                wl.remove(val)
            if s not in l:
                l.append(s)
            else:
                c+=1
            if c>9999:
                break
        ML.extend(l)
        i+=1
    ML.remove("")
    return ML



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    