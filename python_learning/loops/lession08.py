import random

sec_num = random.randint(1,100)
print("Welcome to Gussing-Game\n")
print("Enter a number between 1 to 100\n")

attempts=0

while True:
  guess = int(input("Enter your guess\n"))
  attempts +=1

  if guess<sec_num:
    print("Higer ! Try Aagain\n")
  elif guess>sec_num:
    print("Lower ! Try Again\n")
  else:
    print("Congratulation ! you are gussing the right number\n")
    print("Secret number",sec_num)
    print("Total attempts",attempts)
    break


