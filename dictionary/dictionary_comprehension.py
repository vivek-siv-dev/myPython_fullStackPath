#variable={key_expresion:value_expresion for iteam in itearabe if condition}


#======================================================================================================================================

#                                   # create a dictioinary number is the key and its squre  is the value

#======================================================================================================================================
# #solution 1: treditional method
# numbers=[1,2,3,4,5,6,7,8,9,10]
# sqr={}
# for i in numbers:
#     sqr[i]=i*i
# print(sqr)

#======================================================================================================================================
#solution 2: used dictionary_comperhenson method
# numbers=[1,2,3,4,5,6,7,8,9,10]
# sqr={}
# sqr={i:i**2 for i in numbers}
# print(sqr)


#Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
#======================================================================================================================================

                    # swap key and value in a dic..., dictionary is  dic={'a':1,'b':2,'c':3} to dic={1:'a',2:'b',3:'c'}

#======================================================================================================================================
#solution:

# dic={'a':1,'b':2,'c':3,'d':4}
# invertDic={j:i for i,j in dic.items()}
# print(invertDic)


# output:{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
#======================================================================================================================================

#PROBLEM:                create a dic of charectors and there ASCII value from a given strung
#======================================================================================================================================
#solution:

# st=input("enter the string:")
# dic={}
# for i in st:
#     if i.isspace():
#         continue
#     dic[i]=ord(i)
# print(dic)


# enter the string:I LOVE YOU
# {'I': 73, 'L': 76, 'O': 79, 'V': 86, 'E': 69, 'Y': 89, 'U': 85}
#======================================================================================================================================

                #Read student name and mark in to a dic and find the count of student who get more mark than 50ung

#======================================================================================================================================
#solution:
# dic={}
# count=0
# l=int(input("how many student's marks have to enter:"))
# for i in range(0,l):
#     name=input("enter name         :")
#     totMark=int(input("enter total mark :"))
#     dic[name]=totMark
# for n,m in dic.items():
#     if int(m)>50:
#         count+=1
# print(f"{dic}  in this dictionary there are {count} student get total mark of more than 50! ")

#output:{'vivek': '56', 'jithu': '88', 'sudha': '45'}  in this dictionary there are 2 student get total mark of more than 50! 
#======================================================================================================================================

                                   # update the mark of a given student in a dict

#======================================================================================================================================
#solution:

choices=["y",'yes','yup','offcourse','defenitly','sure']
dic={'raju': '67',
     'radha': '55', 
     'kuttusan': '23',
     'mayavi': '100',
     'dakkini': '34'} 
while True:
    print("Old mark list    :=>",dic)
    name=input("student name who's mark wants to update:")

    mrk=int(input("enter updation mark:"))
    dic[name]=mrk
    choice=input("any other updations?:")
    if choice not in choices:
        break
    
print("updated mark list:=>",dic)


#output:
# Old mark list    :=> {'raju': '67', 'radha': '55', 'kuttusan': '23', 'mayavi': '100', 'dakkini': '34'}
# student name who's mark wants to update:dakkini
# enter the mark:00
# any other updations?:no
# updated mark list:=> {'raju': '67', 'radha': '55', 'kuttusan': '23', 'mayavi': '100', 'dakkini': 0}

#====================================END==========================================END========================================================



