#https://github.com/vshnu1/lab11-VA-DD.git
# Partner 1: Vishnu Araveeti
# Partner 2: Damien Decker
import math 

def square_root(a):
    if a<0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a,b):
    return math.hypot(a,b)
def add(a,b): 
    return a+b 
def subtract(a,b): 
    return a-b 
def mul(a,b): 
    return a*b 
def div(a,b): 
    if a==0: 
        raise ZeroDivisionError 
    return b/a 
def logarithm(a,b): 
    if a<=0 or b<=0: 
        raise ValueError 
    return math.log(b,a) 
def exp(a,b): 
    return a**b