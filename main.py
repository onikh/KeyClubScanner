import Student

students = []

with open("test.csv") as file:
  for item in file:
    students.append(item.rstrip("\n"))

print(students)


    