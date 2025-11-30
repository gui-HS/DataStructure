from aresta import *
from vertice import *

class GrafoDirigido:
    def __init__(self):
        self.listaVertices = list()
        self.listaAresta = list()

    def getOrdem(self):
        return len(self.listaVertices)
    
    def getTamanho(self):
        return len(self.listaAresta)
    
    def vertices(self):
        for i in self.listaVertices:                                                                                        
            print(i.getNome())

    def arestas(self):
        for i in self.listaAresta:
            print(i.getNome())

    def insereV(self):
        self.listaVertices.append(Vertice(len(self.listaVertices)))

    def removeV(self, v):
        for i in self.listaVertices: #Remove da lista de vetores
            if i == v:
                del[i]

        for i in self.listaAresta: #Remove da lista de arestas
            if (i.v1 == v or i.v2 == v):
                self.listaAresta.remove(i)
    
    def insereA(self, u, v):
        aresta = Aresta(len(self.listaAresta), u, v)
        u = self.listaVertices[u]
        v = self.listaVertices[v]
        u.addAdjacente(aresta) # Adiciona a aresta apenas a u
        self.listaAresta.append(aresta)
    
    def removeA(self, e):
        self.listaAresta.remove(e)
        for i in self.listaVertices:
            for j in i.aresta:
                if j == e:
                    i.remove(e)

    def adj(self, v):
        for i in self.listaVertices[v]:
            for j in i.aresta:
                if j.v1 == v:
                    print(j.v2)

    def getA(self, u, v):
        # Para arestas não dirigidas
        for aresta in self.listaAresta:
            if aresta.getV1() == u and aresta.getV2() == v:
                return aresta
        return None
    
    def grauE(self, v):
        qtd = 0
        for aresta in self.listaAresta:
            if aresta.getV2() == v:
                qtd += 1
        return qtd

    def grauS(self, v):
        return len(v.adjV())

    def grau(self, v):
        a = self.listaVertices[v]
        return len(a.aresta)
    
    def oposto(self, v, e):
        if e.getV1() == v:
            return e.getV2()
        elif e.getV2() == v:
            return e.getV1()
        return False
    
    def verticesA(self, e):
        return (e.getV1(), e.getV2())

    def arestasS(self, v):
        for i in self.listaAresta:
            if i.getV1() == v:
                print(i)
    
    def arestasE(self, v):
        for i in self.listaAresta:
            if i.getV2() == v:
                print(i)