# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

total_height = 0
num_students = 0

for height in student_heights:
  total_height += height
  num_students += 1

avg_height = round(total_height / num_students)

print(f"total height = {total_height}\nnumber of students = {num_students}\naverage height = {avg_height}")