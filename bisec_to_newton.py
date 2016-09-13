
'''This program is to calculate the root of a fucntion from (secfun). I origionally tried to use
newtons method, but it was unstable and would not converge. I have instead used the bisection method
to get an approximate root, so that i can feed that guess into Newton's Method in hopes that it will
diverge. '''


import numpy as np
from secfun import secret_func

myfunction = secret_func() #set the secret function to myfuction

def f(x):
	return myfunction.eval(x)    #define first fucntion as the origional function set in secret_func

def df(x):
	return myfunction.deriv(x) #define secret fucntions derivative as df(x)


def bisect_to_newton(a,b,tolb,toln): #define our root finding fucntion

    toll = float(1)
#while count < 25:
    Iter = 1
    fa = myfunction.eval(a)
    while toll > tolb: # start bysection method
        c = (a+b)/2
        f = myfunction.eval(c) # Evaluate to see if inital guess is correct
        if f == 0:
            ans = c
            print(ans) # print the succsessive values for c.

        if np.sign(f) == np.sign(fa): # check to see if there was a sign change
            a = c
            fa = f
        else:
            b = c
        c = (a+b)/2
        toll = abs(f)
        print(c)
    Iter = Iter+1
    return c
    return toll
    while toll > toln: # now lets use Newtons Method.
        a = f(c)
        b = df(c)
        c = c - a/b
        toll = abs(a) # set our previous tollerance to the new value of a.
        print(f(c))
    Iter = Iter+1 # incriment the counter.
    return a
Answer = bisect_to_newton(-100,100,10**-6,10**-5) #set the variable Answer to the soultion of our algorithm
print("The root is:",Answer) # show the answer.
