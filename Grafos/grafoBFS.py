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
            for v in u.adjV():
                if v.cor == "branco":
                    self.Q.insere(v)
                    v.cor = "cinza" #Cor para Cinza
                    v.roteamento = u #Roteamento (pai) de v será u
                    v.d = u.d + 1 #Distância de v
            u.cor = "preto"
    
    def imprimeCaminho(self, s, v): #s (vetor inicial), v (vetor final)
        if s == v:
            print(s.nome)
        elif v.roteamento == None:
            print("Não existe caminho de s para v!")
            return
        else:
            self.imprimeCaminho(s, v.roteamento)
            print("Vertice:", v.nome)

    def verConexidade(self): #Metodo para classificar um grafo nao dirigido como conexo ou nao-conexo
        c = 0

        for u in self.listaVertices:
            if u.roteamento == None:
                u.cor = "preto"
                c += 1
        if c > 1:
            print("Grafo Não Conexo")
        else:
            print("Grafo Conexo")
        print("Quantidade de componentes conexos:", c)

def testeBFS():
    grafo1 = BFS()
    for i in range(25):
        grafo1.insereV()

    grafo1.insereA(grafo1.listaVertices[0], grafo1.listaVertices[12])
    grafo1.insereA(grafo1.listaVertices[12], grafo1.listaVertices[2])
    grafo1.insereA(grafo1.listaVertices[2], grafo1.listaVertices[3])
    grafo1.insereA(grafo1.listaVertices[3], grafo1.listaVertices[4])
    grafo1.insereA(grafo1.listaVertices[4], grafo1.listaVertices[5])

    grafo1.algoritmoBFS()
    
    print("Caminho do vértice 0 até 3: (Deve percorrer 0,12,2,3)")
    grafo1.imprimeCaminho(grafo1.listaVertices[0],grafo1.listaVertices[3])
    grafo1.verConexidade()

testeBFS()
