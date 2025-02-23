#String
# word="APPLE"
# letter= input("Guess a letter:").upper()

# if letter in word:
#     print(f"Right! {letter} is in the word.")
# elif letter not in word:
#     print(f"Sorry! {letter} is not in the word.")

#Tuple
# students={"John","Jane","Joe","Jack","Jill"}
# student=input("Enter a student name: ")

# if student in students:
#     print(f"{student} is in the class.")
# else:
#     print(f"{student} is not in the class.")

#Dictionary
# Grades={"John":"A","Jane":"B",
#         "Joe":"C","Jack":"D",
#         "Jill":"F"}
# student=input("Enter a student name: ")
# if student in Grades:
#     print(f"{student}'s Grade is {Grades[student]}")
# else:
#     print(f"{student} is not in the class.")

#variable
email=input("Enter your email: ")
if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")