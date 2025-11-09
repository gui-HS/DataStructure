class Vertice:
    def __init__(self, nome):
        self.aresta = list()  # Lista de arestas conectadas ao vetor
        self.nome = nome
        self.next = None  # Refência ao próximo vetor
        self.cor = None  # BRANCO (On), CINZA (On operation), PRETO (off)
        self.caminho = None  # Sla
        self.d = None  # Distância
        self.roteamento = None  # Vértice Pai
        self.abertura = None  # Tempo até abertura do vértice
        self.fechamento = None  # Tempo até fechamento do vértice
        self.eulerEdge = None

    def setEulerEdge(self, aresta):
        self.eulerEdge = aresta

    def getEulerEdge(self):
        return self.eulerEdge

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def addAdjacente(self, aresta):
        self.aresta.append(aresta)

    def lenAresta(self):
        return len(self.aresta)

    def getAresta(self):
        return self.aresta

    def adj(self):
        # bla = []
        # for i in self.aresta:
        #    a = i.getV2()
        #    bla.append(a)
        return self.aresta

    def adjV(self):
        setV = set()
        for i in self.aresta:
            setV.add(i.getV1())
            setV.add(i.getV2())
        return setV
