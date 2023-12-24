import csv

students = []

with open("File I-O/csv/students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], 
                         "home": row["home"]})
       
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")