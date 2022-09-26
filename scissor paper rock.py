import random

def user_input():
    user_choice=input("enter rock ,paper,scissor=")
    list=["rock","paper","scissor"]
    computer_choice=random.choice(list)
    return (check_result(user_choice,computer_choice))
   
def check_result(user , computer):
    print(f"you choose {user} and computer choose {computer} so")
    if user==computer:
         print("the game is tie!!!")
    elif user=="rock":
     if computer=="paper":
      print("you won the game!!")
    elif user=="rock":
     if computer=="scissor":
      print("you won the game!!")
    elif user=="scissor":
     if computer=="rock":
      print("you loose the game!!")
    elif user=="scissor":
     if computer=="paper":
      print("you loose the game!!")
    elif user=="paper":
     if computer=="rock":
      print("you won the game!!")
    elif user=="paper":
     if computer=="scissor":
      print("you loose the game!!")
    else:
      print("we love our world")


user_input()