print("Hola, bienvenido al Buscaminas CLI")


def add_task():
    # este es mini todo-list
    task = input("Enter a task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")


def main():
    while True:
        print("1. Add Task")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# dale duro vamos a ello


if __name__ == '__main__':
    main()
