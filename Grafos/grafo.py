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
            print(i.getNome())

    def insereV(self):
        self.listaVertices.append(Vertice(len(self.listaVertices)))

    def removeV(self, v):
        self.listaVertices = [
            i for i in self.listaVertices if i != v
        ]  # Remove da lista de vertices
        self.listaAresta = [
            i for i in self.listaAresta if i.getV1() != v and i.getV2() != v
        ]  # Remove todas arestas

        for vertices in self.listaVertices:
            vertices.aresta = [
                x for x in vertices.aresta if x.getV1() != v and x.getV2() != v
            ]

    def insereA(self, u, v):
        aresta = Aresta(len(self.listaAresta), u, v)
        u.addAdjacente(aresta)
        v.addAdjacente(aresta)
        self.listaAresta.append(aresta)

    def removeA(self, e):
        self.listaAresta.remove(e)

        for vertice in self.listaVertices:
            vertice.aresta = [aresta for aresta in vertice.aresta if aresta != e]
        # Remove instancias nos vertices utilizados
        # v1 = e.getV1()
        # v2 = e.getV2()
        # v1.aresta = [aresta for aresta in v1.aresta if aresta != e]
        # v2.aresta = [aresta for aresta in v2.aresta if aresta != e]

    # def adj(self, v): #Adaptado para o exercicio de grafoBFS
    #    bla = []
    #    for i in self.listaVertices[v]:
    #        for j in i.aresta:
    #            bla.append(j)
    #    return bla

    def adjV(self, vertice):  # Avalia se dado vértice é adjacente a outro e o retorna
        for aresta in self.listaAresta:
            if aresta.getV1() == vertice:
                return aresta.getV2()
            elif aresta.getV2() == vertice:
                return aresta.getV1()
        return False

    #Verifica se dois vértices são adjacentes e o retorna
    def adjV2(self, u, v):
        for aresta in self.listaAresta:
            if ((aresta.getV1() == u and aresta.getV2() == v) or  
               (aresta.getV1() == v and aresta.getV2() == u)):
                return aresta
        return False

    def adj(self, indice):
        return self.listaVertices[indice].adj()

    def getA(self, u, v):
        for i in self.listaAresta:
            # Para arestas não dirigidas
            if i.getV1() == u or i.getV1() == v or i.getV2() == u or i.getV2() == v:
                print(i)

    def grau(self, v):
        a = self.listaVertices[v]
        return len(a.aresta)

    def oposto(self, v, e):
        pass

    def verticesA(self, e):
        temp = self.listaAresta[e]
        print(f"{e} = ({temp.getV1()}, {temp.getV2()})")


"""
def teste():
    grafo1 = Grafo()
    for i in range(25):
        grafo1.insereV()

    grafo1.insereA(grafo1.listaVertices[0], grafo1.listaVertices[12])
    grafo1.insereA(grafo1.listaVertices[12], grafo1.listaVertices[2])
    grafo1.insereA(grafo1.listaVertices[2], grafo1.listaVertices[3])

    print(grafo1.vertices())
    print(grafo1.listaVertices)
    #print(grafo1.arestas())

teste()
"""

