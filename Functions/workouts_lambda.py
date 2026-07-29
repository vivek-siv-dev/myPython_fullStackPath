# : Lambda Function 
#=====================================================================================================
#problom:
#                Write a lambda function to add two numbers.

#=====================================================================================================
#solution:
# sum=lambda a,b : a + b
# print(sum(6,5))

#output:11
#=====================================================================================================
#problom:
#                Write a lambda function to find the square of a number.

#=====================================================================================================
#solution:

# num=int(input("enter number:"))
# sqr_of_number=lambda x: x**2
# print(f"sqr of {num} = {sqr_of_number(num)}")

#output: enter number:3
#        sqr of 3 = 9
#=====================================================================================================
#problom:
#                Write a lambda function to check if a number is even or odd.

#=====================================================================================================
#solution:

# n=int(input("enter the number:"))
# check=lambda n:'even' if n%2==0 else 'odd'
# print(check(n))
#=====================================================================================================
#problom:
#                Write a lambda function to return the last character of a string.

#=====================================================================================================
# solution:

# stri="python"
# lst_ch= lambda s:s[-1]
# print(lst_ch(stri))

# output: n
#=====================================================================================================
#problom:
#                 Write a lambda function to find the maximum of two numbers.

#=====================================================================================================
# solution:

# a=46
# b=321
# maxi= lambda x,y:x if x>y else y
# print(maxi(a,b))

# 321
#=====================================================================================================
#problom:
#                  Write a lambda function to multiply all elements in a list by 3..

#=====================================================================================================
# solution:

# lst=[4,5,6,3,4,3,3,4,5,6,7,5]
# new_lst=list(map(lambda i:i*3,lst))
# print(new_lst)

# output: [12, 15, 18, 9, 12, 9, 9, 12, 15, 18, 21, 15]
#=====================================================================================================
#problom:
#                Write a lambda function to check if a string starts with the letter ‘A’.

#=====================================================================================================
# solution:
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# st=input("enter the string:")
# x=st[0]
# start_with_A=lambda s: s if st[0]==x 'f ' else 
# print(start_with_A(st))



#=====================================================================================================
#problom:

#                Write a lambda function to sort a list of tuples based on the second element.
#                LIST=[(4,6),(3,6),(8,2),(1,0),(3,9)]

#=====================================================================================================
# solution:
# lst=[(4,1),(3,6),(8,2),(1,0),(3,9)]
# sorted_list = sorted(lst, key=lambda x: x[1])
# print(sorted_list)

# output:[(1, 0), (4, 1), (8, 2), (3, 6), (3, 9)]
#=====================================================================================================
#problom:

#                Write a lambda function to sort a list of tuples based on the first element.
#                LIST=[(4,6),(3,6),(8,2),(1,0),(3,9)]

#=====================================================================================================
# solution:

# lst=[(4,6),(3,6),(8,2),(1,0),(3,9)]
# sorted_lst=sorted(lst, key=lambda i : i[0])
# print(sorted_lst)

# output: [(1, 0), (3, 6), (3, 9), (4, 6), (8, 2)]
#==========================================================================================================================
#problom:

#                                Write a lambda function to calculate x^y (x to the power y).

#============================================================================================================================
#SOLUTION:

# x=int(input("enter the number:"))
# y=int(input("enter the power :"))

# power=lambda x,y :x**y
# print(f"{x}^{y}={power(x,y)}")

#output:
#         enter the number: 5
#         enter the power : 2

#         5^2=25
#=====================================================================================================
#problom:

#                        Write a lambda function to find the longer of two strings.

#=====================================================================================================
# solution:

# S1='PYTHON'
# S2='JAVASCRIPT'
# longer=lambda S1,S2 : S1 if len(S1)>len(S2) else S2

# print("longest word in this is : ",longer(S1,S2))

#output:longest word in this is :  JAVASCRIPT
#===========================================================================================================================
#problom:

#                        # Use filter() to get only even numbers tuple from a list of tuple.

#==========================================================================================================================
# solution: filter() function

# lst=lst=[(4,6),(3,6),(8,2),(1,0),(3,9)]
# even=list(filter(lambda i: i[0]%2==0 and i[1]%2==0,lst))
# print(even)

# output: [(4, 6), (8, 2)]
#=============================================================================================================================
#problom:

#                        # Use filter() to get either one of any iteam is an even number in tuple from a list of tuple.

#=============================================================================================================================
# solution: filter()-function-

# lst=lst=[(1,3),(3,6),(8,2),(1,0),(3,9)]
# even_puple=list(filter(lambda i: i[0]%2==0 or i[1]%2==0 and i[0]!=0 and i[1]!=0,lst))
# print(even_puple)

# output:  [(3, 6), (8, 2)]
#=============================================================================================================================
#problom:

