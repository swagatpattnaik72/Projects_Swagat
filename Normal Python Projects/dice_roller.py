import random

def roll_dice():
    print("🎲 Rolling the dice...")
    result = random.randint(1, 6)
    print(f"You rolled a {result}!\n")

while True:
    user_input = input("Press Enter to roll the dice or type 'q' to quit: ")
    if user_input.lower() == 'q':
        print("Goodbye!")
        break
    roll_dice()
