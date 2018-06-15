import random
card4 = (random.randint(1, 10), random.randint(1, 10),
         random.randint(1, 10), random.randint(1, 10))

         
print (card4)

cardstr=[]
for x in range(len(card4)):
    cardstr.append(str(card4[x]))

stepslist=[]    
##card4=(9, 7, 9, 10)
def c24(num):
    if num == (24,):
        return True
    if len(num)>=2:
        for x in range(len(num)):
            L=list(num)
            a= L.pop(x)
            tupx = tuple(L)
            for y in range(len(L)):
                L=list(tupx)               
                b=L.pop(y)
                tupy=tuple(L)
                NewNum = tuple(L)
                #####print (NewNum)
                for z in range(4):
                    NewNum = tuple(L)
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
                    NewNum=  NewNum+ (temp,)

                    if c24(NewNum)==True:                    
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
        newstr= a + stepslist[-1-x][2] + b 
    else:
        newstr= '('+a + stepslist[-1-x][2] + b +')'
    cardstr.append(newstr)
try:
   print (newstr)
except:
    print('cant find solve')
