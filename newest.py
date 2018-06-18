import random
import sys  
import itertools

card4 = tuple([random.randint(1, 10) for x in range(4)])   

print (card4)

cardstr=[]
count=0

for x in range(len(card4)):
    cardstr.append(str(card4[x]))

stepslist=[]    
##card4=(9, 7, 9, 10)
def c24(num):
    if num == (24,):
        return True
    if len(num)>=2:
        for n in list(itertools.combinations(range(len(num)),2)):
            L1=list(num)
            x=n[0]+1-1
            y=n[1]-1
            a= L1.pop(x)
            b=L1.pop(y)
            NewNum1=tuple(L1)
            for z in range(6):
                L2=list(NewNum1)
                if z==0:
                    temp=a+b
                    op='+'
                if z==1:
                    temp=a-b
                    op='-'
                if z==2:
                    temp=a*b
                    op='x'
                if z==3 and b!=0:
                    temp=a/b
                    op='/'
                if z==4:
                    temp=b-a
                    op='rev-'
                if z==5 and a!=0:
                    temp=b/a
                    op='rev/'
                L2.append(temp)
                NewNum2 =  tuple(L2)
                global count
                count=count +1
                #print ('%.2f %s %.2f  %.2f  %d' %(a,op,b,temp, count))
                sys.stdout.write('\r')
                sys.stdout.write('%d operations'%count)

                if c24(NewNum2)==True: 
                    if len(NewNum2)==1: print('\n')
                    print ('%.2f %s %.2f = %.2f' %(a, op, b, temp))
                    global stepslist
                    stepslist.append([x,y,op])
                    return True
    return False
    
                        
c24(card4)

for x in range(len(stepslist)):
    a=cardstr.pop(stepslist[-1-x][0])
    b=cardstr.pop(stepslist[-1-x][1])
    if x==len(stepslist)-1:
        if stepslist[-1-x][2]=='rev-':
            newstr=b+'-'+a
        elif stepslist[-1-x][2]=='rev/':
            newstr=b+'/'+a
        else:
            newstr= a + stepslist[-1-x][2] + b 
    else:
        if stepslist[-1-x][2]=='rev-':
            newstr='('+b+'-'+a+')'
        elif stepslist[-1-x][2]=='rev/':
            newstr='('+b+'/'+a+')'
        else:
            newstr= '('+a + stepslist[-1-x][2] + b +')'
    cardstr.append(newstr)
try:
   print (newstr)
except:
    print('\ncant find solve')
