
# vowels="aeiou"
# total=0
# print("--"*54)
# print(f"\nRULES: * THE SCORE WILL BE CALCULATED IN THE BASIS OF NUMBER OF VOEWLS PRESENT IN THE WORD.{"\n"}       * IF THE COUNT OF VOWELS IS AN EVEN NUMBER THE SORE WILL BE 4! {"\n"}       * FOR  ODD NUMBER THE SCORE WILL BE 2")
# print("--"*54)
# s=input("enter the sentance:").lower()
# words=list(s.split())
# score_bord={}
# vw={}
# for word in words:
#     vowel_count=0
#     for letter in word:
#         if letter in vowels:
#             vowel_count+=1
#     vw[word]=vowel_count
#     if vowel_count%2==0 and vowel_count !=0:
#         score=4
#         total+=score
#         score_bord[word]=score
#     elif vowel_count!=0:
#         score=2
#         total+=score
#         score_bord[word]=score
# print("--"*54)
# print("WORD \t\t\t","No.OF.WOVELS\n")
# for key in vw:
#     print(f"{key}\t\t\t\t===>\t\t{vw[key]}")
# print("\nwords with score ==>",score_bord)
# print("total score=",total)


# st=input("sentance:")
# fq={}
# found=False
# for ch in st:
#     if ch==" ":
#         continue
#     if ch not in fq:
#         fq[ch]=1
#     else:
#         fq[ch]+=1
# for ch in st:
#     if fq[ch]>1:
#         print(ch)
#         found=True
#         break
# if not found:
#     print("there is no repeating char....!!!!")



# st=input("enter sentance:").lower()
# st=st.split()
# lw=st[0]
# for w in st:
#     if len(w)>len(lw):
#         lw=w
# print(lw)
# print(len(lw))


# st=input("enter sentance:").lower()
# nw=""
# nw=st[0]
# for ch in st:
#     if ch not in nw:
#         nw+=ch
# print(nw)

# n=int(input("enter the limits:"))
# count=0
# if n<2:
#     print("there is no prime number in this range.!")
# else:
#     for i in range(1,n+1):
#         count=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 count+=1
#         if count==2:
#             print(i)











