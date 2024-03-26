#Create the todo to take a list
#Store the data in text files

filepath = r"C:/Users/Ato/Desktop/COURSES/PYTHON PROJECTS/WEBSERVER1/To do app/todos.txt"
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        with open(filepath, mode="r") as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with  open(filepath, mode="w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open(filepath, mode="r") as file:
            todos = file.readlines()

        # new_todos = []

        # for item in todos:
        #     new_item = item.strip("\n")
        #     new_todos.append(new_item)

        #Using list comprehsion
        # new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1} - {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            with open(filepath, mode="r") as file:
                todos = file.readlines()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"
            
            with open(filepath, mode="w") as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid")

    elif user_action.startswith("complete"):
        number = int(user_action[9:])

        with open(filepath, mode="r") as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip("\n")
        todos.pop(index)

        with open(filepath, mode="w") as file:
            file.writelines(todos)

        message = f"Todo: {todo_to_remove} was removed from the list"
        print(message)

    elif user_action.startswith("exit"):
        break

    else:
        print("Command not valid")
        
print("bye")
 

