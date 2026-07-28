# #update()
# #----------------------------------------
# d1={"name":"vivek",
#     "place":"koyilandy",
#     "ug":"bca"}

# d2={"name":"jithu",
#     "age":32,
#     "ug" :'bsc',
# }
# # print(d2)
# # d1.update(d2)
# print("before update the designation:",d1)
# d1.update({'designation':'it proffesionalist'})
# print("after updated of  designation: ",d1)

#output:
# before update the designation: {'name': 'vivek', 'place': 'koyilandy', 'ug': 'bca'}
# after updated of  designation:  {'name': 'vivek', 'place': 'koyilandy', 'ug': 'bca', 'designation': 'it proffesionalist'}



#============================================================================================================================
#PROBLOM 1:  Convert two lists into a dictionary
# values= [10,20,30]
# keys=['ten','twenty','thirty']

#============================================================================================================================
#solution :
# values= [10,20,30]
# keys=['ten','twenty','thirty']
# dic={}
# for i in range(0,len(keys)):
#     dic[keys[i]]=values[i]
# print(dic)

#output: {'ten': 10, 'twenty': 20, 'thirty': 30}
#============================================================================================================================
#PROBLOM 2:

#? Initialize dictionary with sutable  values
# foot_ball_players=["muller","naymer","messi",'ronaldo','backam','romero']
# devoloppers = ['Kelly','Emma','vivek','gaize','nizam','athira']
# cricket_players=['sachin','dhoni','sewag','dravid','gaguly']
# it     = {"designation":"developer","salary":23000}
# cricket = {"designation":"criket player","salary":2300000}
# footBall={'designation':"foot ball player","salary":50000000}

#===========================================================================================================================
#solution :
# foot_ball_players=["muller","naymer","messi",'ronaldo','backam','romero']
# devoloppers = ['Kelly','Emma','vivek','gaize','nizam','athira']
# cricket_players=['sachin','dhoni','sewag','dravid','gaguly']
# it     = {"designation":"developer","salary":23000}
# cricket = {"designation":"criket player","salary":2300000}
# footBall={'designation':"foot ball player","salary":50000000}


# income_chart={}

# for i in range(0,len(foot_ball_players)):

#     income_chart[foot_ball_players[i]]=footBall

# for i in range(0,len(devoloppers)):

#     income_chart[devoloppers[i]]=it

# for i in range(0,len(cricket_players)):

#     income_chart[cricket_players[i]]=cricket
# while True:
#     surch=input("which player details you want to know :")
#     print(surch,":",income_chart[surch])
#     choice=input("want to surch more1?:")
#     if choice=='n' or choice=='no' or choice=='nop':
#         break

#output:  which player details you want to know :messi
# messi : {'designation': 'foot ball player', 'salary': 50000000}
# want to surch more1?:y
# which player details you want to know :naymer
# naymer : {'designation': 'foot ball player', 'salary': 50000000}
# want to surch more1?:n 
# 
# 
# 
# to learn:  
# groups = {
#     "football": (foot_ball_players, footBall),
#     "cricket": (cricket_players, cricket),
#     "developer": (developers, it)
# }

# income_chart = {}

# for players, details in groups.values():
#     for player in players:
#         income_chart[player] = details



#
#============================================================================================================================
#PROBLOM 3:

 # Delete a list of keys from a dictionary

#===========================================================================================================================
#Solution:

# dic={'ten': 10, 'twenty': 20, 'thirty': 30, 'fourty':40, 'fifty':50, 'sixty':60, 'seventy':70}
# delt=input(f"{dic}\nwhich key you want to delete from this:")
# dic.pop(delt)
# print("dictionary after delete the enterd key is :",dic)

#============================================================================================================================
#PROBLOM 3:

# 4.  Get the key of a minimum value from the following dictionary

# dic={'ten': 10, 'twenty': 20, 'thirty': 30, 'fourty':40, 'fifty':50, 'sixty':60, 'seventy':70}

#===========================================================================================================================
# solution:

# dic = {"Physics":82,'chemistry':41, 'bio':23, "Maths":65,"History":75,'social':30}
# first=True
# for key,value in dic.items():
#   if first:
#     less_key=key
#     less_value=value
#     first=False

#   elif less_value > value:
#     less_key=key
#     less_value=value

# print(less_key)


