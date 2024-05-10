# Exercise 9.3
# Ryan Calles
# CIS 129
# Collects student name and grades for three exams and writes results to csv file

# Import CSV
import csv

# Asks the user for student's first name, last name, and three exam grades
def get_student_info():

  first_name = input("Enter student's first name: ")
  last_name = input("Enter student's last name: ")
  exam1 = int(input("Enter exam 1 grade: "))
  exam2 = int(input("Enter exam 2 grade: "))
  exam3 = int(input("Enter exam 3 grade: "))
  return {
      "first_name": first_name,
      "last_name": last_name,
      "exam1": exam1,
      "exam2": exam2,
      "exam3": exam3,
  }

# Writes student info to CSV file
def write_to_csv(student_info):
 
  with open('grades.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
      student_info["first_name"],
      student_info["last_name"],
      student_info["exam1"],
      student_info["exam2"],
      student_info["exam3"],
    ])

# Main function that collects student info, writes to CSV, and asks user if they want to continue
def main():
  
  while True:
    student_data = get_student_info()
    write_to_csv(student_data)
    choice = input("Enter another student? (y/n): ").lower()
    if choice != 'y':
      break

main()