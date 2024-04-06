from functions import get_todos, write_todos
import time

now = time.strftime("%D")
print(f"It is now: {now}")

filepath = r"C:/Users/Ato/Desktop/COURSES/PYTHON PROJECTS/WEBSERVER1/To do app/todos.txt"
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos(filepath)

        todos.append(todo + "\n")

        write_todos(filepath, todos)

    elif user_action.startswith("show"):
        todos = get_todos(filepath)

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

            todos = get_todos(filepath)

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"
            
            write_todos(filepath, todos)
        except ValueError:
            print("Your command is not valid")
            continue 

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos(filepath)

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos(filepath, todos)

            message = f"Todo: {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that Index")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command not valid")
        
print("bye")
 

