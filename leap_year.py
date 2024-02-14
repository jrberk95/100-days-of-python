year = int(input())

div_by_4 = year % 4 == 0
div_by_100_not_400 = year % 100 == 0 and year % 400 != 0
div_by_100 = year % 100 == 0

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else: 
    print("Leap year")
else: 
  print("Not leap year")