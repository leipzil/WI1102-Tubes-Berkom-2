import random

def linear_search(target, array, col=None):
    if col == None:
        for x in range(len(array)):
            if target == array[x]:
                return x
    else:
        for x in range(len(array)):
            if target == array[x][col]:
                return x
    return -1

flashcards = [["question 1", "answer 1"]] #2d array consisting of flashcards[[question, answer]]
while True:
    menu = int(input("""
===Menu===
1. Practice run
2. Add card
3. Delete card
4. View cards
5. End
Choice: """))
    if menu == 1:
        if flashcards:
            question_index = list(range(len(flashcards))) #to store available index for random
            wrong_index = [] #to store wrong numbers
            while question_index:
                print("")
                number = random.choice(question_index)
                print(flashcards[number][0])
                answer = input("Answer: ").strip().lower()
                while not answer:
                    answer = input("Answer: ").strip().lower()
                if answer == flashcards[number][1]:
                    print("Correct!")
                else:
                    print("Incorrect")
                    wrong_index.append(number)
                question_index.remove(number)
            while wrong_index:
                number = random.choice(wrong_index)
                print(flashcards[number][0])
                answer = input("Answer: ").strip().lower()
                if answer == flashcards[number][1]:
                    print("Correct!")
                    wrong_index.remove(number)
                else:
                    print("Incorrect!")
        else:
            print("You currently have no flashcards. Please add a flashcard first")
    elif menu == 2:
        question = input("Question: ").strip().lower()
        if linear_search(question, flashcards, 0) != -1:
            print("This question is already in your stack")
        else:
            answer = input("Answer: ").strip().lower()
            flashcards.append([question, answer])
    elif menu == 3:
        target = int(input("Which question number do you want to delete? "))
        if 0 < target <= len(flashcards):
            del flashcards[target-1]
            print("Flashcard deleted")
        else:
            print("This question is not in your stack")
    elif menu == 4:
        for x in range(len(flashcards)):
            print(f"""
{x+1}. Question: {flashcards[x][0]}
   Answer: {flashcards[x][1]}""")
    else:
        break