# dic={'ten': 10, 'twenty': 20, 'thirty': 30, 'fourty':40, 'fifty':50, 'sixty':60, 'seventy':70}
# first=True
# for k,v in dic.items():
#   if first:
#     large_key=k
#     large_value=v
#     first=False
#   elif v>large_value:
#     large_key=k
#     large_value=v
# print(large_key,":",large_value)


#============================================================================================================================
#PROBLOM :

# 12. Write a program to count how many times each letter appears in a string using a dictionary.

#===========================================================================================================================

# sen=input("enter sentance:")
# letter_count={char:sen.count(char) for char in sen if char!=" "}
# sen=sen.split()
# word_count={word:sen.count(word) for word in sen if len(word)>1}
# print("letter and its count in this sentance:",letter_count)
# print("words and its count in this sentance:",word_count)
#print(f"the sentance has {letter_count[" "]} spaces")

#OutPut:enter sentance:i love python
#letter and its count in this sentance: {'i': 1, 'l': 1, 'o': 2, 'v': 1, 'e': 1, 'p': 1, 'y': 1, 't': 1, 'h': 1, 'n': 1}
# words and its count in this sentance: {'love': 1, 'python': 1}
#===========================================================================================================================

# dic={'ten': 10, 'twenty': 20, 'one thirty': 130, 'fourty':40, 'fifty':50, 'sixty':60, 'seventy':70}
# flag=0
# for k,v in dic.items():

#     if flag==0:
#         lk=k
#         lv=dic[k]
#         flag=1
#     elif v>lv:
#         lk=k
#         lv=v
# print(lk,":",lv)

#============================================================================================================================
#PROBLOM :

#  6. Given two dictionaries, merge them into one..

#===========================================================================================================================
#solution 1 :  IN TREDITIONAL WITH USING FOR LOOP

# dic1 = {"Physics":82,'chemistry':41, 'bio':23, "Maths":65}
# dic2={'ten': 10, 'twenty': 20, 'one thirty': 130}
# for key,value in dic1.items():
#     dic2[key]=value
# print(dic2)

#output:{'ten': 10, 'twenty': 20, 'one thirty': 130, 'Physics': 82, 'chemistry': 41, 'bio': 23, 'Maths': 65}
#============================================================================================================================

#============================================================================================================================
#PROBLOM :

#  6. Given two dictionaries, merge them into one..

#===========================================================================================================================
#solution 1 :  WITH USING * update() * FUNCTION

# dic1 = {"Physics":82,'chemistry':41, 'bio':23, "Maths":65}
# dic2={'ten': 10, 'twenty': 20, 'one thirty': 130}
# dic1.update(dic2)
# print("The first and second merged dictionary:  ",dic1)

#output:{'ten': 10, 'twenty': 20, 'one thirty': 130, 'Physics': 82, 'chemistry': 41, 'bio': 23, 'Maths': 65}
#============================================================================================================================

#PROBLOM :

# Create a dictionary of students with student names as keys and another dictionary with age, grade, and city as values.

#===========================================================================================================================

#solution:

# students={}

# while True:
#     dic={}
#     name=input("enter the name:")
#     age=input("enter age:")
#     grade=input("enter grade:")
#     city=input("enter city:")
#     dic['age']=age
#     dic['grade']=grade
#     dic['city']=city
#     students[name]=dic
#     esc=input("exit[ y / n ]?:")
#     if esc !='n':
#         break
# print(students)

#============================================================================================================================
#PROBLOM :

#. Given prices = {'apple': 100, 'banana': 60, 'cherry': 120}, print all items costing more than 80.

#===========================================================================================================================
#solution:

# prices = {'apple': 100, 'banana': 60, 'cherry': 120, 'grapes':130, 'orange':70, 'mango':81}
# hiegher_than_80={key:value for key,value in prices.items() if value>=80}
# print(hiegher_than_80)

#============================================================================================================================
#PROBLOM :

#. 14. Write a program to sort a dictionary by its keys.

#===========================================================================================================================
#solution:  WITH USING OF * sorted() * function   

# prices = {'apple': 100, 'banana': 60, 'cherry': 120, 'grapes':130, 'orange':70, 'mango':81}
# sortedDic={}
# for key in sorted(prices):
#     sortedDic[key]=prices[key]
# print(sortedDic)

