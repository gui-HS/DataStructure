from grafo import *

class Goodman():
    def __init__(self, G):
        self.H = G
        self.V = self.H.listaVertices
        self.E = self.H.listaAresta
        self.C = 0

    def goodMan(self):
        while len(self.V) > 1:
            for w in self.V: #Pegar vetor
                while w.adj(): #Enquanto for adjacente a algum vertice
                    print(w.adj())
                    u = self.adj(w) #Pega o primeiro vertice
                    w = self.fusion(w,u)

    def adj(self, w):
        for i in w.aresta:
            if i.getV1() == w:
                return i.getV2()
            elif i.getV2() == w: #Grafos nao dirigidos
                return i.getV1()
        return None

    def fusion(self, w, u):
        v = Vertice(len(self.E)+1)

        for aresta in w.getAresta():
            if aresta.getV1() == w:
                aresta.setV1(v)
            elif aresta.getV2() == w:
                aresta.setV2(v)
            v.addAdjacente(aresta)
            
        for aresta in u.getAresta():
            if aresta.getV1() == u:
                aresta.setV1(v)
            elif aresta.getV2() == u:
                aresta.setV2(v)
            v.addAdjacente(aresta)

        #Remover os vértices antigos e adicionar o novo
        self.H.removeV(w)
        self.H.removeV(u)
        self.H.listaVertices.append(v)
    
        self.V = self.H.listaVertices
        self.E = self.H.listaAresta

        self.goodMan()
        #return v
        
    def status(self):
        if self.C > 1:
            return "Grafo não conexo"
        return "Grafo conexo"


def testeGoodman():
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
    grafo2.status()

testeGoodman()

        