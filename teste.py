import PySimpleGUI as sg

fruitsList = list()

def buildLayout():

    layout = [
        [sg.Frame('Frutas', [[]], key='frameTeste')],
        [sg.Input(size=(10,10), do_not_clear=True, key='fruitSelector'), sg.Button('Submit', key='submit'), sg.Button('Remover', key='del')]
    ]

    win = sg.Window('Teste App', layout, finalize=True)
    
    for lin in fruitsList:
        win.extend_layout(win['frameTeste'], lin)

    return win

def newRow(fruit):
    num = 0
    row = [[sg.Text(f'{num}:'), sg.Text(f'{fruit}'), sg.Checkbox('')]]
    fruitsList.append(row[:])

    win.extend_layout(win['frameTeste'], row)
    print(row)

win = buildLayout()
while True:
    event, value = win.read()
    
    if event == sg.WIN_CLOSED:
        break
    elif event == 'submit':
        newRow(value['fruitSelector'])
    elif event == 'del':
        win.close()
        win = buildLayout()
        pass