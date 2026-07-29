# def details(name,age):
#     return name,age

# print(details(age=32,name="vivek"))





#  metrix:

# m1=[[1,2,3],[4,5,6],[3,5,6]]
# m2=[[1,0,3],[4,2,1],[3,2,6]]
# main=[]
# for i in range(len(m1)):
#     sub=[]
#     for j in range(len(m1)):
#         sum=0
#         for k in range(len(m1)):
#             sum+=m1[i][k]*m2[k][j]
#         sub.append(sum)
#     main.append(sub)
# print(main)

lst=[]
no=int(input("number of persone to  add:"))
for i in range(no):
    key=input("enter name:")
    value=input("qualification:")
    lst.append((key,value))
print(lst)
s=list(sorted(lst,key=lambda x : x[0]))
print(s)

# sorted_lst=sorted(lst, key=lambda i : i[0])