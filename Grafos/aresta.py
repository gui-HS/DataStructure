class Aresta:
    def __init__(self, nome, v1, v2):
        self.__nome = nome
        self.__v1 = v1
        self.__v2 = v2
    
    def setV1(self, v1):
        self.__v1 = v1
    
    def setV2(self, v2):
        self.__v2 = v2

    def getNome(self):
        return self.__nome

    def getV1(self):
        return self.__v1

    def getV2(self):
        return self.__v2
