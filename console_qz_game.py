import time
print("MATH QUIZZ")
quiz = {
    "What is 15 + 27?": {
        "options": ["32", "42", "52", "62"],
        "answer": "b"
    },

    "What is 9 * 8?": {
        "options": ["63", "72", "81", "64"],
        "answer": "b"
    },

    "What is 144 / 12?": {
        "options": ["10", "11", "12", "14"],
        "answer": "c"
    },

    "What is 25% of 200?": {
        "options": ["25", "40", "50", "75"],
        "answer": "c"
    },

    "What is 7²?": {
        "options": ["14", "42", "49", "56"],
        "answer": "c"
    },

    "What is 100 - 37?": {
        "options": ["53", "63", "73", "67"],
        "answer": "b"
    },

    "What is 3/4 of 80?": {
        "options": ["40", "50", "60", "70"],
        "answer": "c"
    },

    "If x + 15 = 32, what is x?": {
        "options": ["15", "17", "19", "21"],
        "answer": "b"
    },

    "What is the perimeter of a square with a side of 6 cm?": {
        "options": ["12 cm", "18 cm", "24 cm", "36 cm"],
        "answer": "c"
    },

    "What is 2³ + 5²?": {
        "options": ["27", "31", "33", "35"],
        "answer": "c"
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
