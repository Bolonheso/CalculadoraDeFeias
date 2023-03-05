import PySimpleGUI as sg

layout = [[sg.Button('Mostrar Popup')]]

window = sg.Window('Exemplo de Popup', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Mostrar Popup':
        sg.popup('Olá, mundo!')

window.close()