#output : {'apple': 100, 'banana': 60, 'cherry': 120, 'grapes': 130, 'mango': 81, 'orange': 70}
#============================================================================================================================
#PROBLOM :

#. .16. Write a program to find the key with the maximum value in a dictionary.

#============================================================================================================================

# switch=True
# fruits={'apple': 100, 'banana': 60, 'cherry': 120, 'grapes': 130, 'mango': 81, 'orange': 70}
# for key,value in fruits.items():
#     if switch:
#         lk=key
#         lv=value
#         switch=False
#     elif lv<value:
#         lk=key
#         lv=value
# print(lk,":",lv)

#output: grapes : 130
#============================================================================================================================
#PROBLOM :

# Given a nested dictionary:
# student = {'name': 'Alice', 'marks': {'math': 80, 'science': 90}}
# Access the science marks.

#=========================================================================================================================
#solution:

# student = {'name': 'Alice', 'marks': {'math': 80, 'science': 90}}
# for key,value in student.items():
#     if type(value)==dict:
#         print(value['science'])

#============================================================================================================================
#PROBLOM :


#.5 Change value of a key in a nested dictionary

# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 6500}
# }

#=========================================================================================================================
#    solution:
        
# sample_dict ={'vivek': {'name': 'Jhon', 'salary': 7500},
#               'athul': {'name': 'Emma', 'salary': 8000},
#               'raju': {'name': 'Brad', 'salary': 6500}}

# for i in range(2,-1,-1):
#     emp_name=input("enter which persons salary want to update :")
#     if emp_name not in sample_dict:
#         print(f"INVALID EMPLOYEE NAME...!! Try with another name  you have {i} chance lest",)
#     else:
#         break
# else:
#     print("SORRY YOU REACHED the limit aLREADY....!")
# for key,value in sample_dict.items():
#     if key==emp_name:
#         for k,v in value.items():
#             if k=='salary':
#                 new_s=input("enter his new salary:")
#                 value[k]=new_s
        
# print(sample_dict)

#output:  INVALID EMPLOYEE NAME...!! Try with another name  you have 2 chance lest
# enter which persons salary want to update :sa
# INVALID EMPLOYEE NAME...!! Try with another name  you have 1 chance lest
# enter which persons salary want to update :as
# INVALID EMPLOYEE NAME...!! Try with another name  you have 0 chance lest
# SORRY YOU REACHED the limit aLREADY....!
# {'vivek': {'name': 'Jhon', 'salary': 7500}, 'athul': {'name': 'Emma', 'salary': 8000}, 'raju': {'name': 'Brad', 'salary': 6500}} 

#============================================================================================================================
#PROBLOM :

#  7. Swap keys and values in a dictionary. (Assume values are unique and hashable.)


#===========================================================================================================================
#    solution 1: treditional way with for loop

# main_dic={1:'a',
#      2:'b',
#      3:'c',
#      4:'d',
#      5:'e'}
# new_dic={}
# for k,v in main_dic.items():
#      new_dic[v]=k
# main_dic.clear()
# main_dic=new_dic.copy()
# print(main_dic)

#output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#NOTE=> BY USING THIS TREDITIONAL MMETHOD,,,,,!!! SO  WE CANT UPDATE  VALUES TO THE SAME DICTIONARY IN ONE LINE.
#       FIRST WE SHOULD CREATE A NEW NULL DICTIONARY FOR THE SWAP. AFTER THE SWAP COPY NULL DICTIONARY TO THE MAIN DICTIONARY.
#----------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------
# solution 2: with dictionary comprehension
         
# dic={1:'a',
#      2:'b',
#      3:'c',
#      4:'d',
#      5:'e'}
# dic1={value:key for value,key in dic.items()}
# print(dic)

#OUTPUT: {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
#============================================================================================================================
#PROBLOM :

# 11.d1 = {'a': 1, 'b': 2}
#  	d2 = {'b': 3, 'c': 4}
#  	Merge so that keys in d2 overwrite keys in d1


#===========================================================================================================================

d1 = {'a': 1, 'c': 2}
d2 = { 'b':1, 'd':4}
d3={}
d1.update(d2)
print(d1.sorted())

# print(d1)

#============================================================================================================================
#PROBLOM :

#  7. Swap keys and values in a dictionary. (Assume values are unique and hashable.)


#===========================================================================================================================




#  15. Write a program to sort a dictionary by its values




#.
# 
