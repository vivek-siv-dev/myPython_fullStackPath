# #practices:


# dict1={"name": "vivek", "ph": "8156966560"}
# print(dict1)
# #output: {'name': 'vivek', 'ph': '815696656')

# print(dict1["name"])
# #output: vivek
# #______________________________________________________________________
# #dictionary value insertion
# dict={}
# dict["name"]="vivek"
# dict["ph"]  ="8156966560"
# print(dict1)
# #_____________________________________________________________________

# fam={}
# l=input("enter the limit:")
# for i in range(0,3):
#     key=input("enter key:")
#     value=input("enter the value:")
#     fam[key]=value
# print(fam)
#-----------------------------------------------------------------------------
#formkey
#-----------------------------------------------------------------------------

# dic={}
# keys={'a','b','c','d'}
# dic=dict.fromkeys(keys,8)
# print(dic)

#-----------------------------------------------------------------------------
#get()
#-----------------------------------------------------------------------------

# d={"name":"vivek","house":"eleyidath"}
# print(d.get("name"))
#----------------------------------------------------------------------------

#print a dictionary  like this ["vivek":30, jithu:30]
# fam={}
# for i in range(0,2):
#     name=input("enter the nmae:")
#     age=int(input("enter the age:"))
#     fam[name]=age
# print(fam)
#---------------------------------------------------------------------------

#         #.items()

#_________________________________________________________________________
# fam={"jithu":31,"vivek":31,"jithu":31, "jwalin":2.7}
# for i,j in fam.items():
#     print(i,j)

#output:  jithu 31
#         vivek 31
#         jwalin 2.7
#---------------------------------------------------------------------------

#         #.keys()

#__________________________________________________________________________
# fam={"jithu":31,"vivek":31,"jithu":31, "jwalin":2.7}
# for i in fam.keys():
#     print(i)

#output:  jithu 
#         vivek 
 #        jwalin
#---------------------------------------------------------------------------

#         #.keys()

#__________________________________________________________________________

# fam={"jithu":31,"vivek":31,"jithu":31, "jwalin":2.7}
# for i in fam.values():
#     print(i)

#output:  31
#         31
#         2.7
#---------------------------------------------------------------------------



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#problem:
#                                               # convert 2 list in to dictionary
#                                               # keys=["mark1","mark2","mark3","mark4","mark5","mark6","mark7"]
#                                               # values=[40,38,34,45,43,22,40]

#____________________________________________________________________________________________________________________________________________________________________
# solution.2 with using zip()       eg: dict(zip(keys,value)) 

# keys=["mark1","mark2","mark3","mark4","mark5","mark6","mark7"]
# values=[40,38,34,45,43,22,40]
# marklist=dict(zip(keys,values))
# print(marklist)

#output: {'mark1': 40, 'mark2': 38, 'mark3': 34, 'mark4': 45, 'mark5': 43, 'mark6': 22, 'mark7': 40}
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#problem:
#                                               # convert 2 list in to dictionary
#                                               # keys=["mark1","mark2","mark3","mark4","mark5","mark6","mark7"]
#                                               # values=[40,38,34,45,43,22,40]

#____________________________________________________________________________________________________________________________________________________________________
#solution:  WITH USING TREDITIONAL FOR LOOP

# keys  =["mark1","mark2","mark3","mark4","mark5","mark6","mark7"]
# values=[40,38,34,45,43,22,40]
# marklist={}
# for i in range(0,len(keys)):
#     marklist[keys[i]]=values[i]
# print(marklist['mark4']) #output: 45
# print(marklist)          #output: {'mark1': 40, 'mark2': 38, 'mark3': 34, 'mark4': 45, 'mark5': 43, 'mark6': 22, 'mark7': 40}   
 #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#problem:
#                                           # read key and value with user and ask user to which value to be delete

#____________________________________________________________________________________________________________________________________________________________________   
#solution:


# dic={'name':'vivek', 'age':33, 'place':'koyilandy','ph':'8156966560'}
# dlt=input(f"{dic} <=== which key value pair in this dictionary you want to delete:")
# dic.pop(dlt)
# print(f"the dictionary after delete {dlt} is  : {dic}")

#output:{'name': 'vivek', 'age': 33, 'place': 'koyilandy', 'ph': '8156966560'} <=== which key value pair in this dictionary you want to delete:ph
#the dictionary after delete ph is  : {'name': 'vivek', 'age': 33, 'place': 'koyilandy'}
 #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#problem:
#                                               # READ mark from heigh school or hs students SUBJECT AND STORE IT IN a DICTIONARY 

