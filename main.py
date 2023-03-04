from Student import Student
import csv

students = []

with open("Attendance.csv") as file:
  reader = csv.reader(file)
  for row in reader:
    students.append(Student(row[0], row[1], row[2], row[3], row[4]))

for student in students:
  print(student.attendedMeetings)


while True: 
  scan = input("Scan your barcode.")

  if scan == "exit": 
    break

  for student in students:
    if scan == student.studentID:
      student.attendedMeetings["Flag Routes"] = 2
      print("")
      print(student.firstName + "'s attendance record: ")
      print(student.attendedMeetings)
      print("")
      break




f = open("Attendance.csv", "w")

for student in students:
  row = student.studentID + "," + student.lastName + "," + student.firstName + "," + student.email + "," + str(student.attendedMeetings) + "\n"
  f.write(row)
 
f.close()



    

    