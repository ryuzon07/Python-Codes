students = {}
while True:
 print("\nStudent Record Keeper")
 print("1. Add a student record")
 print("2. Update a student record")
 print("3. View all student records")
 print("4. Delete a student record")
 print("5. Exit")
choice = int(input("Enter your choice: "))
if choice == 1:
 name = input("Enter the student’s name: ")
 grades = input("Enter the student’s grades (comma-separated):
 ").split(",")
 attendance = int(input("Enter the student’s attendance (%): "))
 students[name] = {"Grades": grades, "Attendance": attendance}
 print("Student record added!")
elif choice == 2:
 name = input("Enter the student’s name to update: ")
if name in students:
 grades = input("Enter the updated grades (comma-separated):
 ").split(",")
 attendance = int(input("Enter the updated attendance (%): "))
 students[name] = {"Grades": grades, "Attendance": attendance}
 print("Student record updated!")
else:
 print("Student not found!")
elif choice == 3:
 print("Student Records:")
 for name, record in students.items():
 print(f"Name: {name}, Grades: {', '.join(record['Grades'])},
 Attendance: {record['Attendance']}%")
elif choice == 4:
 name = input("Enter the student’s name to delete: ")
if name in students:
 del students[name]
 print("Student record deleted!")
else:
 print("Student not found!")
elif choice == 5:
 print("Exiting Student Record Keeper.")
break
else:
 print("Invalid choice! Please try again.")  
