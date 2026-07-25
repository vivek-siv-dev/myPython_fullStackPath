#PRIME NUMBER
#--------------------------------------------------------------------------
n=int(input("limit:"))
for i in range(2,n+1):
    prime=True
    for div in range(2,int(i**0.5)+1):
        # print(div)
        if i%div==0:
            prime=False
    if prime:
         print(i,end=" ")


#METRIX MULTIPLICARTION
#-------------------------------------------------------------------------

# m1=[[5, 4, 6],[2, 2, 4],[2, 1, 5]]
# m2=[[1, 4, 0],[2, 4, 1],[0, 1, 2]]
# pro=[]
# for row in range(len(m1)):
#     sub=[]
#     for col in range(len(m1)):
#         result=0
#         for k in range(len(m1)):
#             result+=m1[row][k]*m2[k][col]
#         sub.append(result)
#     pro.append(sub)
# for i in range(len(m1)):
#     print(m1[i],"\t",m2[i],"\t",pro[i],"\n")



