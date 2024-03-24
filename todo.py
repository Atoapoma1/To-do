#Create the todo to take a list
#Store the data in text files

filepath = r"C:/Users/Ato/Desktop/COURSES/PYTHON PROJECTS/WEBSERVER1/To do app/todos.txt"
while True:
    user_action = input("Type something; add, show, edit, complete or exit")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open(filepath, mode="r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open(filepath, mode="w")
            file.writelines(todos)
            file.close()

        case "show" | "view":
            file = open(filepath, mode="r")
            todos = file.readlines()
            file.close()

            # new_todos = []

            # for item in todos:
            #     new_item = item.strip("\n")
            #     new_todos.append(new_item)

            #Using list comprehsion
            new_todos = [item.strip("\n") for item in todos]

            for index, item in enumerate(new_todos):
                print(f"{index + 1} - {item}")

        case "edit":
            number = int(input("Type the number of todo to edit"))
            number = number - 1
            new_todo = input("Enter a new todo")
            todos[number] = new_todo
        case "complete":
            number = int(input("Number of todos to complete"))
            todos.pop(1 - 1)
        case "exit":
            break
        
print("bye")
 

