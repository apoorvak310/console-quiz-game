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
attempted = unattempted = score = 0

def print_opt(l):
    for i,o in enumerate(l):
        print(chr(ord('a') + i),".",o)
    print("Skip")

def check_answer(a,key):
    if a == quiz[key]['answer']:
        return True

def result(f:bool):
    global score
    if f == True:
        score += 1
    return score

def ask_again(st):
    if st == 'yes':
        return True
    elif st == 'no':
        return False
    else:
        c = input("Choose any one - Yes/No").strip().lower()
        return ask_again(c)

def play_game(quiz):
    global attempted
    global unattempted
    for k,v in quiz.items():
        i = 1
        print(i,')',k)
        i += 1
        print_opt(v["options"])
        ans = input("Answer__").strip().lower()
        if ans in ['a','b','c','d']:
            flag = check_answer(ans, k)
            attempted += 1
            scr = result(flag)
        elif ans == 'skip':
            unattempted += 1
            continue
        elif ans == 'e':
            fl = ask_again(ans)
            if fl == False:
                print("Exited")
                break
            elif fl == True:
                continue
        else:
            print("Enter a valid option")
    return scr

print(f"Total Questions: {len(quiz)}")
choice = input("Start the game..? (Type Yes (or) No) ").strip().lower()
if choice == "no":
    print("Okayy, see you next time...")
elif choice == "yes":
    # print("Your time starts now ... if you want to exit, press E")
    # start_time = time.time()
    score = play_game(quiz)
    # end_time = time.time()
    # total_seconds = end_time - start_time
    # minutes = int(total_seconds // 60)
    # seconds = int(total_seconds % 60)
    print("Quiz completed!")
    print(f"Total Questions Attempted: {attempted}\nTotal questions unattempted: {unattempted}")
    print(f"Your total Score is {score}/{len(quiz)}")
   
while True:
    again = input("Want to try again? (Yes/No) ").strip().lower()
    f = ask_again(again)
    if f == False:
        print("Exited")
        break
    elif f == True:
        play_game(quiz)
    #print(f"Total time taken: {minutes}.{seconds:02d} minutes")
else:
    print("Sorry can't get you :(")

    
'''leaving this at exit functioning'''
