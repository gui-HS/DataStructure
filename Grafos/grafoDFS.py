from grafo import *

class DFS(Grafo):
    def __init__(self):
        super().__init__()
        self.V = self.listaVertices
        self.E = self.listaAresta
        self.tempo = 0

    def DFS(self):
        for v in self.listaVertices:
            v.cor = "branco"
            v.roteamento = None
        
        self.tempo = 0

        for u in self.V:
            if u.cor == "branco":
                self.DFSVisit(u)

    def DFSVisit(self, u):
        u.cor = "cinza"
        self.tempo = self.tempo + 1
        u.abertura = self.tempo

        for v in u.adj():
            if v.cor == "branco":
                v.roteamento = u
                self.DFSVisit(v)
            
            u.cor = "preto"
            self.tempo = self.tempo + 1
            u.fechamento = self.tempo

    def printVerotes(self):
        for u in self.V:
            if u.roteamento != None:
                temp = u.roteamento.getNome()
            else:
                temp = None
            print("Vetor:", u.getNome(), "Tempo de abertura:", u.abertura,
                "Tempo de Fechamento:", u.fechamento, "Vetor antecessor:", temp)
            

def testeDFS():
    grafo1 = DFS()
    for i in range(25):
        grafo1.insereV()

    grafo1.insereA(grafo1.listaVertices[0], grafo1.listaVertices[12])
    grafo1.insereA(grafo1.listaVertices[12], grafo1.listaVertices[2])
    grafo1.insereA(grafo1.listaVertices[2], grafo1.listaVertices[3])
    grafo1.insereA(grafo1.listaVertices[3], grafo1.listaVertices[4])
    grafo1.insereA(grafo1.listaVertices[4], grafo1.listaVertices[5])

    grafo1.DFS()
    grafo1.printVerotes()

testeDFS()
