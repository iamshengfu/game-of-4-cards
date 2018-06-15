import random
card4 = (random.randint(1, 10), random.randint(1, 10),
         random.randint(1, 10), random.randint(1, 10))
print (card4)
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
                        op='X'
                    if z==3 and b!=0:
                        temp=a/b
                        op='/'
                    NewNum=  NewNum+ (temp,)

                    if c24(NewNum)==True:                    
                        print ('%.2f %s %.2f = %.2f' %(a, op, b, temp))
                        return True
    return False
    
                        
c24(card4)
