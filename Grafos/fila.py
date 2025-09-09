from fila import *

class Vertice:
    def __init__(self, nome):
        self.__aresta = list()
        self.__nome = nome
        self.next = None
        self.cor = None #BRANCO (On), CINZA (On operation), PRETO (off)
        self.caminho = None
        self.d = None
        self.roteamento = None

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
