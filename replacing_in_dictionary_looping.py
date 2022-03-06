student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
for name in student_scores:
    if student_scores[name] > 100:
        student_grades[name] = "invalid value"
    elif student_scores[name] > 90:
        student_grades[name] = "Outstanding"
    elif student_scores[name] > 80:
        student_grades[name] = "Exceeds expectations"
    elif student_scores[name] > 70:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

print(student_grades)
