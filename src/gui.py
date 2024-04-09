import functions
import PySimpleGUI as sg

filepath = r"C:/Users/Ato/Desktop/COURSES/PYTHON PROJECTS/WEBSERVER1/Todoapp/To-do/todos.txt"
#The gui

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="Todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(filepath), key="Todos",
                       enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window("My To-do App",
                    layout=[[label], [input_box, add_button],
                    [list_box, edit_button]],
                    font=("Blue",20))


while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Add":
            todos = functions.get_todos(filepath)
            new_todo = values["Todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(filepath, todos)
        case sg.WIN_CLOSED:
            break
        
event, values = window.read()
print(event)
print(values)
window.close()