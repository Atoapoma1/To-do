import functions
import PySimpleGUI as sg


#The gui
label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My To-do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()