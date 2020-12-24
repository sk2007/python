import random  # importing random
animals = ['lion', 'tiger', 'bear', 'owl', 'frog', 'toucan', 'monkey', 'shark', 'zebra', 'wolverine']  # animals
animals_chars = {'lion': ['mane', 'teeth', 'pride', 'Africa', 'predator'],
'tiger': ['stripes', 'fur', 'endangered', 'cat', 'claws'],
'bear': ['hibernates', 'North America', 'Brown', 'Fur', 'Strong'],
'owl': ['hoot', 'nocturnal', 'flies', 'big eyes', 'eats mice'],
'frog': ['pond', 'green', 'tongue', 'amphibian', 'eats flies'],
'toucan': ['rainbow', 'long beak', 'South America', 'tropical', 'wings'],
'monkey': ['eats bananas', 'trees', 'tail', 'swing', 'primate'],
'shark': ['ocean', 'dangerous', 'cartilege', 'sharp teeth', 'fins'],
'zebra': ['stripes', 'black and white', 'africa', 'safari', 'hoofs'],
'wolverine': ['vicious', 'skunk bear', 'brown', 'small', 'fast']}  # used for guesses

try:
    f1 = open('users+scores.txt', 'r+')  # opening the file
except FileNotFoundError:
    f1 = open('users+scores.txt', 'x')
    f1.close()
    f1 = open('users+scores.txt', 'r+')
text = f1.readlines()  # reading the data
f1.close()
scores = {}
for line in text:
    userdata = line.split()
    if userdata != []:
        scores[userdata[0]] = userdata[1] # getting the score


def intro():
    print("Let's play an animal guessing game!")
    print("Each turn I will give you a characteristic about an animal.")
    print("You have 5 guesses to get 100 points. If you don't, you lose 50 points.")
    name = input('Enter your name: ')
    if name in scores:
        point = scores[name] # if you already played
    else:
        point = 0
    def score(point, name_): # global variable
        global points, name
        points = int(point)
        name = name_
    score(point, name)

def game():    
    global animal, curr_clue, curr_ani_list, guess, points, name
    play = True  # check if elligible to play
    while (play):
        turns = 1
        animal = random.choice(animals)
        curr_clue = random.choice(animals_chars[animal])
        print("---------------------------------------------------")
        print('Your current score is: ' + str(points))
        print("\nGuess the animal I'm thinking of.")
        print("The first letter is: ", animal[0])
        print(curr_clue)
        curr_ani_list = animals_chars[animal]
        curr_ani_list.remove(curr_clue)
        guess = input('\nWhat animal am I thinking of? ').lower()   
        if guess == animal:  # checking if first attempt is right
            points = int(points)
            points += 100
            cont = input(f"\nCongrats! You earned 100 points in this turn!\nYou now have: {str(points)} points.\n\nWould you like to continue? Type y for yes and n for no: ")
            if cont.lower() != 'y':
                play = False
                break
        
        while guess != animal:
            if turns <= 4:  # check for correctness after first wrong
                print('\nSorry, here is another clue:')
                curr_clue = random.choice(curr_ani_list)
                print(curr_clue)
                curr_ani_list.remove(curr_clue)
                guess = input('\nWhat animal am I thinking of? ').lower()
                turns += 1
                if guess == animal:  # checking to see if correct
                    points = int(points)
                    points += 100
                    cont = input(f"\nCongrats! You earned 100 points in this turn!\nYou now have: {str(points)} points.\n\nWould you like to continue? Type y for yes and n for no: ")
                    if cont.lower() == 'n':  # whether you would like to continue or not
                        play = False
                        break
            else: # when you use all attempts
                print('\nOops no more clues for you! Sorry you lose 50 points')
                points = int(points)
                points -= 50
                print("The animal was", animal + '.')
                print(f"You now have: {str(points)} points.")
                print('This turn will now end.')
                print('\nType y to replay and n to quit')
                opt = input()
                if opt.lower() == 'n': # whether you would like to continue or not
                    play = False
                break    
            
def farewell():  # closing game
    global name, points
    scores[name] = str(points)
    f1 = open('users+scores.txt', 'w')
    for u in scores:
        f1.write(u + ' ' + scores[u] + '\n') # writing user scores and name to file
    f1.close()
    print('\n---------------------------------------------------\n')
    print(f"Your score: {str(points)}")
    print('Bye! Thanks for playing!')

intro()
game()
farewell()
