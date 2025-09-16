from fila import *

class Vertice:
    def __init__(self, nome):
        self.__aresta = list() #Lista de arestas conectadas ao vetor
        self.__nome = nome
        self.next = None #Refência ao próximo vetor
        self.cor = None #BRANCO (On), CINZA (On operation), PRETO (off)
        self.caminho = None #Sla
        self.d = None #Distância
        self.roteamento = None #Vértice Pai
        self.abertura = None #Tempo até abertura do vértice
        self.fechamento = None #Tempo até fechamento do vértice

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def addAdjacente(self, aresta):
        self.__aresta.append(aresta)

    def lenAresta(self):
        return len(self.__aresta)
    
    def getAresta(self):
        return self.__aresta
    
    def adj(self):
        bla = []
        for i in self.__aresta:
            a = i.getV2()
            bla.append(a)
        return bla
