
#                                          FILTER FUNCTION
#                                          MAP    FUNCTION

#-------------------------------------------------------------------------------------------------------

# FILTERS ELEMENTS FROM AM ITEARABLE(LIKE LIST)
#BASED ON A GIVEN FUNCTION AND RETURN A FILTER OBJECT

# SYNTAX:
    #  numbers=[2,3,4,5,6,7,4,3,4,5,56,67,7,8,54,3,3,4,,5]
    #  even=filter(lambda x:x%2==0,numbers)

#````````````````````````````````````````````````````````````````````````````````````````````````````````
#                          take all even numbers from this list
#                                 [2,3,4,5,6,7,4,3,4,5,56,67,7,8,54,3,3,4,5]
# =======================================================================================================
# numbers=[2,3,4,5,6,7,4,3,4,5,56,67,7,8,54,3,3,4,5]
# even=list(filter(lambda x:x%2==0,numbers))
# print("even numbers from the list is :",even)

# output:[2, 4, 6, 4, 4, 56, 8, 54, 4]
#````````````````````````````````````````````````````````````````````````````````````````````````````````
#                          take all words form the list that have more than 5 letters
#                                 fruits=['mango', 'orange','apple','grapes]
# =======================================================================================================
#solution:

# fruits=['mango', 'orange','apple','grapes']
# fr=list(filter(lambda fruit: len(fruit)>5, fruits))
# print(fr)

#output:
#    ['orange', 'grapes']

#=========================================================================================================
# PROBLOM:
#  take all odd numbers from the lis lst=[3,4,5,6,7,5,4,4,5,8,6,4,3,3,3,3,4,5,5,6,6,11]

#========================================================================================================
#solution:
# lst=[3,4,5,6,7,5,4,4,5,8,6,4,3,3,3,3,4,5,5,6,6,11]
# odd=list(filter(lambda number:number%2==1,lst))
# print(odd)

#output: [3, 5, 7, 5, 5, 3, 3, 3, 3, 5, 5, 11]
#==================================================================================================
#problom:

# use hiegher order function to find the interest for different interst rates
# equation:p*n*r
# interest_rate=[0.05, 0.1, 0.15, 0.2]

#===================================================================================================
#soluton

# interest_rate=[0.05, 0.1, 0.15, 0.2]
# amount=10000
# piriod=5
# interest=list(map(lambda i : amount*piriod*i,interest_rate))
# print(interest)

#output:  [2500.0, 5000.0, 7500.0, 10000.0]
#=========================================================================================================
# PROBLOM:

#  take all numbers that fully divisible by 5 in this list and stored in a tuple then print it.
#  lst =[30,40,5,65,7,51,41,6,4,3,4,51,51,60,6,11]

#========================================================================================================
#solution:
# lst =[30,40,5,65,7,51,41,6,4,3,4,51,51,60,6,11]
# fact5=tuple(filter(lambda num : num%5==0,lst))
# print(fact5)

#output: (30, 40, 5, 65, 60)


#   *   *   *   *    map() functiom * * * * * * * * *
#   map() applies a function to each element of an iterable,   
#   returning a lazy iterator that generates results as needed. 


#=====================================================================================================================
#problom:
#take numbers from a list and strore its factorial  in an other list and prit it

#list=[3, 5, 7, 5, 5, 3, 3, 3, 3, 5, 5, 11]

#=====================================================================================================================
# solution:    with map() function

# list1=[3, 5, 7, 5, 5, 3, 3, 3, 3, 5, 5, 11]
# def facto(num):
#     fact=1
#     for i in range(2,num+1):
#         fact*=i
#     return fact
# fact_list=list(map(lambda num:facto(num),list1))
# print(fact_list)

#output:[6, 120, 5040, 120, 120, 6, 6, 6, 6, 120, 120, 39916800]
#=====================================================================================================================
#problom:
#take only prime numbers from a list and store it as a list.

#list=[3, 50, 7, 58, 51, 34, 38, 37, 43, 25, 5, 51, 11]

#=====================================================================================================================
#solution:

# lst=[3, 50, 7, 58, 51, 0, 1, 34, 38, 37, 43, 25, 5, 51, 11,61]
# def confirm_prime(num):
#     if num==0 or num==1:
#         return
#     prime=True
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             prime=False
#     if prime:
#         return num
# prime_list=list(filter(lambda prime : confirm_prime(prime),lst))
# print(prime_list)

# output:[3, 7, 37, 43, 5, 11, 61]
#*****************************************************************************************************
#problonm:
#  take only prime number from list and print it using filter()

#*****************************************************************************************************
#solution:
# lst=[3, 50, 7, 58, 51, 0, 1,2, 34, 38, 37, 43, 25, 5, 51, 11,61]
# def confirm_prime(num):
#     if num==0 or num==1:
#         return False
#     prime=True
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return False
#             break
#     else:
#         return True
# pri_list=list(filter(confirm_prime,lst))
# print(pri_list)

#NB: 
# SEE I CALLED THE FUNCTION NAME LIKE A VARIABLE. AND ALSO I NEVER GIVE PARAMEETER TOO
# BECAUSE THE HIGHER ORDER FUNCTION TEAT FUNCTION AS A VARIABLE
# SO WE CAN JUST CALL IT LIKE SAME AS VARIABLE
#*****************************************************************************************************
#PROBLOM:
#           take even number and also divisible by 5 from a list and print it

#*****************************************************************************************************
#SOLUTION:
# lst=[3, 50, 7, 55, 51, 0, 10, 20, 34, 38, 37, 43, 25, 5, 51, 15,6]
# def check(num):
#     if num%2==0 and num%5==0 and num!=0:
#         return True
#     else:
#         return False
# filterd_lst=list(filter(check,lst))
# print(filterd_lst)

#output: [50, 10, 20]








 
