#                        # Use filter() to select words longer than 4 characters from a list of strings.

#=============================================================================================================================
# solution: filter()-function-

# str_list=["java", 'python','php', 'cpp', 'javacript','css','devops']
# str_moreThan4_letters=list(filter(lambda word: len(word)>4,str_list))
# print(str_moreThan4_letters)

#output:['python', 'javacript', 'devops']
#=============================================================================================================================
#problom:

#                        # Use filter() to find numbers greater than 15 in a list.

#=============================================================================================================================
# solution: filter()-function-

# lst=[12, 15, 18, 9, 12, 9, 9, 12, 15, 22, 21, 15]
# list_of_more_than_12=list(filter(lambda i: i>15,lst))
# print(list_of_more_than_12)

#output: [18, 22, 21]
#=============================================================================================================================
#problom:

#                       Use filter() with a lambda to select strings that start with ‘p’ in a list

#=============================================================================================================================
# solution: filter()-function-

# lst=["java", 'python','php', 'cpp', 'javacript','css','devops']
# new_list=tuple(filter(lambda word: word[0]=='p',lst))
# print(new_list)

#output: ('python', 'php')
#=============================================================================================================================
#problom:

#                        Use filter() to get all prime numbers from a list.

#=============================================================================================================================
# solution: filter()-function-
# lst=[11, 5, 18, 9, 12, 7, 9, 12, 17, 22, 21, 15]

# def prime(num):
#     if num==0:
#         return False
#     elif num==1:
#         return False
#     else:
#         for i in range(2,int(num**0.5)+1):
#             if num%i==0:
#                 return False
#                 break
#         else:
#             return True

# prime_list=list(filter(lambda number: prime(number),lst))
# print(prime_list)

#output:[11, 5, 7, 17]
#zxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#                                                       M A P()
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


#=======================================================MAP()======================================================================
#problom:

#                              convert all strings in a list to uppercase.

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#solution: with using 'map()'  function

# lst=["java", 'python','php', 'cpp', 'javacript','css','devops']
# upper_case_list=list(map(lambda word: word.upper(),lst))

# print(upper_case_list)

#output: ['JAVA', 'PYTHON', 'PHP', 'CPP', 'JAVACRIPT', 'CSS', 'DEVOPS']

#=======================================================MAP()======================================================================
#problom:

#                              to find the square of each number in a list.
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#solution: with using 'map()'  function


# lst=[11, 5, 18, 9, 12, 7, 9, 12, 17, 22, 21, 15]
# sqr_list=list(map(lambda num: num**2,lst))
# print(sqr_list)

#output: [121, 25, 324, 81, 144, 49, 81, 144, 289, 484, 441, 225]
#=======================================================MAP()======================================================================
#problom:

#                              convert a list of temperatures from Celsius to Fahrenheit.
                                # equation: (c x 9/5)+32==> c x 1.8+32

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#solution: with using 'map()'  function

# celsius=[10,28,40,50,60,70,80,100,120,28,27,22,10]
# fahrenheit=list(map(lambda cel : (cel*1.8)+32,celsius))

# print(fahrenheit)

# output:[50.0, 82.4, 104.0, 122.0, 140.0, 158.0, 176.0, 212.0, 248.0, 82.4, 80.6, 71.6, 50.0]
#=======================================================MAP()======================================================================
#problom:

#                             to concatenate a word like “_done” to each string in a list.

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#solution: with using 'map()'  function

# lst=["java", 'python','php', 'cpp', 'javacript','css','devops']
# new_list=list(map(lambda word: word+"_done",lst))

# print(new_list)

#        Outout:['java_done', 'python_done', 'php_done', 'cpp_done', 'javacript_done', 'css_done', 'devops_done']
#=======================================================MAP()======================================================================
#problom:

#                             to add elements of two lists (element-wise addition).

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#solution: with using 'map()'  function

# 

#output: [22, 43, 58, 69, 72, 79, 89, 112, 135, 46, 42]

#===================# Reduce()====================================# Reduce()======================================================================
#=======================================# Reduce()======================================================================
#===================# Reduce()====================================# Reduce()======================================================================
#problom:
#                              Use reduce() to find the sum of all numbers in a list.

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#solution: with using # Reduce()  function

# from functools import reduce
# lst=[2,3,4,6,5,4,5,6,7]
# sum=reduce(lambda f,j : f+j, lst)
# print(sum)

#output: 42
#===================# Reduce()====================================# Reduce()======================================================================
#problom:
#                            Use reduce() to find the product of all elements in…

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#solution: with using # Reduce()  function

# lst=[2,1,4,6,1,4,1,6,1]
# from functools import reduce
# product=reduce(lambda x,y : x*y,lst)
# print(product)

#output: 1152
#=============================================================================================================================
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx E-N-D xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#=============================================================================================================================













