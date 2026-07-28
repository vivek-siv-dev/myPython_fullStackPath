                                                                

#=======================================================================================================================================


#PROBLOM:               KEEP TAKING NUMBERS FROM THE USER. WHEN THE USER ENTERS 0, PRINT THE TOTAL SUM AND STOP.


#=======================================================================================================================================
#solution:

sum=0
while True:
    n=int(input("enter numbers:"))
    if n==0:
        print("sum of your enterd numbers is :",sum)
        break
    else:
        sum+=n
#output:


# # =====================================================     END     ==================================================



# '''Keep taking numbers from the user. Stop when a negative number is entered. Print how many positive numbers were entered.'''
# # # ====================================================================================================================
# count=0
# while True:
#     n=int(input("enter numbers:"))
#     if n>0:
#         count+=1
#     else:
#         print("the total +ve numbers are:",count)
#         break
# print("number of positive numbers you enterd:",count)

#  # =====================================================     END     ==================================================


# '''Keep taking numbers from the user until 0 is entered. Print the largest number entered.'''
# # =======================================================================================================
# large=0
# while True:
#     n=int(input("enter numbers:"))
#     if n!=0:
#         if large<n:
#             large=n
#     else:
#         print("largest from your enterd number is:",large)
#         break


# # ==================================================    END          ================================================================

# # '''Take numbers continuously. When 0 is entered, print the count of even and odd numbers.'''
# # # ========================================================================================================================
# o=0
# e=0
# while True:
#     n=int(input("enter numbers:"))
#     if n==0:
#         print("number of odd  numbers in this :",o)
#         print("number of even numbers in this :",e)
#         break
    
#     else:
#         if n%2==0:
#             e+=1
#         else:
#             o+=1

# # '''Take a number from the user and print its multiplication table from 1 to 10 using a while loop.'''
# # # =======================================================================================================
# n=int(input("enter the number:"))
# i=1
# while i<=10:
#     print(i ," x" ,n,"=",n*i)
#     i+=1

# '''Take a name from the user and print each character on a new line.'''
# #======================================================================

# name=input("enter your name:")
# for l in name:
#     print(l)
# # ===============================================     END       ========================================================


# '''Take a string and count how many vowels (a,e,i,o,u) are present.'''
# #=========================================================VVVVVVVV===========================================================
# s=input("enter the string:")
# v=0
# for letter in s:
#     if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
#         v+=1
# print(v," vowels in your string...!")
# ===============================================     END       ========================================================

# print string in reverse order.
# #=======================================
# s=input("enter string:")
# rev=""
# l=len(s)-1
# while l>=0:
#     rev+=s[l]
#     l-=1
# print(rev)

# ===============================================     END       ========================================================
# '''Take a string and count uppercase and lowercase letters separately.'''
# # =======================================================================================================
# s=input("enter a string:")
# lo=0
# u=0
# for letter in s:
#     if letter.islower():
#         lo+=1
#     elif letter.isupper():
#         u+=1
# print(u,":upper case letters in this string!")
# print(lo,":lower case letters in this string!")
# ===============================================     END       ========================================================
# #====================== '''Take a string and print characters present at index positions 0, 2, 4, ....'''===============
# st=input("enter string:")
# i=0
# while i<len(st):
#     print(st[i],"===>","[",i,"]")
#     i+=1
# ===============================================     END       ========================================================

# '''Given a list of numbers, print only the even numbers.'''
# # ===================================================================================================================

# nl=[34,55,34,21,22,89,86,53]
# for n in nl:
#     if n%2==0:
#         print(n)

# Take a number from the user and calculate its factorial.'''
# # # =======================================================================================================
# n=int(input("enter number:"))
# i=1
# f=1
# while i<=n:
#     f=f*i
#     i+=1
# print(f)
# # ==================================================   END   ============================================================

# # '''Given a list, find and print the largest element.'''
# # # =======================================================================================================
# ls=[23,67,45,21,34,75,89,108,4,3,2,5,99,5,4,43,51,63]
# large=0
# for i in ls:
#     if i>large:
#         large=i
# print("largest from this list is:",large)
# # ==================================================   END   ============================================================

# '''Given a list, count how many times a specific number appears.'''
# # ======================================================================================================= 
# count=0
# for i in lst:
#     if type(i)==int:
#         count+=1
# print("there are", count,"numbers in the list")
# # ==================================================   END   ============================================================

# '''Given a list containing a 0, print all elements before 0.'''
# # ==============================================================================================================

# lst=["v",8,"i",7,"v",6,"e",0,90,"k",47]
# for i in lst:
#     if i!=0:
#         print(i,end=" ")
#     else:
#         break
# # ==================================================   END   ============================================================
# '''Given a list containing multiple zeros, skip them using continue.'''
# # ======================================================================================================================

# lst=["codes","v",8,0,"i",7,0,"v",6,"e",0,90,"k","dream",0,47,"raj",16,916,"hari",0,55,"love",0]
# for iteam in lst:
#     if iteam!=0:
#         print(iteam,end="  ")
#     else:
#         continue
# # =====================================================   END   ============================================================

