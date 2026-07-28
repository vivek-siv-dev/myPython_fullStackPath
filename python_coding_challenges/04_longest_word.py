st=input("enter sentance:").lower()
st=st.split()
lw=st[0]
for w in st:
    if len(w)>len(lw):
        lw=w
print("Longest word in this sentace is:",lw)
print("with :",len(lw)," letters")

# #output: enter sentance :  i love python programming
#
#         Longest word in this sentace is: programming
#         with 11 letters