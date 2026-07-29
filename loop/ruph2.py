
def quiz(name,ans):
    score=0
    data={}
    data[name]=ans
    anskey={1:'tiger',
            2:'Peacock',
            3:'Lotus',
            4:'mango',
            5:'Banyan Tree',
            6:'ganga',
            7:'Jana Gana Mana',
            8:'Vande Mataram ',
            9:'fishLion',
            10:'Wild Lion'}
    for i in range(1,11):
        if ans[i].lower()==anskey[i].lower():
            score+=1
    data[name]['score']=score
    return data

def score_board(name):

    print(main)
    top_sco=main[names[0]]['score']
    winner=name
    for name in names:
        if main[name]['score']>top_sco:
            winner=name
    print(f"THE WINNER OF THE QUIZ IS: mr.{winner} WITH THE SCORE OF {main[winner]['score']} ")
    print(f"score board of {winner} =>",main[winner])


q={1:" What is the national animal of India?",
  2: "What is the national bird of India?",
  3: "What is the national flower of India?",
  4: "What is the national fruit of India?",
  5: "What is the national tree of India?",
  6: "What is the national river of India?",
  7: "What is the national anthem of India?",
  8: "What is the national song of India?",
  9: "What is the national aquatic animal of India?",
 10: "What is the national heritage animal of India?"
}






        




main={}
names=[]
atmpt=3
while True:
    print(""" 1.PARTICIPANT
             2.QUIZ MASTER
             SELECT YOUR ROLE""")
    role=int(input("1 or 2:"))

    if role==1:
        psw=input("ENTER PASSWORD TO START THE QUIZ:")
        if psw=='student123':
            name=input("Name:")
            names.append(name)
            a={}
            for i in range(1,11):
                score=0
                print(q[i])
                ans=input(f"answer:")
                a[i]=ans
            main.update(quiz(name,a))
        else:
            if atmpt>1:
                atmpt-=1
                print(f"wrong password enterd...!!!!!  you have only {atmpt} left ")
            else:
                print("good bye..!!  you reached maximum number of attempt")
                break
    elif role==2:
        password=input("Enter Quiz Master Password For SHOWING ENTIRE SCORE BOARD AND THE WINNER:")
        if password=='520':
            score_board(name)
        else:
            print("wrong password enterd")
    









