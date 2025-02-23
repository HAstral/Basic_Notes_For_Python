questions=("How many elements are there in periodic table? : ",
           "Which animal lays the biggest eggs?: ",
           "What is the most useful gas for living beings? : ",
           "How many planets are there in our solar system? :",
           "How many continents are there in the world? :")
options=(("A. 118","B. 119","C. 120","D. 121"),
         ("A. Ostrich","B. Hen","C. Sparrow","D. Pigeon"),
         ("A. Oxygen","B. Nitrogen","C. Carbon dioxide","D. Hydrogen"),
         ("A. 8","B. 9","C. 10","D. 11"),
         ("A. 5","B. 6","C. 7","D. 8"))
answers=("A","A","A","B","C")
guesses=[]
score=0
question_num=0

for quest in questions:
    print("----------------")
    print(quest)
    for opt in options[question_num]:
        print(opt)
    guess=input("Enter your answer(A,B,C,D): ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("Bingo! Correct answer.")
    else:
        print("Booo! You are noob.")
        print(f"Correct answer is {answers[question_num]}")
    question_num+=1
    
print("----------------")
print("     Results     ")
print("----------------")

print("Answers: ",end=" ")
for ans in answers:
    print(ans,end=" | ")
print()

print("Guesses: ",end=" ")
for guess in guesses:
    print(guess,end=" | ")
print()

score=int(score/len(questions) * 100 )
print(f"Your score is {score}%")