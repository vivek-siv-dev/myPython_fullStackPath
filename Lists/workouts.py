#===================================================================================================================================

#1.PROBLEM  :	Create a set named fruits with elements: "apple", "banana", "cherry". Print it.

#===================================================================================================================================
# *SOLUTION : creating set with { }

# fruits={"apple","banana",'cherry'}
# print(fruits)

# output :   {'banana', 'cherry', 'apple'}

#===================================================================================================================================

#2.PROBLEM  :	Add "orange" to the fruits set.

#===================================================================================================================================
# *SOLUTION : using add() function

# fruits={"apple","banana",'cherry'}
# fruits.add("orange")
# print(fruits)

#OUTPUT :  {'orange', 'cherry', 'apple'}
#===================================================================================================================================

#2.PROBLEM  :	Remove "banana" from the set using both .remove() and .discard() — see the difference.

#--------------------------------------------------------------------------
# remove(element):           Deletes the specified element from the set. 
# If the element is not present, it raises a KeyError 
#----------- -------------- ------------- ---------------------------------
# discard(element):         Deletes the specified element if it exists.
# If the element is not present, it does nothing and no error is raised 
#--------------------------------------------------------------------------

#===================================================================================================================================
# *SOLUTION : USING remove() function

# fruits={"apple",'cherry',"orange"}
# fruits.remove("banana")
# print(fruits)

#OUTPUT :  KeyError: 'banana'    BECAUSE "banana" IS NOT PRESENT IN THE SET
#-----------------------------------------------------------------------------------------------------------------------------------
# *SOLUTION : USING discard() function

# fruits={"apple", 'cherry', "orange"}
# fruits.discard("banana")
# print(fruits)

#OUTPUT :  {'orange', 'cherry', 'apple'}--> [ ACTUALLY BANANA IS NOT PRESENT IN THE SET BUT WE NEVER GET ERROR WHILE WE USE discard()]

#===================================================================================================================================


# 4.PROBLEM  :   Check if "apple" is present in the set.

#===================================================================================================================================
# *SOLUTION : using of 'in' or 'not in' with set
# fruits={"apple", "orange", "mango"}
# if "apple" in fruits:
#     print("yes apple is present in the set of fruits")

#OUTPUT :  yes apple is present in the set of fruits
#===================================================================================================================================

# 5.PROBLEM  : Find the length of the set.   

#===================================================================================================================================
# *SOLUTION :   using of len() function in set

# fruits={"apple", "orange", "mango"}
# print(len(fruits))

    #OUTPUT : 3

#===================================================================================================================================

# 6.PROBLEM  :Create two sets a = {1,2,3,4} and b = {3,4,5,6}. Find their union.  

#===================================================================================================================================
# *SOLUTION : use of union funtion or the symbol |

# a = {1,2,3,4}
# b = {3,4,5,6}
# c = a.union(b) # or we can do a|b  this two are  same 
# print(c)

#  OUTPUT : {1, 2, 3, 4, 5, 6}
#===================================================================================================================================

#7. PROBLEM  : Find the intersection of the two sets above. 

#===================================================================================================================================
# *SOLUTION : using of intersection function

# a = {1,2,3,4}
# b = {3,4,5,6}
# c=a.intersection(b)
# print(c)

# output : {3, 4}
#===================================================================================================================================

# 8. PROBLEM  : Find the difference between the two sets (a - b and b - a). 

#===================================================================================================================================
# *SOLUTION :    using difference() function with - symbol

# A = {1,2,3,4}
# B = {3,4,5,6}
# C=A-B       # OR WE CAN WRITE A.defrence(b).   # means the iteam that in A but not in B
# D=B.difference(A)
# print("A-B:",C)
# print("B-A:",D)

#OUTPUT: A-B: {1, 2}
#OUTPUT: B-A: {5, 6}
#===================================================================================================================================
# *SOLUTION :

# 8. PROBLEM  : Find the difference between the two sets (A and B) and update in A. 

#===================================================================================================================================
# *SOLUTION :    use difference_update() functon

# A = {1,2,3,4,5,8,9}
# B = {3,4,5,6,10,11}
# A.difference_update(B)       #THIS FUNCTION TAKE THE DIFFERENCE AND STORE IN A
# print(A)

#OUTPUT: {1, 2, 8, 9}
#===================================================================================================================================

# 9. PROBLEM  : Find the symmetric difference of sets a and b. 

