import PySimpleGUI as sg
import Interface as itf
from itfLogica import logicaInterface

familiasList = []
windowBase = itf.layoutBase(familiasList)
estado = 'base' 

funcsTela = logicaInterface(windowBase, familiasList, estado)

while True:
    funcsTela.mainLoop(sg.read_all_windows())
    estado = funcsTela.estado
    
    match estado:
        case 'base':
            funcsTela.winBase()
        case 'addFam':
            funcsTela.addFams()
        case 'editFam':
            funcsTela.editFam()
        case 'addEditPart':
            funcsTela.addEditPart()

