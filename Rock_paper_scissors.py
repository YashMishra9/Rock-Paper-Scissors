import random

num=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if num not in [0,1,2]:
    print("Invalid option!")
    exit()
if  num==0:
    print(rock)
elif num==1:
    print(paper)
elif num==2:
    print(scissors)


print("Computer chose:")
computer_choice= random.randint(0,2)
RPS=[rock,paper,scissors]
print(RPS[computer_choice])

if num==computer_choice:
    print("That's a draw")
elif ((num==0 and computer_choice==1) or
            (num==1 and computer_choice==2) or
                    (num==2 and computer_choice==0)):
                            print("You lose mate!")


elif ((num==1 and computer_choice==0) or
             (num==2 and computer_choice==1)
                     or (num==0 and computer_choice==2)):
                                print("Congrats!! You've won")

else:
    print("Nahhhh!!!! You're pressing the wrong buttons mate")
