#*****************************************************************************************************
#problonm:
#  take only prime number from list and print it using filter()

#*****************************************************************************************************
#solution:
lst=[3, 50, 7, 58, 51, 0, 1,2, 34, 38, 37, 43, 25, 5, 51, 11,61]
def confirm_prime(num):
    if num==0 or num==1:
        return False
    prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
            break
    else:
        return True
pri_list=list(filter(confirm_prime,lst))
print(pri_list)

#NB: 
# SEE I CALLED THE FUNCTION NAME LIKE A VARIABLE. AND ALSO I NEVER GIVE PARAMEETER TOO
# BECAUSE THE HIGHER ORDER FUNCTION TEAT FUNCTION AS A VARIABLE
# SO WE CAN JUST CALL IT LIKE SAME AS VARIABLE
#*************************************************************************************************
lst=[3, 50, 7, 58, 51,60,70, 0, 1,2, 34, 38, 37, 43, 25, 5, 51, 11,61]

def check(num):
    if num%5==0 and num%2==0 and num!=0:
        return True
    else:
        False

def prime(num):
    if num ==0 or num==1:
        return False
    for i in range(2,int(num*0.5)):
        if num%i==0:
            return False
    return True

prime_in_list=list(filter(prime,lst))
print(prime_in_list)





    