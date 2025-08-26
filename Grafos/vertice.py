from grafoBFS import *

class Vertice:
    def __init__(self, nome):
        self.__aresta = list()
        self.__nome = nome
        self.next = None
        self.cor = -1 #BRANCO = -1, CINZA = 1, PRETO = 0 
        self.fila = Fila()
        self.d = int()
    
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
