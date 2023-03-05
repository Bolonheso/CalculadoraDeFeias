import PySimpleGUI as sg
import Interface as itf
import dados
from sys import exit

def delElements(elementsList, elementId, windowRestarted):
    pass

class logicaInterface: 
    def __init__(self, winBase, famsList, estado):
        self.windowBase = winBase
        self.familiasList = famsList
        self.estado = estado
        self.estadoBefore = estado

    def defInfo(self, args):
        self.win, self.event, self.value = args

    def winBase(self):
        if self.win == self.windowBase and self.event == sg.WIN_CLOSED:
            exit()   

        if self.win == self.windowBase and self.event == 'add' and self.estado == 'base':
            self.parts = list()
            self.windowAddFam  = itf.layoutAddFamily(self.parts)
            self.estado = 'addFam'

        for fam in self.familiasList:
            if self.win == self.windowBase and self.event == fam.id:
                self.famToEdit = fam
                self.windowEditFamily = itf.layoutEditFamily(self.famToEdit)
                self.estado = 'editFam'
        
        if self.win == self.windowBase and self.event == 'delFam':
            for fam in self.familiasList:
                if self.value[f'Fd{fam.id}']:
                    self.familiasList.remove(fam)
            self.windowBase.close()
            self.windowBase = itf.layoutBase(self.familiasList)

    def addFams(self):
        if self.win == self.windowAddFam and self.event == sg.WIN_CLOSED:
            self.windowAddFam.close()
            self.estado = 'base'

        if self.win == self.windowAddFam and self.event == 'cancelAddFam':
            self.windowAddFam.close()
            self.estado = 'base'

        if self.win == self.windowAddFam and self.event == 'addPart':
            self.parts.append(dados.Participante(
                len(self.parts),
                self.value['partNome'],
                self.value['partDias'],
                self.value['partValor']))
            
            self.windowAddFam.find_element('defPagAddWin').update(values=[participante.nome for participante in self.parts])
            self.windowAddFam.extend_layout(self.windowAddFam['partsList'], [[sg.Text(f"{self.parts[-1].id}:"), sg.Text(f'{self.value["partNome"]}, R${self.value["partValor"]} Dias: {self.value["partDias"]}'), sg.Checkbox('', key=f'P{len(self.parts)-1}')]])

        if self.win == self.windowAddFam and self.event == 'delPart':
            for part in self.parts[:]:
                if self.win == self.windowAddFam and self.value[f'P{part.id}']:
                    self.parts.remove(part)
            self.windowAddFam.close()
            self.windowAddFam = itf.layoutAddFamily(self.parts)

        if len(self.parts) >= 1:
            self.windowAddFam.find_element('delPart').update(visible=True)
        else:
            self.windowAddFam.find_element('delPart').update(visible=False)

        if self.win == self.windowAddFam and self.event == 'addFamily':
            fam = dados.Familia(
                len(self.familiasList),
                self.value['defPagAddWin'] if self.value['defPagAddWin'] != '' else self.parts[:][0].nome,
                self.parts[:]
                )
            
            self.familiasList.append(fam)

            if len(self.familiasList) == 1:
                self.windowBase.close()
                self.windowBase = itf.layoutBase(self.familiasList, ext=False)

            self.windowBase.extend_layout(self.windowBase['frameFamilias'], [[sg.Text(f'{fam.id}:'), sg.Text(f'{fam.pagante}'), sg.Button('Editar', key=fam.id), sg.Checkbox('', key=f'Fd{fam.id}')]])
            self.estado = 'base'
            self.windowAddFam.close()

    def editFam(self):
        if self.win == self.windowEditFamily and self.event == 'confEditFam':
            self.windowEditFamily.close()
            self.estado = 'base'

        if self.win == self.windowEditFamily and self.event == sg.WIN_CLOSED:
            self.windowEditFamily.close()
            self.estado = 'base'

        if self.win == self.windowEditFamily and self.event == 'defPagante':
            self.famToEdit.pagante = self.value['defPagante']
        
        elif self.win == self.windowEditFamily and self.event == 'delPart':
            
            for part in self.famToEdit.partsList[:]:
                if self.win == self.windowEditFamily and self.event[part.id]:
                    self.famToEdit.partsList.remove(part)
            
            self.windowEditFamily.close()
            self.windowEditFamily = itf.layoutEditFamily(self.famToEdit)

        for part in self.famToEdit.partsList[:]:
            if self.win == self.windowEditFamily and self.event == f'Pe{part.id}':
                self.windowAddEditPart = itf.layoutAddEditPart(part)
                self.partToEdit = part
                self.estado = 'addEditPart'
                self.estadoBefore = 'editFam'
        
        #for f in range(len(self.familiasList)):
        #    if self.familiasList[f].id == self.famToEdit.id:
        #        self.familiasList[f] = self.famToEdit

    def addEditPart(self):
        if self.win == self.windowAddEditPart and self.event == sg.WIN_CLOSED:
            self.windowAddEditPart.close()

            if self.estadoBefore == 'editFam': self.estado = self.estadoBefore
            elif self.estadoBefore == 'addFam': self.estado = self.estadoBefore
        
        if self.win == self.windowAddEditPart and self.event == 'addEditPart':
            self.partToEdit.nome = self.value['partNome']
            self.partToEdit.pagou = self.value['partValor']
            self.partToEdit.dias = self.value['partDias']

            self.windowAddEditPart.close()
            
            if self.estadoBefore == 'editFam':
                self.windowEditFamily.close()
                self.windowEditFamily = itf.layoutEditFamily(self.famToEdit)


    def mainLoop(self, reads):
        self.defInfo(reads)
        
        if self.win == self.winBase and self.event == sg.WIN_CLOSED: exit()
