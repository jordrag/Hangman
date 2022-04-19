import random
answer = []

fail_count = 0

# database of words

words_data = {'animals': ['camel', 'rabbit', 'bear', 'dolphin', 'penguin', 'giraffe', 'sheep', 'goat', 'cow', 'wolf'],
              'cities': ['Varna', 'Sofia', 'London', 'Tokyo', 'Moscow', 'Washington', 'Amsterdam', 'New York'],
              'plants': ['potatoes', 'carrot', 'apple', 'orange']}


# function for choice
def choice(choice):
    while True:
        if choice == 1:
            key = "animals"
            break
        elif choice == 2:
            key = "plants"
            break
        elif choice == 3:
            key = "cities"
            break
        else:
            print('Make a choice: 1.Animals, 2.Plants, 3.Cities')
            choice = int(input())

    rnd_number = random.randrange(0, len(words_data[key]))

    word_choice = words_data[key][rnd_number]

    return word_choice


print('Make a choice: 1.Animals, 2.Plants, 3.Cities')
nmr = int(input())

word = choice(nmr)

for i in range(len(word)):
    print(" _ ", end="")
    answer.append("_")

# Comparison of  entered letter vs. letters of random chosen word for this game

while True:
    print()
    print("Ask a letter from the word: ")
    letter = str(input())
    guessed_right = 0
    for i in range(len(word)):
        if word[i] == letter:
            answer[i] = letter
            guessed_right += 1

# Drawing the hangman

    if guessed_right != 0:
        print("".join(answer))
        if "_" not in answer:
            print("You won!")
            break
    else:
        print("*" * fail_count)
        fail_count += 1
        if fail_count == 7:
            print("Game over! You lose!")
            break
