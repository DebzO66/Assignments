import random

input("welcome to rock, paper, scissors! press enter to start.")

user_score = 0
cpu_score = 0

while True:
 print()
 user_choice = input("rock, paper, scissors?").lower()

 while user_choice != "rock" and user_choice != "paper" and user_choice != "scissors": user_choice = input("invalid iput, please try again:").lower()


 random_num = random.randint(0,2)
 if random_num == 0:
  cpu_choice = "rock"
 elif random_num == 1:
  cpu_choice = "paper"
 elif random_num == 2:
  cpu_choice = "scissors"

 print()
 print("user_choice:", user_choice)
 print("computer's choice:", cpu_choice)
 print()

 if user_choice == "rock":
    if cpu_choice == "rock":
      print("it's a tie!")
    elif cpu_choice =="paper":
        print("you lost!")
        cpu_score += 1
    elif cpu_choice =="scissors":
        print("you win!")
        user_score +=1
 elif user_choice == "paper":
    if cpu_choice == "paper":
      print("it's a tie!")
    elif cpu_choice =="scissors":
        print("you lost!")
        cpu_score += 1
    elif cpu_choice =="rock":
        print("you win!")
        user_score += 1
 elif user_choice == "scissors":
    if cpu_choice == "scissors":
      print("it's a tie!")
    elif cpu_choice =="rock":
        print("you lost!")
        cpu_score +=1
    elif cpu_choice =="paper":
        print("you win!")
        user_score += 1

 print()  
 print("you have", user_score, "wins")
 print("computer", cpu_score, "wins")
 print()

 repeat = input("play again? (Y/N)").lower()
 while repeat != "n" and repeat != "y":
    repeat = input("invalid input, please try again:").lower()

 if repeat == "n":
     break
 print("..........")