#1 read a list and if data above 50 then print the data
# list1=[]
# limit=int(input("enter the limint:"))
# for i in range(limit):
#     x=input("enter the iteam:")
#     list1.append(x)
# print(list1)
# for i in list1:
#     if int(i)>50:
#         print(i)
#------------------------------------------ END --------------------------------------------
# #2 sum of a number list
# lst=[2,3,4,5]
# sum=0
# for i in lst:
#     sum+=i
# print("sum=",sum)

#3 get a list and print 1st and last data
#-------------------------------------------------
# ls=[1,2,3,4,5]
# # print(ls[0],ls[-1])
#4 merge two list using buildin method and without building method 
# #without build in function
# lst1=[1,2,3,4,5]
# lst2=[1,2,3,4,5]
# lst1=lst1+lst2
# print(lst1)
# #with build in function EXTEND()
# lst1=[1,2,3,4,5]
# lst2=[1,2,3,4,5]
# lst1.extend(lst2)
# print(lst1)
#__________________________________________________________eND __________________________________________________
#5 read data for list from user and read data and check the enterd data is in the list
# lst=[]
# count=int(input("how many data you want to enter:"))
# for i in range(count):
#     x=int(input(f"enter the {i}st iteam:"))
#     lst.append(x)
#     print(lst)
# chk=int(input("enter what you want to check in this list:"))
# for i in lst:
#     if i == chk:
#         print(f"yes {chk} is in the list")
#         break
# else:
#     print("the data you enterd is not in the list")

#6 if list is [1,2,3,4,0,5,0,6,4,0,7] then print [1,2,3,4,5,6,4,7,0,0,0]
# lst=[1,2,3,4,0,5,0,6,4,0,7]
# nlst=[]
# zlst=[]
# for i  in lst:
#     if i!=0:
#         nlst.append(i)
#     else:
#         zlst.append(i)
# nlst.extend(zlst)
# print(nlst)
#------------------------------------------------------------END-------------------------------------------------
#7 if list is ["e,"t,"b,"a,"b,"e","b,"q"]

# l=["a","b","d","b","s","e","t","r","b","l"]
# for i in range(len(l)):
#     if l[i]=="b":
#         l[i]="k"
# print(l)


# 1.take user input if the user enter number then only store to the list.ignore other wife using build in function
#------------------------------------------------------------------------------------------------------------------------

# lst=[]
# spc=""
# for i in range(0,6):
#     data=input("enter the data:")
#     if data.isdigit():
#         lst.append(data)
# print(lst)
#_________________________________________________________END END END END END END END________________________________________

# 2.largest number in a list
#----------------------------------------------------------------------------------------------------------------------------
# lst=[34,5,3,2,44,811,55,64,6,4,33,52,333,433,678,3,333]
# large=0
# for i in lst:
#     if i>large:
#         large=i
# print(large)
#_________________________________________________________END END END END END END END________________________________________

# 3.store words in a list and ask that which position data to be reversed . then reverse the data (uesd build in functiond and not used build in function)
#----------------------------------------------------------------------------------------------------------------------------
#WITHOUT USING BUID IN FUNCTION
# lst=[]
# for i in range(0,5):
#     word=input("enter the word:")
#     lst.append(word)
# print(lst)
# which=input(" which do you you want to reverse in this list:")
# if which in lst:
#     ind=lst.index(which)
#     x=lst[ind]
#     rev=""
#     for i in range(len(x)-1,-1,-1):
#         rev+=x[i]
#     print(rev)
# else:
#     print("the word you enterd not in the list.")

#_______________________________________________________________END END END END END END END________________________________________
# 4.read a list from user and replAce all even numbers with 0

# lst=[]
# for i in range(0,5):
#     n=input("enter the numbers to the number list:")
#     if n.isdigit():
#         lst.append(n)
#     else:
#         print("please enter a number")
# print(lst)
# for i in range(0,len(lst)):
#     if int(lst[i])%2==0:
#         lst[i]="0"
# print(lst)

#_______________________________________________________________END END END END END END END___________________________________________
# # 5.read positive negative and 0 into 3 saprate list and count the iteam sapratly


# lstz=[]
# lstp=[]
# lstn=[]
# cp=0
# cn=0
# cz=0
# for i in range(0,12):
#     n=int(input("enter iteam:"))
#     if n==0:
#         lstz.append(n)
#     elif n>0:
#         lstp.append(n)
#     elif n<0:
#         lstn.append(n)
# print(f"list of zero       ===>{lstz} count={len(lstz)}")
# print(f"list of -ve numbers===>{lstn} count={len(lstn)}")
# print(f"list of +v enumbers===>{lstp} count={len(lstp)}")

#_______________________________________________________________END END END END END END END___________________________________________
# 6.sum of two list

# l1=[4,5,6,2,4,5,2]
# l2=[8,1,8,3,7]
# print("the 1st list========>:",l1)
# print("the 2nd list========>:",l2)
# sum=[]
# if len(l1)==len(l2):
#     for i in range(0,len(l1)):
#         sum=l1[i]+l2[i]
#         suml.append(sum)
# elif len(l1)<len(l2):
#     for i in range(0,len(l1)):
#         sum.append(l1[i]+l2[i])
#     for i in range(len(l1),len(l2)):
#         sum.append(l2[i])
# else:
#     for i in range(0,len(l2)):
#         sum.append(l1[i]+l2[i])
#     for i in range(len(l2),len(l1)):
#         sum.append(l1[i])
# print("the sum of two list=>:",sum)


#_______________________________________________________________END END END END END END END___________________________________________
# 7.prime number in a list
#______________________________________________________________________________________________________________________________________
#solution:

def isprime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False

lst=[1,2,3,4,5,6,7,8,9,10]
prime_numbers = [n for n in lst if isprime(n)]
print("Prime numbers in the list:", prime_numbers)


#_______________________________________________________________END END END END END END END___________________________________________
# 8.replace all -ve number with a positive of that numbers in the list

# lst=[7,8,-5,-3,6,-9]
# for i in range(0,len(lst)):
#     if lst[i]<0:
#         lst[i]=+(lst[i])
# print(lst)
# x=-3
# print(x)
#_______________________________________________________________END END END END END END END___________________________________________
#9.factorial list of a list 
#______________________________________________________________________________________________________________________________________
#solution:

# lst=[1,2,3,4,5]
# factorial_list = [1]  # Initialize the list with the factorial of 0!
# for n in lst:
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#     factorial_list.append(factorial)


# 
# 10.count the repetation
# 11.store string in to a list and count the words that is starting and ending with the same letter

#


