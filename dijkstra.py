class Dijkstra:
    def __init__(self):
        self.H = None

    def initialize(G, s):
        for v in G.listaVertices:
            v.d = "inf"
            v.roteamento = None
