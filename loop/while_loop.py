# #========================================= print multiplication table of given number=======================

# n=int(input("enter the number              :"))
# l=int(input("enter the limit do you want to print:"))
# i=1
# while i<=l:
#     print(i,"*",n,"=",n*i,"\n")
#     i+=1
# #============================================ * EVEN NUMBER DIGIT IN A NUMBER * =====================================================

# n=int(input("enter a number : "))
# count=0
# while n!=0:
#     i=n%10
#     if i%2==0:
#         count+=1

#     i=0
#     n=n//10
# print(count)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> END  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# # +++++++++++++++++++++++++++++++++++++++=============   lARGEST DIGIT OF A NUMBER   =============+++++++++++++++++++++++++++++++++++++++===============
# n=int(input("enter a number:"))
# largest=0
# while n!=0:
#     cut=n%10
#     if cut>largest:
#         largest=cut
#     n=n//10
# print("largest digit is:",largest)


# ==============================================================   PRIME NUMBER UP TO N   =============================================================
# n=int(input("enter a number:"))
# i=1
# primeNumbers=""
# while i<=n:
#     count=0
#     j=1
#     while j<=n:
#         if i%j==0:
#             count+=1
#         j+=1
#     if count==2:
#         primeNumbers+=str(i)+" "
#     i+=1
# print("prime numbers up to", n, "are:", primeNumbers)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> END  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#================================================================  FIBINOCCCI SERIES UP TO N==========================================================
# n=int(input("enter the limit:"))
# n = int(input("How many terms? "))

# a = 0 
# b = 1
# i = 1

# while i <= n:
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
#     i += 1


#================================================================== CONTINUE ===================================================================

# i=0
# while i<10:
#     i+=1
#     if i==5:
#         continue
#     print(i)
#    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> END  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#================================================================  WHILE TRUE==========================================================

#Q THE NUMBER GUSSING GAME USING WHILE TRUE

while True:
    x=int(input("ENTER YOUR GUSS:")) 
    if x==108:
        print("CONGRATZ..!!!! YOU WIN THE GAME")
        break
    else:
        if x>108:
            print("gussed number is grater than the exact ")
        else:
            print("the gussed number is less than the exact")
            print("GAME OVER...!!!")
