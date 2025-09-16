from grafo import *

class Goodman():
    def __init__(self, G):
        self.H = G
        self.V = self.H.listaVertices
        self.E = self.H.listaAresta
        self.C = 0

    def goodMan(self):
        while len(self.V) != 0:
            for w in self.V:
                while self.adj(w):
                    u = self.adj(w)
                    w = self.fusion(w,u)

    def adj(self, w):
        for i in self.E:
            if i.getV1() == w:
                return i.getV2()
            elif i.getV2() == w: #Grafos nao dirigidos
                return i.getV1()
        return False

    def fusion(self, w, u):
        w.addAdjacente(u)
        self.H.removeV(u)


def testeBFS():
    grafo1 = Grafo()
    for i in range(15):
        grafo1.insereV()

    grafo1.insereA(grafo1.listaVertices[0], grafo1.listaVertices[12])
    grafo1.insereA(grafo1.listaVertices[12], grafo1.listaVertices[2])
    grafo1.insereA(grafo1.listaVertices[2], grafo1.listaVertices[3])
    grafo1.insereA(grafo1.listaVertices[3], grafo1.listaVertices[4])
    grafo1.insereA(grafo1.listaVertices[4], grafo1.listaVertices[5])

    grafo2 = Goodman(grafo1)
    grafo2.goodMan()

testeBFS()

        