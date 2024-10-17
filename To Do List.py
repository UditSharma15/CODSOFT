tasks= []
print("Enter the number of the operation you want to operate")
print("1. Add  a task")
print("2. Delete a task")
print("3. View the Task")
print("4. Exit")

def addtask():
  task = input("enter the task to add: ")
  tasks.append(task)
  print(f"the task {task} is successfully addded")

def deltask():
  tasktodelete = int(input("enter the number of the task you want to delete: ")
  tasks.pop(tasktodelete)
  print(f"the task #{tasktodelete} is successfully deleted")

def viewtask():
  if not task:
    print("task list is empty")
  else:
    for index,task in enumerate(tasks):
      print(f"Task #{index}. {task}")
      
while True:
  if choice == 1:
    addtask()
  elif choice == 2:
    deltask()
  elif choice == 3:
    viewtask()
  elif choice == 4:
    break
  else:
    print("Invalid Input!)
print("GoodBye!")

