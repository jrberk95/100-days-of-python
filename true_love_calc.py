print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

combined_names = name1.lower() + name2.lower()

trueTotal = 0
loveTotal = 0

true = "true"
love = "love"

for letter in true:
  trueTotal += combined_names.count(letter)

for letter in love:
  loveTotal += combined_names.count(letter)

score = int(str(trueTotal) + str(loveTotal))

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

