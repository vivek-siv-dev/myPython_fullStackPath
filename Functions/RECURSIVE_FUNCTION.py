#=======================================================================================================================================


            #                                            RECURSIVE FUNCTION :
                                             #FUNCTION CALL ITSELF IS CALLED RECURSIVE FUNCTION
                                             # base case: means when function call want to stop

#======================================================================================================================================
#----------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------#
#PROBLOM: FIND THE FACTORIAL OF A NUMBER USING RECURSIVE FUNCTION


# solution:
# def fact(num):
#     if num<l:
#         return num*fact(num+1)
#     else:    # this is the base part of recursive function
#         return num

# l=int(input("enter the limit:"))
# print(fact(1))




# 

#----------------------------------------------------------------------------------------------------------#
#                                                                                               * * * * * 
#----------------------------------------------------------------------------------------------------------#
#PROBLOM: FIbnocci series using function recursion

# def fib(number):
#     if number==0:
#         return 0
#     if number==1:
#         return 1
#     else:
#        return fib(number-1)+fib(number-2)
# n=int(input("enter the number:"))

# for i in range(n):
#     print(fib(i),end=" ")

#----------------------------------------------------------------------------------------------------------#
#          sum of n numbers 1 to n and n to 1                                                                                     * * * * * 
#----------------------------------------------------------------------------------------------------------#
# def Nsum(limit):
#     if limit>=1:
#         return limit+Nsum(limit-1)
#     else:
#         return 0
# n=int(input("enter the limit:"))
# print(Nsum(n))


def num(l):
    print(l)
    if l < 7:
        return(num(l+1))

print(num(1))








    