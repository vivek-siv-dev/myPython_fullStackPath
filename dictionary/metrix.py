#[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] *  METRIX  * ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]


# metrix1=[[1,2,3], [4, 5, 6],[7,8,9]]
# # print(metrix1)
# for i in metrix1:
#     for j in i:
#         print(j,end="    ")
#     print()   # for print in next line

#output: 1    2    3    
#        4    5    6    
#        7    8    9  
#========================================================================================================================================

#PROBLOM 1 :   READ TWO METRIX AND PRINT ITS RESULT METRIX.

#=========================================================================================================================================
# #solution:


# metri1  =[]
# metri2  =[]
# metri_sum=[]
# row=int(input("how many row in your metrix   :"))
# col=int(input("how many column in your metrix:"))

# for i in range(row):
#     sub1=[]
#     for j in range(col):
#         data=int(input(f"enter data for first metrix==> [ {i}:{j} ] :"))
#         sub1.append(data)
#     metri1.append(sub1)


# for i in range(row):
#     sub1=[]
#     for j in range(col):
#         data=int(input(f"enter data for  metrix==> [ {i}:{j} ] :"))
#         sub1.append(data)
#     metri2.append(sub1)

# for i in range(row):
#     temp=[]
#     for j in range(col):
#         temp.append(metri1[i][j] + metri2[i][j])
#     metri_sum.append(temp)


# print("\n FIRST METRIX:\n------------------------------------\n")
# for i in range(row):
#     for j in range(col):
#         print(metri1[i][j],end="   ")
#     print("\n")
    
# print("\n SECOND METRIX:\n------------------------------------\n")

# for i in range(row):
#     for j in range(col):
#         print(metri2[i][j], end="  ")
#     print("\n")

# print("\n RESULT METRIX:\n------------------------------------\n")

# for i in range(row):
#     for j in range(col):
#         print(metri_sum[i][j], end="  ")
#     print("\n")
#========================================================================================================================================

#PROBLOM 2 :   READ TWO METRIX AND PRINT ITS DEFFERENCE METRIX.(SUBSTACTION)

#=========================================================================================================================================
#solution:


# metri1  =[]
# metri2  =[]
# metri_sum=[]
# row=int(input("how many row in your metrix   :"))
# col=int(input("how many column in your metrix:"))

# for i in range(row):
#     sub1=[]
#     for j in range(col):
#         data=int(input(f"enter data for first metrix==> [ {i}:{j} ] :"))
#         sub1.append(data)
#     metri1.append(sub1)


# for i in range(row):
#     sub1=[]
#     for j in range(col):
#         data=int(input(f"enter data for  metrix==> [ {i}:{j} ] :"))
#         sub1.append(data)
#     metri2.append(sub1)

# for i in range(row):
#     temp=[]
#     for j in range(col):
#         temp.append(metri1[i][j] - metri2[i][j])
#     metri_sum.append(temp)


# print("\n FIRST METRIX:\n------------------------------------\n")
# for i in range(row):
#     for j in range(col):
#         print(metri1[i][j],end="     ")
#     print("\n")
    
# print("\n SECOND METRIX:\n------------------------------------\n")

# for i in range(row):
#     for j in range(col):
#         print(metri2[i][j], end="    ")
#     print("\n")

# print("\n RESULT METRIX:\n------------------------------------\n")

# for i in range(row):
#     for j in range(col):
#         print(metri_sum[i][j], end="    ")
#     print("\n")

#=========================================================================================================================================
#PROBLOM 3 : [3 X 3] METRIX MULTIPLICATION

#=========================================================================================================================================
#solution:
m1=[[1, 2, 4], [3, 6, 5], [7, 8, 9]]
m2=[[4, 8, 7], [3, 9, 1], [1, 2, 0]]

result_main=[]
#-------------------#         #-------------------#             #-------------------#
#       1   2   4   |         #       4   8   7   |             #     14    34     9 
#  M1=> 3   6   5   |    X    #  M2=> 3   9   1   | ========>   #     
#       7   8   9   |         #       1   2   0   |
#-------------------#         #-------------------#

for i in range(3):
    for j in range(3):
        result=0
        result_sub=[]
        for k in range(3):
            result+=m1[j][k]*m2[k][j]
        result_sub.append(result)
    result_main.append(result_sub)
print(result_main,end=" ")

    

    
    



        


