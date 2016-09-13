# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 20:17:34 2016

@author: evanshapiro
"""



def bisectnewton(a,b,tolbis,tolnew):
    from secfun import secret_func
    import numpy as np
    myfunction = secret_func()
    tolerance = float(1)
#while count < 25:
    count = 1
    fa = myfunction.eval(a)
    while tolerance > tolbis:
        c = (a+b)/2
        f = myfunction.eval(c)
        if f == 0:
            ans = c
            print(ans)
        
        if np.sign(f) == np.sign(fa):
            a = c
            fa = f
        else:
            b = c
        c = (a+b)/2
        tolerance = abs(f)
    count = count+1
    return c
    return tolerance
    while tolerance > tolnew:        
        a = myfunction.eval(c)
        b = myfunction.deriv(c)
        c = c - a/b 
        tolerance = abs(a)
    count = count+1
    return a
bisectnewton(-100,100,10**-3,10**-5)
print("The root is:")
    print(c)
    print("Secret function evaluated at the root is:")
    print(a)
