import random

print("Welcome to this Dice Simulator")

def roll_dice():
    while True:
        try:
            number_of_dice = int(input('Enter number of dice 🎲 (1, 2, or 3): '))
            print("****************************")
            
            if number_of_dice in [1, 2, 3]:
                dice_values = [random.randint(1, 6) for _ in range(number_of_dice)]
                print('Rolled values:', dice_values)
                print("********************")
                
                while True:
                    roll_again = input("Roll again? (y/n): ")
                    print("*******************")
                    if roll_again.lower() == 'y':
                        break
                    elif roll_again.lower() == 'n':
                        print('Thanks for playing!👋')
                        return
                    else:
                        print("Invalid Input. Please enter 'y' or 'n': ")
                        print("****************************************")
            else:
                print('Please enter a valid number of dice (1, 2, or 3): ')
                print("****************************************")
        
        except ValueError:
            print('Please enter a valid number(1, 2, 3).')
            print("*************************************")

roll_dice()
