#==================================================================================================================
#problom:

                                # CREATE A SIMPLE CALCULATOR WITH function
                                # NB: saprate functions for each operators


#==================================================================================================================
#solution:

n1=float(input(" 1st no:"))
op=input(" oprtr :")
n2=float(input(" 2nd no:"))

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

def mod(n1,n2):
    return n1%n2

if op=='+':
    print(f" {n1}+{n2}={add(n1,n2)}")
elif op == "-":
    print(f" {n1}-{n2}={sub(n1,n2)}")
elif op == "*":
    print(f" {n1}*{n2}={mul(n1,n2)}")
elif op == "/":
    print(f" {n1}/{n2}={div(n1,n2)}")
elif op == "%":
    print(f" {n1}%{n2}={mod(n1,n2)}")
else: 
    print("syntax error!")
    

    

    


