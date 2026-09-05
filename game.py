import random
choices = ["rock","paper","scissors"]

user_score = 0
computer_score = 0

print("RROCK PAPER SCISSORS GAME 👾")
print("-----------------------------")

# Using Loop for the multiple choices

while True:
    user = input("\nEnter rock, paper, scissors or quit:").lower()

    # Exit Game 

    if user == "quit":
        break


    # Check Invalid input 
    if user not in choices:
        print("Invalid choice ❌Try Again.")
        continue


    # Computer chooses randomly 
    computer = random.choice(choices)
    print("YUU", user)
    print("computer", computer)


    # Results
    if user == computer:
        print("it's a Tie!")

    elif(
        (user == "rock" and computer == "scissors")
        or(user == "paper" and computer == "rock")
        or(user == "scissors" and computer == "paper")
    ):
        print("MUJSE BADHKAR KOI NHAI")
        user_score += 1

    else:
        print("Teri Aesi ki Tassi")
        computer_score += 1

    print(f"Score - Tumhara: {user_score} | Computer: {computer_score}")


print("\n============================")
print("        GAME OVER")
print("============================")

print(f"Final Score → You: {user_score} | Computer: {computer_score}")

if user_score > computer_score:
    print("🏆 You are the Winner!")

elif computer_score > user_score:
    print("💻 Computer is the Winner!")

else:
    print("🤝 Match Draw!")
