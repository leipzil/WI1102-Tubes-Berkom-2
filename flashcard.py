import random

flashcards = [["question 1", "answer 1"]] #2d array consisting of flashcards[[question, answer]]
question_index = [0] #to store available index for random
wrong_a = []
while True:
    menu = int(input("""===Menu===
    1. Practice run
    2. Add card
    3. Delete card
    4. End
    Choice: """))
    if menu == 1:
        if flashcards:
            for x in range(len(flashcards)):
                number = random.choice(question_index)
                print(flashcards[number][0])
                answer = input("Answer: ").strip().lower()
                while not answer:
                    answer = input("Answer: ").strip().lower()
                if answer == flashcards[number][1]:
                    print("Correct!")
                else:
                    print("Incorrect")
                    wrong_a.append(flashcards[number])
                question_index.remove(number)
            while wrong_a:
                number = random.randint(0, len(wrong_a)-1)
                print(wrong_a[number][0])
                answer = input("Answer: ").strip().lower()
                if answer == wrong_a[number][1]:
                    print("Correct!")
                    del wrong_a[number]