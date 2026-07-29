#=======================================================================================================================================


#PROBLOM:                            1.find factorial of a number using functon


#=======================================================================================================================================
#solution:
# def fact(num):
#     f=1
#     for i in range(1,num+1):
#         f*=i
#     return f
# n=int(input("enter number:"))
# print(f"{n}!={fact(n)}")

#output:
#   enter number:5
#                5!=120
#=======================================================================================================================================


#PROBLOM:                   # 2.swap 1st and last digit of a number using function


#=======================================================================================================================================
#solution:
# def swap(num):
#     num=str(num)
#     new=list(num)

#     first_digit=new.pop(0)
#     last_digit=new.pop(-1)
#     new.insert(0,last_digit)
#     new.append(first_digit)
#     rev=""
#     for i in new:
#         rev+=i
#     return(int(rev))
# n=input("enter the number:")
# print("THE ENTERD NUMBER IS                                :",n)
# print("THE NUMBER AFTER SWAPED THE FIRST AND LAST DIGIT IS :",swap(n))


#output:
# enter the number:6483
# THE ENTERD NUMBER IS                                : 6483
# THE NUMBER AFTER SWAPED THE FIRST AND LAST DIGIT IS : 3486
#=======================================================================================================================================


#PROBLOM:                      # 3.sum of digits of a number using function


#=======================================================================================================================================
#solution:
# def digi_sum(num):
#     num=str(num)
#     sum=0
#     for i in num:
#         sum+=int(i)
#     return(sum)                                     
# n=int(input("ENTER THE NUMBER:"))
# print("sum of digit of the number ",n," IS :",digi_sum(n))


#output: ENTER THE NUMBER:356
# sum of digit of the number  356  IS : 14
#=======================================================================================================================================


#PROBLOM:      4 .1!/1+ 2!/2+ 3!/3+ 4!/4+ 5!/5+ 6!/6+ 7!/7 =874.0...etc up to N


#==========================================================================================================================
#solution:

# def factorial_operation(num):
#     result=0
#     while num!=0:
#         fact=1
#         for i in range(1,num+1):
#             fact*=i
#         result+=fact/num
#         print(f"{num}!={fact}")
#         num-=1
#     return result

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f*=i
#     return f

# n=int(input("enter the number:"))
# out=""
# for i in range(1,n+1):
#     if i!=n:
#         out+=f"({fact(i)}/{i})+"
#     else:
#         out+=f"({fact(i)}/{i})"
# out+=str(f"={factorial_operation(n)}")
# print(out)

#output: 
#enter the number:7
# 7!=5040
# 6!=720
# 5!=120
# 4!=24
# 3!=6
# 2!=2
# 1!=1
# (1/1)+(2/2)+(6/3)+(24/4)+(120/5)+(720/6)+(5040/7)=874.0
#=======================================================================================================================================


#PROBLOM:                     5. rverse of number with using funtion

#======================================================================================================================================
#solution:

# def rev_number(num):
#     rev=0
#     while num !=0 :
#         last_digit=num%10
#         # if last_digit==0:

#         rev=rev*10+last_digit
#         num//=10
#     return rev

# n=int(input("Enter the number:"))
# print("Revers of ",n,"is:",rev_number(n))

#output:  Enter the number:528
#         Revers of  528 is: 825

#=======================================================================================================================================


#PROBLOM:                FACTORIAL OF PRIME NUMBERS UP TO N using function *****


#======================================================================================================================================
#solution:

def prime(limit):
    pr=[]
    for i in range(2,limit+1):
        its_prime=True
        for j in range(2,int(i*0.5)+1):
            if i%j==0:
                its_prime=False
        if its_prime:
            pr.append(i)
    return pr
def facto(prime):
        fact = 1
        for i in range(2,prime+1):
            fact*=i
        return fact

     
limit=int(input("enter the limit:"))  
prime_numbers=prime(limit)
print(f"There are {len(prime_numbers)} prime numbers up to  {limit} \nTHE PRIME NUMBER'S AND ITS FACTORIAL AS FOLLOWs \n\nPRIME_NUMBER\t\t FACTORIAL\n")
for num in prime_numbers:
    print(f"   {num}\t\t=>\t     {facto(num)}\n")


#=======================================================================================================================================


#PROBLOM:                SORT PRIME NUMBERS FROM A LIST using function *****


#======================================================================================================================================
#solution:

def prime_in_list(n):
    prime = True
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            prime=False
    if prime:
        return n
n=[3,4,6,5,2,3,4,5,6,17,44,33,2,4,55,4,22,46,68,53,88,81,83]
print("prime numbers in this list are:")
for i in n:
    if prime_in_list(i) is not None:
        print(prime_in_list(i),end=" ")

    

