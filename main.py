tasks = []


if __name__ == "__main__":

     ### Create a loop to run the app
     print("Welcome to the to do list app :")
     while True:
     print("\n")
     print("Please select on of the following options")
     print("_________________________________________")
     print("1. Add a task")
     print("2. View all tasks")
     print("3. Exit")
     print("4. Quit")
     print("_________________________________________")

     choice = input("Enter your choice: ")

     if( choice == "1"):
          addTask()
     elif(choice == "2"):
          delete()
     elif(choice == "3"):
          listTasks()
     elif(choice == "4"):
          break
     else:
          print("Invalid input. Please try again.")

print("Goodbye ")