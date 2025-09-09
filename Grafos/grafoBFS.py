from grafo import *
from fila import *

class BFS(Grafo):
    def __init__(self):
        super().__init__()
        self.s = None
        self.Q = Fila()

    def algoritmoBFS(self): #Inicializando elementos
        cont = 0
        for v in self.listaVertices:
            v.nome = cont
            v.cor = "branco"
            v.caminho = None
            v.d = True #True = Infinito
            cont += 1

        #Inicilizando busca em vertice atual
        self.s = self.listaVertices[0]
        self.s.d = 0
        self.s.cor = "cinza"
        self.Q = Fila()
        self.Q.insere(self.s)

        while self.Q.inicial: #Enquanto houver vertices na fila
            u = self.Q.remove()
            for v in u.getAresta():
                if v.cor == "branco":
                    self.Q.insere(v)
                    v.cor = "cinza" #Cor para Cinza
                    v.roteamento = u #Roteamento (pai) de v será u
                    v.d = u.d + 1 #Distância de v
        u.cor = "preto"

    def imprimeCaminho(self, G, s, v): #s (vetor inicial), v (vetor final)
        if s == v:
            print(s.nome)
        elif v.rotemento == None:
            print("Não existe caminho de s para v!")
        else:
            self.imprimeCaminho(self, G, s, v.roteamento)
            print(v.nome)

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
    for i in range(25):
        grafo1.insereV()

    for i in range((len(grafo1.listaVertices)-1)):
        grafo1.insereA(i,i+1)
    
    grafo1.listaVertices[1].addAdjacente(grafo1.listaAresta[2])

    print(grafo1.listaVertices[1].getAresta())
    grafo1.algoritmoBFS()
    #print(grafo1.listaVertices, grafo1.listaAresta)
    
    print(grafo1.imprimeCaminho())

testeBFS()
