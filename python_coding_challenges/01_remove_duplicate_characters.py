st=input("enter sentance:").lower()
nw=""
nw=st[0]
for ch in st:
    if ch not in nw:
        nw+=ch
print(nw)

#output: enter sentance:programming              
#        progamin