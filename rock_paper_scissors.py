import random

print("Rock Paper Scissors Game")
print("-------------------------")

user_score = 0
computer_score = 0
tie_score = 0

while True:
    print("\nChoose:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        user = "rock"
    elif choice == "2":
        user = "paper"
    elif choice == "3":
        user = "scissors"
    else:
        print("Invalid choice!")
        continue

    computer = random.choice(["rock", "paper", "scissors"])

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
        tie_score += 1

    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print("Your Score:", user_score)
    print("Computer Score:", computer_score)
    print("Ties:", tie_score)

    again = input("\nPlay again? (yes/no): ").lower()

    if again != "yes":
        break

print("\nFinal Score")
print("Your Score:", user_score)
print("Computer Score:", computer_score)
print("Ties:", tie_score)
print("Thank you for playing!")
