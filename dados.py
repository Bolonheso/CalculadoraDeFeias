class Participante:
    def __init__(self, id, nome, dias, pagou):
        self.id = id
        self.nome = nome
        self.dias = dias
        self.pagou = pagou

    def addDias(self, *dias):
        for dia in dias:
            self.dias.append(dia)
        self.quantDias = len(dias)

    def delDias(self, *dias):
        for dia in dias:
            self.dias.remove(dia)
        self.quantDias = len(dias)

    def pagamento(self, val):
        self.pagou = val

class Familia:
    def __init__(self, id, pagante, partsList):
        self.id = id
        self.pagante = pagante
        self.partsList = partsList

    def DEFpagante(self, pag):
        self.pagante = pag

    def addPart(self, *parts):
        for part in parts:
            self.partsList.append(part)
    
    def delPart(self, *IDparts):
        for IDpart in IDparts:
            self.partsList.pop(IDpart-1)

    def partsInfo(self):
        info = list()
        inffo = list()
        for participante in self.partsList:
            info.append(participante.nome)
            info.append(participante.dias)
            info.append(participante.quantDias)
            info.append(participante.pagou)

            inffo.append(info[:])
            info.clear()
        return inffo

valTotal = float()
familiasList = list()
diasViagem = list()
totalDiasPagos = int()
