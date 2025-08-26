from grafo import *
from grafo import Grafo

class BFS(Grafo):
    def __init__(self, listaVertices, listaAresta):
        super().__init__(listaVertices, listaAresta)
        self.s = Vertice()
        self.Q = Fila()

    def algoritmoBFS(self):
        for v in self.listaVertices:
            v.cor = -1
            v.caminho = None
            v.d = True #True = Infinito

        self.s.d = 0
        self.s.cor = 1
        self.Q.insere(self.s)

        while self.Q.inicial:
            u = self.Q.remove()
            for v in u.getArestas:
                if v.cor == -1:
                    self.Q.insere(v)
                    v.cor = 1 #Cor para Cinza
                    v.roteamento = u #Roteamento (pai) de v será u
                    v.d = u.d + 1 #Distância de v
        u.cor = 0

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

def testeBFS():
    grafo1 = BFS()

    grafo1 = Grafo()
    for i in range(25):
        grafo1.insereV()

    for i in range((len(grafo1.listaVertices)-1)):
        grafo1.insereA(i,i+1)
    
    grafoBfs1 = BFS(grafo1)
    grafoBfs1.algoritmoBFS(Vertice(1))

