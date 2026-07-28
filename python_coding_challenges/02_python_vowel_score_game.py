
vowels="aeiou"
total=0
print("--"*54)
print(f"\nRULES: * THE SCORE WILL BE CALCULATED IN THE BASIS OF NUMBER OF VOEWLS PRESENT IN THE WORD.{"\n"}       * IF THE COUNT OF VOWELS IS AN EVEN NUMBER THE SORE WILL BE 4! {"\n"}       * FOR  ODD NUMBER THE SCORE WILL BE 2")
print("--"*54)
s=input("enter the sentance:").lower()
words=list(s.split())
score_bord={}
vw={}
for word in words:
    vowel_count=0
    for letter in word:
        if letter in vowels:
            vowel_count+=1
    vw[word]=vowel_count
    if vowel_count%2==0 and vowel_count !=0:
        score=4
        total+=score
        score_bord[word]=score
    elif vowel_count!=0:
        score=2
        total+=score
        score_bord[word]=score
print("--"*54)
print("WORD \t\t\t","No.OF.WOVELS\n")
for key in vw:
    print(f"word:{key}     number of vowels: {vw[key]}")
print("\nwords with score ==>",score_bord)
print("total score=",total)