#PRIME NUMBER
#--------------------------------------------------------------------------

def check_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return ' '
        else:
            return n

n=int(input("limit:"))
for i in range(2,n+1):
    print(check_prime(i))
        


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



