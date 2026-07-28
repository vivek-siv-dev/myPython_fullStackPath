print("""    1.add    ✚
    2.view   👁️
    3.update 🔄
    4.delete 🗑️
    5.exit   🏃""")
main_dict={}
time_out=2
while True: 
    
    cho=int(input("enter your choice:"))
    if 5>=cho>=1:
        if cho==1:
            l=int(input("how many persons data u want to enter:"))
            for i in range(l):
                sub_dict={}
                ph=[]
                mail=str(input("Mail id 📧:"))
                name=str(input("👉 name   :"))
                count=int(input("how many phone📞 number to be add.?:")) 
                for i in range(count):  
                    ph_number=int(input(f"enter {i+1} phone📞 number:"))
                    ph.append(ph_number)
                sub_dict['name']=name
                sub_dict['mail']=mail
                sub_dict['phone_number']=ph
                main_dict[mail]=sub_dict

        elif cho==2:
            print("📋",main_dict)
        
        elif cho==3:
            email=input("Enter the mail id 📧 for which persons data you want to update:")
            if email in main_dict:
                print("📋",main_dict[email])
                count=1
                while True:
                    up=input("enter which data 📋 you want to update in it:")
                    
                    if up in sub_dict:
                        if up=='mail':
                            new_data=input(f"Enter the new value for {up}📧:")
                            main_dict.pop(email)
                            sub_dict['mail']=new_data
                            main_dict[new_data]=sub_dict
                            print("E-MAIL ID updated successfully✅")
                            break
                        elif up=='name':
                            new_data=input(f"Enter the new value for {up} :")
                            sub_dict[up]=new_data
                            print("NAME updated successfully✅")
                            break
                        elif up=='phone_number' or 'number' or 'phone':
                            l=int(input("how many 📞 phone numbers have to enter:"))
                            ph=[]
                            for i in range(l):
                                new_data=int(input(f"Enter the {i+1} new value for {up} :"))
                                ph.append(new_data)
                            sub_dict[up]=ph
                            print("PHONE_NUMBER updated successfully✅")
                            break

                    elif count<3:
                        print(f"\nINVALID ENTRY⛔\n  there is no data named {up} in it\n")
                        count+=1
                    else:
                        print(f"\nUPDATION NOT COMPLETED ⛔ there is no data named {up} in it .... you reached the attempt llimit\n")
                        break


    # elif cho==4:
    #     del main_dict  
    #     print("viviviiivviivivivviviivvi")         
    elif cho==5:
            break
    else:
        if time_out!=0:
            
            print(f"INVALID option enterd!⚠️ you have {time_out} attempt left")
            time_out-=1
        else:
            print("\ngood bye..👋👋 \n\nyou have reached the maximum number of attempt 😵‍💫❌\n")
            break
        
        
    
