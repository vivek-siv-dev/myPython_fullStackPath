#==================================================================================================================
#problom:

                                # CREATE A SIMPLE CALCULATOR WITH function
                                # NB: saprate functions for each operators
                                #   : the calculator should work in a single line input 
                                #   : eg: 34+55
                                #       : 89


#==================================================================================================================
#solution:

def add(n1,n2):
    return float(n1)+float(n2)

def substract(n1,n2):
    return float(n1)-float(n2)

def mul(n1,n2):
    return float(n1)*float(n2)

def div(n1,n2):
    return float(n1)/float(n2)

def mod(n1,n2):
    return float(n1)%float(n2)

st=input("YOU CAN SIMPLY ENTER OPERATION IN THE SAME LINE(LIKE 1+5,etc..):")
ops="+-*/%"
op=n1=n2=""
reach_op=False
one_optr=0

for ch in st:
    if ch ==" ":
        continue
    if ch not in ops :
        if not reach_op:
            n1+=ch
    if ch in ops:
        op+=ch
        reach_op=True
        one_optr+=1
    if ch not in ops and  reach_op:
        n2+=ch
if one_optr>1:
    print("SYNTAX ERROR.!!!!!")
else:
    if op == '+':
        print(add(n1,n2))
    elif op == '-':
        print(substract(n1,n2))
    elif op == '*':
        print(mul(n1,n2))
    elif op == '/':
        print(div(n1,n2))
    elif op == '%':
        print(mod(n1,n2))
    else:
        print("syntax error")