#===================================================================================================================================
# *SOLUTION : using of difference(-) and .symmetric_difference_update() function

# A = {1,2,3,4,5,8,9}
# B = {3,4,5,6,10,11}
# print("A:",A)
# print("B:",B) 
# A_diff_B = A-B                      # <=======  the iteam belonging in the list A but not in B
# print("A-B:",A_diff_B)
# B_diff_A=B-A                        # <=======  the iteam belonging in the list B but not in A
# print("B-A:",B_diff_A)
# A.symmetric_difference_update(B)    # <=======  the iteam belonging in the list A but not in B AND  B but not in A TOGETHER IN A ONE LIST
# print("SYMMETRIC:",A)

#output: A : {1, 2, 3, 4, 5, 8, 9}
#        B : {3, 4, 5, 6, 10, 11}
#      A-B : {8, 1, 2, 9}
#      B-A : {10, 11, 6}
# SYMMETRIC: {1, 2, 6, 8, 9, 10, 11}
#============================================================================================================================================================

# 10. PROBLEM  : Convert a list [1,2,2,3,4,4,5] into a set to remove duplicates. 

#============================================================================================================================================================
# *SOLUTION : using of set() and list() functions to convert
 
# A=[1, 2, 6, 2, 3, 6, 1, 8, 9, 10, 1]
# print("the list[] of  A:",A)
# A=set(A)                      #  <===============  first the list of A[] convert in to set of A{}   TO REMOVE THE DUPICATE VALUES
# print("the set of A: ",A)     #  <===============  The set{} not allowing duplicate value so THE SET A will not have any duplicate values
# A=list(A)                     #  <===============  Actually we want same set with non duplicate values so we need to econvert the set{} of A to the List
# print("the list of A without duplicate values:",A)     #  <===============  Then We print the A we will get the list of A without duplicate values


#output:            the list[] of A               : [1, 2, 6, 2, 3, 6, 1, 8, 9, 10, 1]
#                   the set of A                  : {1, 2, 3, 6, 8, 9, 10}
#                   list of  A without duplicates : [1, 2, 3, 6, 8, 9, 10]
#============================================================================================================================================================

#11. PROBLEM  : Given set1 = {10, 20, 30} and set2 = {20, 40, 50}, update set1 with all elements from set2. 

#============================================================================================================================================================
# *SOLUTION :      using of the union function

# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# set1 = set1.union(set2)
# print(f"{set1} union {set2} : {set1}")

#output: {50, 20, 40, 10, 30} union {40, 50, 20} : {50, 20, 40, 10, 30}
#============================================================================================================================================================

#12. PROBLEM  : Check whether set1 is a subset or superset of set2 

#============================================================================================================================================================
# *SOLUTION :      using of issubset()  and issuperset() functions

# set1={1,2,4,5,6,7,8}
# set2={7,8,6}
# if set1.issubset(set2):
#     print(f"set1:{set1} is a subset of set2:{set2}")
# elif set1.issuperset(set2):
#     print(f"set1:{set1} is a SUPERSET of set2:{set2}")
# else:
#     print(f"set1: {set1} is not a subset or superset of set2: {set2}")

#output: set1:{1, 2, 4, 5, 6, 7, 8} is a SUPERSET of set2:{8, 6, 7}
#============================================================================================================================================================

#13.PROBLEM  : Remove all elements from a set using .clear().

#============================================================================================================================================================
# *solution : use of .clear() function

# setToClear={1, 2, 4, 5, 6, 7, 8}
# print("set BEFORE DELETING THE VALUES   : ",setToClear)
# setToClear.clear()
# print("set AFTER THE CLEAR FUNCTION CALL: ",setToClear)

#output  : set BEFORE DELETING THE VALUES   :  {1, 2, 4, 5, 6, 7, 8}
#          set AFTER THE CLEAR FUNCTION CALL:  set()   ===============================> see the list is empty after using .clear() function
#============================================================================================================================================================

#14.PROBLEM  : Given a list of numbers [1,2,3,4,5,6,2,3,1], print the elements that appear more than once using a set..

