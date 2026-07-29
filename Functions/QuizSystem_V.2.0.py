

# ==========================================================
#               QUIZ MANAGEMENT SYSTEM
#                    PART - 1
# ==========================================================

# ---------------- GLOBAL VARIABLES ---------------- #
import os
questions = {}
options = {}
answer_key = {}
participants = {}

QUIZ_PASSWORD = "student123"
MASTER_PASSWORD = "520"

# ---------------- FUNCTIONS ---------------- #

def line():
    print("=" * 60)


def add_question(q_no):
    """
    Create one question with four options and correct answer.
    """
    os.system('cls')
    print(f"\nQUESTION {q_no}")

    question = input("Enter Question : ").strip()

    option = {}

    for ch in "ABCD":
        option[ch] = input(f"Option {ch}: ").strip()

    while True:

        answer = input("Correct Option (A/B/C/D): ").upper()

        if answer in option:
            break

        print("Invalid option! Choose A, B, C or D.")

    return question, option, answer


# ------------------------------------------------------ #

def create_quiz():

    questions.clear()
    options.clear()
    answer_key.clear()

    while True:

        try:
            os.system('cls')
            total = int(input("\nTotal number of questions❓: "))

            if total > 0:
                break

            print("Number should be greater than zero.")

        except ValueError:
            print("Please enter a valid number.")

    for i in range(1, total + 1):

        q, op, ans = add_question(i)

        questions[i] = q
        options[i] = op
        answer_key[i] = ans

    print("\nQuiz Created Successfully✅")


# ------------------------------------------------------ #

def conduct_quiz():

    if not questions:
        print("\nQuiz has not been created yet.")
        return

    while True:
        os.system('cls')
        name = input("\nEnter Your Name : ").strip().title()

        if name == "":
            print("Name cannot be empty.")

        elif name in participants:
            print("This participant already attended the quiz...!")

        else:
            break

    answers = {}

    score = 0
    os.system('cls')
    line()
    print(f"Welcome {name}")
    line()

    for q_no in questions:
        # os.system('cls')
        print(f"\nQ{q_no}. {questions[q_no]}")

        for key, value in options[q_no].items():
            print(f"{key}. {value}")

        while True:

            ans = input("Your Answer : ").upper()
            showAns(q_no,ans)
            input("\npress enter ↵ key for the next qustion")

            if ans in "ABCD":
                break

            print("Please enter A/B/C/D only.")

        answers[q_no] = ans

        if ans == answer_key[q_no]:
            score += 5

    participants[name] = {
        "answers": answers,
        "score": score
    }
    os.system('cls')
    line()
    print(f"Quiz Completed!")
    print(f"Your Score : {score}/{len(questions)*5}")
    line()


# ------------------------------------------------------ #

def show_scoreboard():

    if not participants:
        print("\nNo participants yet.")
        return

    ranking = sorted(
        participants.items(),
        key=lambda x: x[1]["score"],
        reverse=True
    )
    os.system('cls')
    line()
    print("SCORE BOARD")
    line()

    for rank, (name, data) in enumerate(ranking, start=1):

        print(
            f"{rank}. {name:<20} "
            f"{data['score']}/{len(questions)*5}"
        )

    top_score = ranking[0][1]["score"]

    winners = []

    for name, data in ranking:

        if data["score"] == top_score:
            winners.append(name)

    line()
    print("Winner(s):", ", ".join(winners),"🥇")
    print(f"Highest Score : {top_score}/{len(questions)*5}")
    line()


# ------------------------------------------------------ #
def showAns(qno,ans):
    if answer_key[qno]==ans:
        print("congrats...✅ correct answer keep going.👍!")
    else:
        print(f"\nWRONG ANSWER..❌😑!\n\nthe correct answer is {answer_key[qno]}✅ ")


def show_answers():

    if not questions:
        print("Quiz not created.")
        return

    line()
    print("ANSWER KEY")
    line()

    for q_no in questions:
            print(f"Q{q_no}. "f"{questions[q_no]}")

            print()

def edit_qustion():

    print("total qustions are folows...\n")
    line()
    for qno,question in questions.items():
        print(f"{qno}.{question}\n")

    qn=int(input("enter the qustion number which you want to edit:"))
    # questions.pop(qn)
    new_que=input("enter new the qustion you want to add:")
    questions[qn]=new_que
    for choice in 'ABCD':

        options[choice] = input(f"Option {choice}: ").strip()


    # for qno,question in questions.items():                    SHOULD WORK IN IT
        print(f"{qno}.{question}\n")
        print(f"{options[qno]}")


#=-------=-------------------=----------------=-----------===============---------------===-----------
c=100
while c!=3:
    if c==1:
        for i in range(2,-1,-1):
            pw=input("PASSWORD:")
            if pw!=QUIZ_PASSWORD:
                print(f"WRONG PASSWORD.....❌😑!\n {i} attempt left")
            else:
                conduct_quiz()
                break
    elif c==2:
        for i in range(3):
            pw=input("PASSWORD:")
            if pw!=MASTER_PASSWORD:
                print(f"WRONG PASSWORD.....❌😑!\n {2-i} attempt left")
            else:
                os.system('cls')
                print("""\n\n1.CREATE QUIZ\t2.CONDUCT QUIZ\t 3.SHOW SCORE_BOARD\t 4.EDIT_QUSTIONS\t 0.EXIT""")
                cho=int(input("\n\n\nSELECT THE OPTION:"))
                if cho==1:
                    os.system('cls')
                    create_quiz()
                elif cho==2:
                    conduct_quiz()
                elif cho==3:
                    show_scoreboard()
                elif cho==4:


                    edit_qustion()



                elif cho==0:
                    os.system('cls')
                    print("GOOD BYE....!!")
                    break
                else: 
                    print("WRONG CHOICE❌😑!!")
    elif c==0:
        print("GOOD BYE....👋!")
        break

    print("""\n\n1.PARTICIPANT🧑‍🎓          2.QUIZ_MASTER👨‍🏫        0.EXIT🏃‍♂️\n\n""")
    c=int(input("SELET YOUR ROLE(1/2/3):"))
    

                



    