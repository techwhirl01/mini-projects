import random

emojis = { 'r' : '🪨', 's' : '✂️', 'p' : '📄'}
choices = ('r', 'p', 's')

player_score = 0
computer_score = 0

while True:
    user_choice = input("rock, paper, or scissor? (r/p/s): ").lower()

    if user_choice not in choices:
        print("invalid choice!")
        continue

    computer_choice = random.choice(choices)

    print(f'you chose {emojis[user_choice]}')
    print(f'computer chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('tie!')
    elif ((user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 'r')):
        print('you win!')
        player_score += 1

    else:
        print('you lose!')
        computer_score += 1

    print(f"\nScore: You {player_score} - {computer_score} Computer")

    should_continue = input('continue? (y/n): ').lower()
    if should_continue == 'n':
        print("\nFinal Score")
        print(f"You: {player_score}")
        print(f"Computer: {computer_score}")
        print("Thanks for playing!")
        break
