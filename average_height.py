student_heights = input("Input a list of student heights \n").split()

sum_heights = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  sum_heights += student_heights[n]

total_students = len(student_heights)

average_height = round(sum_heights / total_students)
print(average_height)