class Fila:
    def __init__(self):
        self.inicial = None

    
    def insere(self, v):
        if not(self.inicial):
            self.inicial = v
        else:
            temp = self.inicial
            while temp.next != None:
                temp = temp.next
            temp.next = v

    def remove(self):
        temp = self.inicial
        self.inicial = self.inicial.next
        return temp
    
    def imprimir(self):
        if not(self.inicial):
            return
        else:
            temp = self.inicial
            while temp:
                print(temp.getNome())
                temp = temp.next