#____________________________________________________________________________________________________________________________________________________________________ 
#solution:
sec_sub   = ['english','2nd language','chemistry','biolagy','phisics','social','maths','info tech']
hs_sc_sub = ['chemistry','biology','phisics','maths','zuology','botoni']
hs_com    = ['business','accountency','english','ecnomics','maths','com_ap']
hs_hum    = ['english','2nd language','politics','history','evs']
group=0
marklist={}    #or also we can create a dict like marklist=dict()
name=input(" name:")
mark_list={}
std=input(f"in which class {name} belongs to:")
if std=='8th' or std=='8' or std=='9' or std=='9th' or std=='10th' or std=='10':
    if '8' in std:
        std="8th"
    elif '9' in std:
        std='9th'
    else:
        std='10th'

    for subject in sec_sub:

       # key=  input("enter the subject :")
        try:
            value=int(input(f"enter the mark  of {subject}:"))
        except ValueError:
            print("enter only digits")
        mark_list[subject]=value
elif std=='11th' or std=='11' or std=='12th' or std=='12' or std=='+2' or std=='+1' :
    if '11' in std or '+1' in std:
        std='+1'
    else:
        std='+2'    
    print("""1.scince       2.commerce          3.humanitees""")
    group=int(input("select group [1 or 2 or 3]:"))
    if group==1:
        for subject in hs_sc_sub:
            try:
                value=int(input(f"enter mark for the subject {subject}:"))
            except ValueError:
                print("enter only numbers for the mark...!!!")
            mark_list[subject]=value

    elif group==2:
        for subject in hs_com:
            try:
                value=int(input(f"enter mark for the subject {subject}:"))
            except ValueError:
                print("enter only numbers for the mark...!!!")
            mark_list[subject]=value

    elif group==3:
        for subject in hs_hum:
            try:
                value=int(input(f"enter mark for the subject {subject}:"))
            except ValueError:
                print("enter only numbers for the mark...!!!")
            mark_list[subject]=value

#print(f"mark lisk of {name.upper()} CLASS {std.upper()}: {mark_list}")



if group==2:
    print(f"\nMARK LIST \nNAME:{name.upper()}   course: {std} commerce\n-----------------------------------------")
    for sub in hs_com:
        print(sub,"   \t\t:",mark_list[sub])
    print("\n")
    k=max(mark_list,key=mark_list.get)
    print("TOTAL MARK    :",sum(mark_list.values()))
    print("HIEGHEST MARK :",max(mark_list,key=mark_list.get),mark_list[k])
elif group==1:
    print(f"\nMARK LIST \nNAME:{name.upper()}  Course: {std} scince\n--------------------------------------------------")
    for sub in hs_sc_sub:
        print(sub,"   \t\t\t:",mark_list[sub])
    print("\n")
    k=max(mark_list,key=mark_list.get)
    print("TOTAL MARK    :",sum(mark_list.values()))
    print("HIEGHEST MARK :",max(mark_list,key=mark_list.get),mark_list[k])
elif group==3:
    print(f"\nMARK LIST \nNAME:{name.upper()}  course: {std} humanitees\n----------------------------------------------")
    for sub in hs_hum:
        print(sub,"   \t\t\t:",mark_list[sub])
    print("\n")
    k=max(mark_list,key=mark_list.get)
    print("TOTAL MARK    :",sum(mark_list.values()))
    print("HEIEGHEST MARK :",mark_list[k],max(mark_list,key=mark_list.get))
else:
    print(f"\nMARK LIST \nNAME:{name.upper()}  Course: {std}\n-------------------------------------")
    for sub in sec_sub:
        print(sub,"   \t\t\t:",mark_list[sub])
    print("\n")
    k=max(mark_list,key=mark_list.get)
    print("TOTAL MARK    :",sum(mark_list.values()))
    print("HEIEGHEST MARK :",mark_list[k],max(mark_list,key=mark_list.get))



























#problem:                                                    # create dict with user input keys and value

#____________________________________________________________________________________________________________________________________________________________________

#solution

# l=int(input("HOW MANY KEY VALUE PAIR YOU WANT TO ENTER :"))
# dt={}
# keys=[]
# for i in range(0,l):
#     while True:
#         key=input("enter the key    :")
#         if key in keys:
#             print("the key value you enterd already EXIST in the dictionary!!!!   please enter a unique key value")   
#         else:
#             keys.append(key)
#             break

#     value=input("enter the value:")
#     dt[key]=value
# print(dt)

#output:NORMALY

#HOW MANY KEY VALUE PAIR YOU WANT TO ENTER :4
# enter the key    :name
# enter the value:vivek
# enter the key    :age 
# enter the value:31
# enter the key    :place
# enter the value:koyilandy
# enter the key    :ug
# enter the value:bca
# {'name': 'vivek', 'age ': '31', 'place': 'koyilandy', 'ug': 'bca'}

# 
# OUTPUT: IF YOU TRY TO ENTER A MORE THAN ONE SAME KEY NAME!!!!

# HOW MANY KEY VALUE PAIR YOU WANT TO ENTER :4
# enter the key    :name
# enter the value:vivek
# enter the key    :name
# the key value you enterd already EXIST in the dictionary!!!!   please enter a unique key value
# enter the key    :








#

# read a dictionoary with mark1 to mark5 and fid the greatest mark
# read a dictionary and print keys and value with loop
