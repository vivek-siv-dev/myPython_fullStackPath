# name=input("name")
# age=int(input("age:"))
# c=input("country:")
# id=input("you have valid id card(y/n):")
# if age>18:
#     if c=="india":
#         if id=="y":
#             print("yes you are elegible to vote")
#         else:
#             print(f"mr.{name} your age and nationality is eligible for vote but you dont have a valid id so you can't vote")
#     else:
#         print(f"mr.{name} you cant vote becose you are not an indian")
# else:
#     print("wait for 18.... you can vote after 18 in india ")
           

# n=int(input("enter number:"))
# if n>=100 and n<=999:
#     if n%2==0:
#         print("the number is 3 digit and also an EVEN number")
#     else:
#         print("the number is 3digit but not an EVEN NUMBER")
# else:
#     print("the eneterd number is not a 3 DIGIT NUMBER ")
#-------------------------------------------------------- 4 DIT ENDS WITH ZERO
# n=int(input("enter a number:"))
# x=str(n)
# if len(x)==4:
#     if n%10==0:
#         print("the number is 4 digit and end with ZERO")
#     else:
#         print("the number is 4 35DIGIT but not ending with ZERO")
# else:
# #     print("the enterd number is not a 4 digit number")
#     #===================================================================================================================================================
# un="user"
# pw="password"
# u=input("enter use name: ")
# if un==u:
#     p=input("password: ")
#     if p==pw:
#         print("LOGIN SUCCSUSSFULL...!")
#     else:
#         print("INCORRECT PASSWORD")
# else:
#     print("enter a valid user name...!")
# #------------------------------------------------NESTED IF --------------------------------------------------------
# n=int(input("enter no:"))
# if n%3==0:
#     if n%5==0:
#         if n%8==0:
#             print("the number is divisible by 3,5,and 8")
#         else:
#             print("the number is divisible by 3,5 not with 8")
#     else:
#         print("the number IS ONLY divisible by 3 ")
# else:
#     if n%5==0:
#         if n%8==0:
#             print("the enterd number is not divisible by 8 and 5 and not divisible by 3")
#         else:
#             print("the number is not divisible by 3 and 8 but it can with 5")
#     else:
#         if n%8==0:
#             print("the number can ONLY DIVISIBLE BY 8 ")
#         else:
#             print("this number can't divisible by 3,5 or 8")

#---------------------------------------------------------------------------------------------------------------------
# 1.# Check whether a number is positive, negative, or zero using nested if.
# 2.# Check whether a number is positive and even using nested if.
# 3.# Find the greater number between two numbers using nested if.
# 4.# Check whether a person is eligible to vote.
#       # Age > 18
#       # Citizen = Yes
# 5.# Check whether a student has passed.
#        # Marks ≥ 40
#        # Attendance ≥ 75%
# 6.# Find the largest among three numbers using nested if.
# 7.# Determine the grade of a student:
#      # Marks ≥ 90 → A
#      # Marks ≥ 75 → B
#      # Marks ≥ 60 → C
#      # Otherwise → Fail
# 8.# ATM Withdrawal Program
#      # PIN must be correct.
#      # Balance must be sufficient.
#      # Amount must be a multiple of 100.     
# 9.# Login System
#     # Username must be correct.
#     # Password must be correct.
#     # OTP must be correct.     
# 10.# Admission Eligibility
#      #Age ≥ 17
#      # Marks ≥ 60
#      # Entrance Exam ≥ 50
# 11.# Employee Bonus Calculation
#       # Experience > 5 years
#       # Salary < 50000
#       # Then give 10% bonus    
# 12.# Determine whether a number is:
#       # Positive
#       # Even
#       # Divisible by 5
# 13.# Bank Loan Eligibility
#       # Age ≥ 21
#       # Salary ≥ 25000
#       # Credit Score ≥ 700      
# 14.#Blood Donation Eligibility
#       # Age between 18 and 60
#       # Weight ≥ 50 kg


# 5.# Check whether a student has passed.
#        # Marks ≥ 40
#        # Attendance ≥ 75%
# #5    --------------------------------------- attendence and msrk----------------------------------------------------------------------
# m=int(input("emter your mark:"))
# a=int(input("enter your attendence percentage:"))
# if a>=75:
#     if m>=40:
#         print("****CONGRATZ!!  YOU PASSED THE 6TH SEM!!!*****")
#     else:
#         print("""FAID
#               CAUSE:SHORTAGE OF MARK
#               YOUR MAR IS:""",m)
# else:
#     if m<40:
#        print("""         **** FAILD ****
#         CAUSE:YOUR ATTENDANCE SHORTAGE and  LESS EXAM SCORE 
#         your mark is:""",m)
#        print("     your attendance is:",a)
#     else:
#         print("""FAILD
#         CAUSE: ATTENDANCE SHORTAGE""") 


