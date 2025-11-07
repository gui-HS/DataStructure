from grafo import *
import random

class Goodman:
    def __init__(self):
        self.H = None
        self.C = 0

    def conexidadeFusao(self, G):
        #Inicialização
        self.C = 0
        self.H = G

        #Fusão sucessiva de vertices
        while len(self.H.listaVertices) != 0:
            #Selecione um vértice w pertencente a H
            w = self.H.listaVertices[0]
            #Enquanto for adjacente a algum vertice
            for aresta in self.H.listaAresta:
                if aresta.getV1() == w:
                    w = self.fusion(aresta.getV2(), w)
                elif aresta.getV2() == w:
                    w  = self.fusion(aresta.getV1(), w)

            #Remove o vértice w do grafo
            self.H.removeV(w)

            #Contabilize uma nova componente conexa
            self.C += 1
        
        if self.C > 1:
            return f"Grafo não conexo, com {self.C} componentes conexas"
        return f"Grafo conexo, {self.C} componentes conexas"
    
    def fusion(self, w, v):
        for verticesAdjacentes in v.adjV():
            w.addAdjacente(Aresta(random.randint(0, 1000), w, verticesAdjacentes))

        self.H.removeV(v)
        return w
    


def testeGoodman():
    grafo1 = Grafo()
    for i in range(15):
        grafo1.insereV()

    grafo1.insereA(grafo1.listaVertices[0], grafo1.listaVertices[12])
    grafo1.insereA(grafo1.listaVertices[11], grafo1.listaVertices[2])
    grafo1.insereA(grafo1.listaVertices[2], grafo1.listaVertices[3])
    grafo1.insereA(grafo1.listaVertices[3], grafo1.listaVertices[4])
    grafo1.insereA(grafo1.listaVertices[4], grafo1.listaVertices[5])

    print(Goodman().conexidadeFusao(grafo1))

    grafo3 = Grafo()
    for i in range(5):
        grafo3.insereV()

    grafo3.insereA(grafo3.listaVertices[0], grafo3.listaVertices[1])
    grafo3.insereA(grafo3.listaVertices[1], grafo3.listaVertices[2])
    grafo3.insereA(grafo3.listaVertices[2], grafo3.listaVertices[3])
    grafo3.insereA(grafo3.listaVertices[3], grafo3.listaVertices[4])
    print(Goodman().conexidadeFusao(grafo3))

testeGoodman()