#============================================================================================================================================================
# solution : we can create two sets one for unique values and one for duplicate values.
# Then we can iterate through the list and check if the value is already in the unique set.
# If it is, we add it to the duplicate set. If not, we add it to the unique set.
# WE CAN ALSO USE THE COUNT() FUNCTION
#*AND ALSO WE CAN USE A EMPTY LIST TO STORE THE DUPLICATE VALUES AND THEN CONVERT IT INTO A SET TO REMOVE THE DUPLICATE VALUES.*
#*BUT IT TAKE MORE TIME THAN THE ABOVE METHOD.*

# lst= [1,2,3,4,5,6,2,3,1]
# setlst=set()
# dupli=set()
# for i in lst:
#     if i in setlst:
#         dupli.add(i)
#     else:
#         setlst.add(i)
# print(dupli)

#output: {1, 2, 3}
#============================================================================================================================================================

#15.PROBLEM  :  Write a Python program to find elements present in only one of two given sets.

#============================================================================================================================================================
#SOLIUTION : store A-B(difference) in C and  B-A in D and UNION C and D. 
#            hihihihiii FOR THIS deficult OPERATION., 
#            SIMPLY WE HAVE symmetric_difference() function.   woww....!!!
#            WE CAN EASLY SOLVE THE PROBLEM WITH symmetric_difference() function as follows 

# A={1, 2, 3, 4}
# B={3, 4, 5, 6}
# symm=A.symmetric_difference(B)
# print(symm)

# output: {1, 2, 5, 6}
#============================================================================================================================================================

#16.PROBLEM  :   Combine multiple sets: {1,2}, {3,4}, {5,6} into a single set.

#============================================================================================================================================================
#solution: is there TWO WAys 1. use union(|): like >>>>> a=a|b|c <<<< 
# or SIMPLY >>>> a.update(b,c) <<<< this is simplest,easy and better

# a={1, 2}
# b={3, 4}
# c={5, 6}
# a.update(b,c)
# print(a)

#output: {1, 2, 3, 4, 5, 6}
#============================================================================================================================================================

#17.Given two sets {1,2,3} and {3,4,5}, write a program that prints “Disjoint” if the sets have  no elements in common, otherwise “Not Disjoint”.

#============================================================================================================================================================
#solution:  to check or take comon elemnts of sets 
# we can use 'intersection()' function

# s1={1, 2, 3}
# s2={3, 4, 5}

# if s1.intersection(s2):
#     print(""""THERE IS A COMON ELEMENTS IN THIS LISTS SO PRINTING "Disjoint" """)
# else:
#     print("""THERE IS NO COMON ELEMENTS IN THIS LISTS SO PRINTING "NOt Disjoint" """)

# output:"THERE IS A COMON ELEMENTS IN THIS LISTS SO PRINTING "Disjoint" 
#============================================================================================================================================================

#18. Write a Python program to count the number of unique words in a sentence using sets.

#============================================================================================================================================================
# solution: Usually, in programming questions, unique words means distinct words (ignoring duplicates), not "words that appear only once.

# s = "i love python and i love css and i love cpp"
# lst=s.split()
# unique_words=set(lst)
# print(unique_words)
# print("count:",len(unique_words))


#output: {'python', 'love', 'css', 'i', 'and', 'cpp'}
        #  count: 6
#============================================================================================================================================================

#19. Given set1 = {'a', 'b', 'c'} and set2 = {'b', 'c', 'd'}, 
#       create a new set containing only items unique to each set.

#============================================================================================================================================================
# solution: 

# set1 = {'a', 'b', 'c'}
# set2 = {'b', 'c', 'd'}
# set3 = set1.symmetric_difference(set2)
# print(set3)

#output: {'a', 'd'}





# #=======================================================================================================================================


                    #PRINT UNIQUE ELEMNT IN THE LISt LST=[6,9,5,1,8,5,8,9,2,11,3,2,1,3,4,5,9,6,10,4,8,11,12,12,10]


# #========================================================================================================================================
lst=[6,9,5,1,8,5,8,9,2,11,3,2,1,3,4,5,9,6,10,4,8,11,1543,12,12,10]
count=0
for i in range(0,len(lst)):
    count=0
    for j in lst:
        if lst[i]==j:
            count+=1
            if count>1:
                break
    if count==1:
        print(lst[i])
        break
else:
    print("NO UNIQUE ITEAM IN THIS LIST")











# 14. Create a frozen set from list [1,2,3,4]. Try adding a new element—observe the error.
# 15.
# 16. 
# 17. 
# 18.
# 19. Write a Python program to count the number of unique words in a sentence using sets.
# 20.