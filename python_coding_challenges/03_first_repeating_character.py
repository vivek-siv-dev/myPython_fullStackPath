st=input("sentance:")
fq={}
found=False
for ch in st:
    if ch==" ":
        continue
    if ch not in fq:
        fq[ch]=1
    else:
        fq[ch]+=1
for ch in st:
    if fq[ch]>1:
        print("The first repeating charecter in this word is :",ch)
        found=True
        break
if not found:
    print("there is no repeating char....!!!!")

# output: 
# sentance:  programming
# The first repeating charecter in this word is : r
