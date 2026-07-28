# =======================================================================================================================
#
                                #read and update data to a nested_dictionary
#
#=========================================================================================================================

import os
choices=["y",'yes','yup','offcourse','defenitly','sure']
mainDict={}


def header():
    print(f"\n\n{'='*40} personal data form{'='*40}" .upper())


def add_data():
    while True:
        subDict={}
        email=input("enter email:")
        name=input("enter the name:")
        subDict['name']=name
        age=input("enter the age:")
        subDict['age']=age
        city=input("enter the city:")
        subDict['city']=city
        mainDict[email]=subDict

        user_choice=input(" \nDO YOU HAVE ANY OTHER DATA TO ADD:".lower())
        if user_choice not in choices:
            break

    print(f"\n{'-'*165} \n Old Data:{mainDict} \n{'-'*165}\n")


def update_data(u='n'):
    while True:
        uc='yes'
        print(f"\n{'-'*165} \n Old Data:{mainDict} \n{'-'*165}\n")
        if u not in choices:
            uc=input("\nDO YOU HAVE ANY DATA TO UPDATE IN THIS:")
        if uc.lower() not in choices:
            print("ok bei")
            break

        else:
            mailToUpdate=input("enter email id of the person to update his data:".title())
            old=input(f"for {mailToUpdate} what personal data want to update:")
            new=input("with what?:")
    
    
            for i,j in mainDict.items():
                if i==mailToUpdate:
                    for k,l in j.items():
                        if k==old:
                            j[k]=new
            os.system('cls')
            header()
            print(f"\n{'-'*160}\nupdated Data:{mainDict} \n{'-'*160}")
            user_choice=input("\nUPDATED SUCSSESSFULLY.....!!! \nDO YOU HAVE ANY OTHER DATA TO UPDATE".lower())
            if user_choice not in choices:
        
                break

while True:
    option=int(input("1.Add Data\t\t2.Update\n\n[Select 1 or 2]:"))
    if option==1:
        os.system('cls')
        header()
        add_data()
        u=input("do you want to update any data in this dictionar?:")
        if u in choices:
            update_data(u)
        break
    elif option==2:
        os.system('cls')
        header()
        if mainDict:
            update_data()
            break
        else:
            os.system('cls')
            print("dictionary empty!!!  No data to be update. please add data first ")
    else:
        print("wrong choice.... try again...!!!")




