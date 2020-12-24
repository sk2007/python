import random
def display(word, temp):
    displayString = ""
    for i in range(len(temp)):
        if temp[i] != '-':
            displayString += "-"
        else:
            displayString += word[i]
    return displayString
def checklives(lives):
    lives = list(lives)
    for i in lives:
        if i == 0:
            print('You are hanged!')
            break
words = ['supercalifragilisticexpialidocious', 'aardvark', 'butter', 'chicken', 'furry', 'python', 'java', 'kotlin', 'javascript']  # Write your code here
word = random.choice(words)
temp = word
chosen = word
lives = 8
print('H A N G M A N')
print('Inputs must contain only letters and be one character long.')
chosen = '-' * len(chosen)
displayString = chosen
for attempts in range(lives + len(word)):
    print('')
    print(display(word, temp))
    guess = input("Input a letter: ")
    if guess not in 'abcdefghijklmnopqrstuvwxyz' or len(guess) != 1:
        print('Input does not meet requirements')
    else:
        if guess in temp:
            position = temp.index(guess)
            temp = temp.replace(temp[position], '-')
            if temp == chosen:
                print()
                print('Congratulations! You have guessed the word ' + word + '!')
                print("Thanks for playing!")
                print("We'll see how you did in the next stage")
                break
        elif guess not in temp:
            print('No such letter in the word')
            lives -= 1
            if lives == 0:
                print()
                print('The word was ' + word + '.')
                print("Thanks for playing!")
                break
            else:
                continue
