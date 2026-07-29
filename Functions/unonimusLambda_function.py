#MAP FUNCTION
#SYNTAX:
    # map(function, iterating_variable)'=
    # eg:
        # lst=[10,20,30,40,50]
        # a=list(map(lambda x:x*x,lst))


# lst=[1,2,3,4,5]
# a=list(map(lambda x:x*x,lst))
# print(a)
# #output:[1, 4, 9, 16, 25]


lis=[10,20,30,40,50,60,70,80]
a=list(map(lambda i:i**2,lis))
print(a)