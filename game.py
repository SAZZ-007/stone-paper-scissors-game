import random

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

#Write your code below this line 👇

choice = int(input("enter rock,paper or siccessors,0,1,2 respectively are the values "))

computer_choice =random.randint(0,2)
print(computer_choice)

if choice == 0 and computer_choice ==1:
  print("computer win")

if choice == 1 and computer_choice == 0:
 print("computer win")

if choice ==0 and computer_choice ==2:
 print("user win")

if choice == 1 and computer_choice == 2:
 print("userwin")

if choice == 2 and computer_choice == 0:
 print("computer win")

if choice == 2 and computer_choice == 1:
 print("userwin")

if choice == computer_choice:
 print("draw")
