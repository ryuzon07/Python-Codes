tasks = []
while True:
 print("\nTask List Manager")
 print("1. Add a task")
 print("2. Remove a task")
 print("3. Update a task")
 print("4. View tasks")
 print("5. Sort tasks")
 print("6. Exit")
choice = int(input("Enter your choice: "))
if choice == 1:
 task = input("Enter the task to add: ")
 tasks.append(task)
 print("Task added!")
elif choice == 2:
 task = input("Enter the task to remove: ")
if task in tasks:
 tasks.remove(task)
 print("Task removed!")
else:
 print("Task not found!")
elif choice == 3:
 old_task = input("Enter the task to update: ")
if old_task in tasks:
 new_task = input("Enter the new task: ")
 index = tasks.index(old_task)
 tasks[index] = new_task
 print("Task updated!")
else:
 print("Task not found!")
elif choice == 4:
 print("Current Tasks:")
for i, task in enumerate(tasks, start=1):
 print(f"{i}. {task}")
elif choice == 5:
 tasks.sort()
 print("Tasks sorted!")
elif choice == 6:
 print("Exiting Task List Manager.")
break
else:
 print("Invalid choice! Please try again.")