# -------------------------------------------------------------* GRADE *-------------------------------------------------------------------------------------------- 
# 
# # 7.# Determine the grade of a student:
#      # Marks ≥ 90 → A
#      # Marks ≥ 75 → B
#      # Marks ≥ 60 → C
#      # Otherwise → Fail
# #        
# m=int(input("ENTER YOUR MARK:"))
# if m<60 and m>0:
#     print("         *FAILD*         ")
# elif m>=60 and m<75:
#     print("YOU PASS THE EXAM WITH [C] GRADE")
# elif m>=75 and m<90:
#     print("YOU ARE PASS THE EXAM WITH [B] GRADE")
# elif m>=90:
#     if m>100:
#         print("*PLLEASE CHECK THE MARK YOU ENTERD*, \nTHE MARK SHOULD BE IN THE RANGE OF {0 - 100}")
#     else:
#         print("YOU  PASS  WITH [A] GRADE")
# else:
#     print("PLEASE CHECK THE MARK YOU ENTERD\nYOU ENTERD : ",m," \nMARK SHOULD WITH IN [0 TO 100]")
#------------------------------------------------------------------------------------------------------------------------------------------------------
# 11.# Employee Bonus Calculation
#       # Experience > 5 years
#       # Salary < 50000
#       # Then give 10% bonus
#------------------------------------------------------------------ * Employee Bonus Calculation * ----------------------------------------------------

# e=float(input("ENTER YOUR EXPERIANCE IN THIS COMPANY: "))
# if e > 5:
#     s=int(input("ENTER YOUR CURRENT SALARY IN THIS FIRM: "))
#     if s<50000:
#         b=(s*10)/100
#         s+=b
#         print("YOUR THIS MONTH SALARY WTH BONUS IS :",s)
#     else:
#         print("SORRY YOU ARE NOT ELEGIBLE FOR THE BONUS.  BONUS SHOULD BE ALLOWD ONLY FOR WHO WORKS UNDER 500000")
# else:
#     print("SORRY YOU ARE NOT ELEGIBLE FOR THIS BONUS BECUASE YOU DONT HAVE MORE THAN 5 YEARS OF EXPERIANCE IN THIS COMPANY")


#-------------------------------------------------------------------------------------------------------------------------------------------------------------

# 13.# Bank Loan Eligibility
#       # Age ≥ 21
#       # Salary ≥ 25000
#       # Credit Score ≥ 700 

#---------------------------------------------------- Bank Loan Eligibility----------------------------------------------------------------------------

# a=int(input("enter  age:"))
# if a>=21 and a<=99:   
#     s=int(input("enter salalary:"))
#     if s>=25000:
#         cs=int(input("Enter Credit Score:"))
#         if cs>=700:
#             print("CONGRAGULATIONS YOU ARE ELIGIBLE FOR THE BANK LOAN!!!")
#         else:
#           print(" insuficiant credit score")
#     else:
#         print("salary inceficiant for the loan ")
# else:
#     print("AGE IS NOT ELIGIBLE FOR THE LOAN......!")

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# 14.#Blood Donation Eligibility
#       # Age between 18 and 60
#       # Weight ≥ 50 kg
#----------------------------------------------------------14.#Blood Donation Eligibility---------------------------------------------------------------
# age=int(input("age:"))

# if age>=18 and age<=60:
#     weight=float(input("enter weight:"))
#     if weight>=50:
#         print("CAN DONATE BLOOD")
#     else:
#         print("YOU CAN'T DONATE THIS TIME BECAUSE YOUR WEIGHT UNDER 50.")
# else:
#     weight=float(input("enter weight:"))
#     if weight<50:
        
#        print("YCAN'T DONATE BLOOD..., AGE AND WEIGHT CRITERIA NOT MET")
#     else:
#        print("NOT ELIGIBLE DUE TO AGE")


#======================================================== prime numbers up to n =======================================================


# n=int(input("enter the number:"))
# i=1
# while i<=n:
#     count=0
#     j=1
#     while j<=i:
#         if i%j==0:
#             count+=1
#         j+=1
#     if count==2:
#         print(i)
#     i+=1

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     END      <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        

