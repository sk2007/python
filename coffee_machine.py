water = 400
milk = 540
coffee = 120
money = 550
cups = 9

print('The coffee machine has: ')
print(str(water), 'of water')
print(str(milk), 'of milk')
print(str(coffee), 'of coffee beans')
print(str(cups), 'of disposable cups')
print(str(money), 'of money')

option = input('Write action (buy, fill, take, remaining, exit):\n')
while option != 'exit':
    if option == 'buy':
        print()
        type_want = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
        if type_want == '1':
            water_n = 250
            coffee_n = 16
            cups_n = 1
            if water > water_n and coffee > coffee_n and cups > cups_n:
                print('I have enough resources, making you a coffee!')
                print()
                water -= water_n
                coffee -= coffee_n
                cups -= cups_n
                money += 4
            else:
                if water < water_n:
                    print('Sorry, not enough water!')
                    print()
                elif coffee < coffee_n:
                    print('Sorry, not enough coffee beans!')
                    print()
                elif cups < cups_n:
                    print('Sorry, not enough disposable cups')
                    print()
        elif type_want == '2':
            water_n = 350
            milk_n = 75
            coffee_n = 20
            cups_n = 1
            if water > water_n and milk > milk_n and coffee > coffee_n and cups > cups_n:
                print('I have enough resources, making you a coffee!')
                print()
                water -= water_n
                milk -= milk_n
                coffee -= coffee_n
                cups -= cups_n
                money += 7
            else:
                if water < water_n:
                    print('Sorry, not enough water!')
                    print()
                elif milk < milk_n:
                    print('Sorry, not enough milk!')
                    print()
                elif coffee < coffee_n:
                    print('Sorry, not enough coffee beans!')
                    print()
                elif cups < cups_n:
                    print('Sorry, not enough disposable cups')
                    print()
        elif type_want == '3':
            water_n = 200
            milk_n = 100
            coffee_n = 12
            cups_n = 1
            if water > water_n and milk > milk_n and coffee > coffee_n and cups > cups_n:
                print('I have enough resources, making you a coffee!')
                print()
                water -= water_n
                coffee -= coffee_n
                milk -= milk_n
                cups -= cups_n
                money += 6
            else:
                if water < water_n:
                    print('Sorry, not enough water!')
                    print()
                elif milk < milk_n:
                    print('Sorry, not enough milk!')
                    print()
                elif coffee < coffee_n:
                    print('Sorry, not enough coffee beans!')
                    print()
                elif cups < cups_n:
                    print('Sorry, not enough disposable cups!')
                    print()
        print('The coffee machine has: ')
        print(str(water), 'of water')
        print(str(milk), 'of milk')
        print(str(coffee), 'of coffee beans')
        print(str(cups), 'of disposable cups')
        print(str(money), 'of money')
    elif option == 'take':
        print()
        print('I gave you $' + str(money))
        print()
        money -= money
    elif option == 'fill':
        print()
        morew = int(input('Write how many ml of water do you want to add: \n'))
        morem = int(input('Write how many ml of milk do you want to add: \n'))
        morec = int(input('Write how many grams of coffee beans do you want to add: \n'))
        morecups = int(input('Write how many disposable cups do you want to add: \n'))
        water += morew
        milk += morem
        coffee += morec
        cups += morecups
        print()
    elif option == 'remaining':
        print()
        print('The coffee machine has: ')
        print(str(water), 'of water')
        print(str(milk), 'of milk')
        print(str(coffee), 'of coffee beans')
        print(str(cups), 'of disposable cups')
        print(str(money), 'of money')
        print()
    option = input('Write action (buy, fill, take):\n')

if option == 'exit':
    mylist = []
    mylist.append(option)
    for i in mylist:
        break
