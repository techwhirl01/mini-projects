import random
#generate a random number
num_to_guess = random.randint(1, 100)
#loop
attempts = 0

while True:
    try:
    #ask the user to make a guess
        guess = int(input("guess the no. between 1 to 100: "))
        #if no. is not in range.
        if guess < 1 or guess > 100:
            print ("please enter a number between 1 and 100.")
            continue

        attempts +=1
        
        if guess < num_to_guess:
            print("no. is too low!")
        elif guess > num_to_guess:
            print("no. is too high!")
        else:
            print(f"congo!, you got the right answer in {attempts} attempts.")
            break
        
    except ValueError:
        print("invalid input")


