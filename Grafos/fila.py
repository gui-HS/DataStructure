from vertice import Vertice

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

def testeFila():
    fila1 = Fila()

    fila1.insere(Vertice(1))
    fila1.insere(Vertice(2))
    fila1.insere(Vertice(3))
    fila1.imprimir()
    fila1.remove()
    print("Após remoção: ")
    fila1.imprimir()