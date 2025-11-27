class Aresta:
    def __init__(self, nome, v1, v2):
        self.__nome = nome
        self.__v1 = v1
        self.__v2 = v2
        self._prevEdge = None
        self._nextEdge = None
        self._EulerEdge = None
        self.__valor = None

    # Estrutura para criação de heap, 
    # utilizado no arquivo de caminhos mínimos
    def __lt__(self, other): 
        return self.getValor() < other.getValor()

    def theOtherOne(self, v):
        if self.getV1() == v:
            return self.getV2()
        return self.getV1()

    def setV1(self, v1):
        self.__v1 = v1

    def setV2(self, v2):
        self.__v2 = v2

    def setValor(self, valor):
        self.__valor = valor

    def getNome(self):
        return self.__nome

    def getV1(self):
        return self.__v1

    def getV2(self):
        return self.__v2
    
    def getValor(self):
        return self.__valor

    # Getters
    def getPrevEdge(self):
        return self._prevEdge

    def getNextEdge(self):
        return self._nextEdge

    def getEulerEdge(self):
        return self._EulerEdge

    # Setters
    def setPrevEdge(self, edge):
        self._prevEdge = edge

    def setNextEdge(self, edge):
        self._nextEdge = edge

    def setEulerEdge(self, edge):
        self._EulerEdge = edge
