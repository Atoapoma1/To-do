def get_todos(filepath):
    with open(filepath, mode="r") as file:
        todos = file.readlines()
    return todos

def write_todos(filepath, todos_arg):
    with open(filepath, mode="w") as file:
        file.writelines(todos_arg)

print(__name__)