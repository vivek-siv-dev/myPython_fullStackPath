
#===========================================================================================================
# hiegher order functions are the functions that recieve another function as an argument
# map, filter functions are comonly called heigher order functions
#because they take other other function as arguments

#========================================================================================================= 

#==================================================================================================

# use hiegher order function to find the interest for different interst rate
# equation:p*n*r
# interest_rate=[0.05, 0.1, 0.15, 0.2]

#===================================================================================================
#soluton
interest_rate=[0.05, 0.1, 0.15, 0.2]
amount=10000
piriod=5
interest=list(map(lambda i : amount*piriod*i,interest_rate))
print(interest)





#create an anounimous function to find farenheet from celsious 
# equation (c*9/5)+32