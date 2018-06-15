#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
card4 = (random.randint(1, 10), random.randint(1, 10),
         random.randint(1, 10), random.randint(1, 10))
print (card4)
print ('\n') 

def c24(n, ans, num):
    if n == 0 and ans == 24:
        print ('true')
        return True
    if n==4:
        for x in range(4): 
            L=list(num)
            a = L.pop(x)
            NewNum = tuple(L)
            if c24(n-1, a, NewNum):
                print (num[x])
                return True
    L=list(num)
    if n<4:
        for x in range(len(L)):
            L=list(num)
            a = L.pop(x)
            NewNum = tuple(L)
            if c24(n - 1, ans + a, NewNum):
                print ('+ %d'%(a))
                return True
            if c24(n - 1, ans - a, NewNum):
                print ('- %d'%(a))
                return True
            if c24(n - 1, a - ans, NewNum):
                print (' %d -'%(a))
                return True
            if c24(n - 1, ans * a, NewNum):
                print ('X %d'%(a))
                return True
            if c24(n - 1, ans / a, NewNum):
                print ('/ %d'%(a))
                return True
            if ans != 0:
                if c24(n - 1, a / ans,NewNum):
                    print (' %d /'%(a))
                    return True  
    return False
c24(len(card4), 0, card4)

