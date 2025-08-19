class Grafo:
    def __init__(self):
        self.listaVertices = list()
        self.vertice = Vertice
        self.listaAresta = list()

    def getOrdem(self):
        return len(self.listaVertices)
    
    def getTamanho(self):
        return len(self.listaAresta)
    
    def vertices(self):
        for i in self.listaVertices:
            print(i)

    def arestas(self):
        for i in self.listaAresta:
            print(i)

    def insereV(self):
        self.listaVertices.append(Vertice("v"+len(self.listaVertices())))

    def removeV(self, v):
        self.listaVetores.remove(v) #Remove da lista de vetores

        #Remove da lista de arestas
        for i in self.listaAresta():
            if (i.v1 == v or i.v2 == v):
                self.listaAresta.remove(i)
    
    def insereA(self, u, v):
        nome = len(self.listaAresta)
        nome = Aresta(u, v)
        u.addAdjacente(nome)
        v.addAdjacente(nome)
        self.listaAresta.append(nome)
    
    def removeA(self, e):
        self.listaAresta.remove(e)
        for i in self.listaVetores:
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
    
    def vertices(self, e):
        temp = self.listaAresta[e]
        print(f"{e} = ({temp.v1}, {temp.v2})")

class Vertice:
    def __init__(self):
        self.__aresta = list()
    
    def addAdjacente(self, aresta):
        self.aresta.append(aresta)

    def lenAresta(self):
        return len(self.aresta)
    
    def getAresta(self):
        return self.__aresta

class Aresta:
    def __init__(self, nome, v1, v2):
        self.__nome = nome
        self.__v1 = v1
        self.__v2 = v2
    
    def setV1(self, v1):
        self.v1 = v1
    
    def setV2(self, v2):
        self.v2 = v2

    def getNome(self):
        return self.nome

    def getV1(self):
        return self.v1

    def getV2(self):
        return self.v2

