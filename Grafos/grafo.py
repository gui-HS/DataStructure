from aresta import Aresta
from vertice import Vertice

class Grafo:
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
            print(i)

    def insereV(self):
        self.listaVertices.append(Vertice(len(self.listaVertices)))

    def removeV(self, v):
        del self.listaVertices[v] #Remove da lista de vetores

        #Remove da lista de arestas
        for i in self.listaAresta:
            if (i.v1 == v or i.v2 == v):
                self.listaAresta.remove(i)
    
    def insereA(self, u, v):
        aresta = Aresta(len(self.listaAresta), u, v)
        u = self.listaVertices[u]
        v = self.listaVertices[v]
        u.addAdjacente(aresta)    
        v.addAdjacente(aresta)
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
                print(j)

    def getA(self, u, v):
        for i in self.listaAresta:
            #Para arestas não dirigidas
            if (i.v1 == u or i.v1 == v or i.v2 == u or i.v2 == v):
                print(i)

    def grau(self, v):
        a = self.listaVertices[v]
        return len(a.aresta)
    
    def oposto(self, v, e):
        pass
    
    def verticesA(self, e):
        temp = self.listaAresta[e]
        print(f"{e} = ({temp.v1}, {temp.v2})")

    def arestasE(self, v):
        for i in self.listaAresta:
            if i.v1 == v:
                print(i)
    
    def arestasS(self, v):
        for i in self.listaAresta:
            if i.v2 == v:
                print(i)
