cet_students = {"Alice", "Bob", "Charlie"}
jee_students = {"Bob", "David", "Eve"}
neet_students = {"Alice", "Eve", "Frank"}
while True:
 print("\nStudent Enrollment Manager")
 print("1. View all students in CET, JEE, or NEET")
 print("2. Union (students enrolled in any exam)")
 print("3. Intersection (students enrolled in all exams)")
 print("4. Difference (students enrolled in CET but not JEE)")
 print("5. Exit")
choice = int(input("Enter your choice: "))
if choice == 1:
 print("CET Students:", cet_students)
 print("JEE Students:", jee_students)
 print("NEET Students:", neet_students)
elif choice == 2:
 all_students = cet_students.union(jee_students).union(neet_students)
 print("Students enrolled in any exam:", all_students)
elif choice == 3:
 common_students =
 cet_students.intersection(jee_students).intersection(neet_students)
 print("Students enrolled in all exams:", common_students)
elif choice == 4:
 cet_not_jee = cet_students.difference(jee_students)
 print("Students enrolled in CET but not JEE:", cet_not_jee)
elif choice == 5:
 print("Exiting Student Enrollment Manager.")
break
else:
 print("Invalid choice! Please try again.")