# '''Print Numbers from 1 to 20
# # Use range() and a for loop.'''
 
# for i in range(1,21):
#     print(i,end=" ")
# =======================================================   END   ============================================================

# '''Print Even Numbers from 1 to 50
# Use range().'''
#=============================================================================================================================
# for i in range(2,51,2):
#     print(i,end=" ")
# =======================================================   END   ============================================================


# '''Find Sum of Numbers from 1 to 100
# Use a for loop.'''
#=============================================================================================================================
# sum=0
# for i in range(1,101):
#     sum+=i
# print("sum of 1 to 100 is:",sum)
# # =======================================================   END   ============================================================




# '''Find Factorial of a Number
# # =======================================================================================================
        
# f=1
# n=int(input("enter a number:"))
# i=1
# while i<=n:
#     f*=i
#     i+=1
# print(f"{n}!={f}")
#----------------------------------------------------------------------------------------------------------------------






# # =======================================================================================================
                               #### coding challenge ~~~~~~~~~~~ LOOPS 
# # =======================================================================================================
#PRINT NUMBERS IN A LIST WHEN 5 OCCURS STOP THE ITERATION
# lst=[1,3,4,3,2,8,6,4,5,6,7,3]
# for i in lst:
#     if i!=5:
#         print(i,end=" ")
#     else:
#         print("stoping the loop here..! cause found 5")
        # break
#-------------------------------------------- *  END *  ---------------------------------------------------
# # =======================================================================================================
#PRINT NUMBERS 1 TO 20 SKIP THE MULTIPLE OF 3
# for i in range(1,21):
#     if i%3==0:
#         continue
#     else:
#         print(i,end=" ")
#-------------------------------------------- *  END *  ---------------------------------------------------
# =======================================================================================================
# TAKE A NUMBER WHETHER ITS PRIME
#1. n=int(input("enter the number:"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("prime")
# else:
#     print("not prime")    
#------------------------------------------
  #CAN USE THIS 2 LOGICS TO CHECK PRIME
#------------------------------------------
#2. n=int(input("enter number:"))
# if n<2:
#     print("NOT A PRIME NUMBER!")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime number")
#------------------------------------------------------------ END ----------------------------------------
#  prime number up to n using for loop
#==========================================================================================================
# n=int(input("enter the limits:"))
# count=0
# if n<2:
#     print("there is no prime number in this range.!")
# else:
#     for i in range(1,n+1):
#         count=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 count+=1
#         if count==2:
#             print(i)
#------------------------------------------------------------ END ----------------------------------------
# TAKE A STRING AND COUNT HOW MANY DIGITS ARE PRESENT 
#==========================================================================================================
# st=input("enter the string:")
# count=0
# for d in st:
#     if d.isdigit():
#         count+=1
# print(f"THIS STRIG HAS {count} DIGITS")
#------------------------------------------------------------ END ----------------------------------------
# take a string and count how many space belongs in it
#==========================================================================================================
# s=input("enter a sentance:")
# count=0
# for space in s:
#     if space==" ":
#         count+=1
# print(f"THIS ENTERD SENTANCE HAS {count} SPACES")
# #------------------------------------------------------------ END ----------------------------------------
# # TAKE A SENTANCCE AND PRINT IT WITHOUT ANY SPACE
# #==========================================================================================================
# s=input("enter the sentance:")
# without_sp=""
# for word in s:
#     if word!=" ":
#         without_sp+=word
# print(without_sp)
# #------------------------------------------------------------ END ----------------------------------------
# # TAKE A SENTANCCE AND PRINT ITS FIRST ND LAST LETTER
# #==========================================================================================================
# s=input("enter a sentance:")
# l=len(s)
# print(f"first letter==> {s[0]} \n last letter==> {s[l-1]}")

# #------------------------------------------------------------ END ---------------------------------------- ****
# # check whether a strong number or not  like 145 ==> 1!+4!+5!
# #========================================================================================================== ****
# n=input("enter a number:")
# sum=0
# for i in n:
#     fact=1
#     i=int(i)
#     for j in range(1,i+1):
#         fact*=j
#     sum+=fact
#     print(i,"!+",end=" ")
# print("=",sum)
# if sum==n:
#     print(n,"IS A STRONG NUMBER")
# else:
#     print(n,"IS NOT A STRONG NUMBER")

# #------------------------------------------------------------ END ---------------------------------------- 
# # PRINT UNIQUE ELEMNT IN THE LISt LST=[6,9,5,1,8,5,8,9,2,11,3,2,1,3,4,5,9,6,10,4,8,11,12,12,10]
# #==========================================================================================================
lst=[6,9,5,1,8,5,8,9,2,11,3,2,1,3,4,5,9,6,10,4,8,11,1543,12,12,10]
count=0
for i in range(0,len(lst)):
    count=0
    for j in lst:
        if lst[i]==j:
            count+=1
            if count>1:
                break
    if count==1:
        print(lst[i])
        break
else:
    print("NO UNIQUE ITEAM IN THIS LIST")
    
    
    

    
