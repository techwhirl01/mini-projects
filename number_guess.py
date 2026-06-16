import random

num_to_guess = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1
        difference = abs(num_to_guess - guess)

        if guess < num_to_guess:
            print("Number is too low!")
            if difference <= 5:
                print("Very close!")
            elif difference <= 10:
                print("Close!")
            elif difference <= 20:
                print("Getting warmer!")
            else:
                print("Far away!")

        elif guess > num_to_guess:
            print("Number is too high!")
            if difference <= 5:
                print("Very close!")
            elif difference <= 10:
                print("Close!")
            elif difference <= 20:
                print("Getting warmer!")
            else:
                print("Far away!")

        else:
            print(f"Congratulations! You got the right answer in {attempts} attempts.")
            break

    except ValueError:
        print("Invalid input.")

