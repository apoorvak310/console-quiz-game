# quiz = {
#     "What is the capital of India?": "delhi",
#     "What is 5 + 7?": "12",
#     "Which planet is known as the Red Planet?": "mars",
#     "What is the largest ocean on Earth?": "pacific ocean",
#     "Who wrote Romeo and Juliet?": "william shakespeare",
#     "How many continents are there?": "7",
#     "What is the chemical symbol for water?": "h2o",
#     "Which language is used to create web pages?": "html",
#     "What is the largest mammal in the world?": "blue whale",
#     "How many days are there in a leap year?": "366"
# }
# score = 0
# choice = input("Do you want to start the quiz? (y/n): ").strip().lower()
# if choice == 'n':
#     print("Okay, see you next time!!")
# elif choice == 'y':
#     for k,v in quiz.items():
#         print(k,end=" ")
#         ans = input("Answer...").lower()
#         if ans == quiz[k]:
#             score += 1
#             print(True)
#         elif ans in quiz[k].split():
#             print("Too close, but not correct")
#         else:
#             print("Wrong answer")
# else:
#     print("Enter valid input")
# print("You scored",score,"out of",len(quiz))

import time
print("MATH QUIZZ")
quiz = {
    "What is the capital of India?": {
        "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
        "answer": 'b'
    },

    "Which planet is known as the Red Planet?": {
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": 'b'
    },

    "What is 10 * 5?": {
        "options": ["15", "50", "100", "25"],
        "answer": 'b'
    },

    "Who wrote Romeo and Juliet?": {
        "options": ["William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"],
        "answer": 'a'
    },

    "How many continents are there?": {
        "options": ["5", "6", "7", "8"],
        "answer": 'c'
    }
}
score = 0
def print_opt(l):
    o = ord('a')
    for i in l:
        print(chr(o),".",end=" ")
        yield i
        o += 1

print(f"Total Questions: {len(quiz)}")
choice = input("Shall we start..? (Type Yes (or) No) ").strip().lower()
if choice == "yes":
    print("Your time starts now ... if you want to exit, press E")
    startTime = time.time()
    for k,v in quiz.items():
        print(k)
        for i in print_opt(v["options"]):
            print(i)
        ans = input("Answer...").strip().lower()
        if ans == v["answer"]:
            score += 1
            print("Correct!")
        elif ans == 'e':
            ch = input("Are you you want to sure to exit ? (yes/no) ").strip().lower()
            if ch == 'yes':
                break
            elif ch == 'no':
                pass
        else:
            print("Wrong answer. The correct answer is:", v["answer"])
    endTime = time.time()
    print(f"Your total Score out of {len(quiz)} is: {score}")
    print(f"Total time taken: {(endTime-startTime)//60} minutes")
elif choice == "no":
    print("Okayy, see you next time...")
else:
    print("Sorry can't get you :(")