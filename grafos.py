import turtle

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
        for i in self.listaVertices: #Remove da lista de vetores
            if i == v:
                print("bla")

        for i in self.listaAresta: #Remove da lista de arestas
            if (i.v1 == v or i.v2 == v):
                self.listaAresta.remove(i) 
    
    def insereA(self, u, v):
        aresta = Aresta(len(self.listaAresta), u, v)
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

class Vertice:
    def __init__(self, nome):
        self.__aresta = list()
        self.__nome = nome
    
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

def graphic(grafo):
    t = turtle.Turtle()
    #https://www.geeksforgeeks.org/python/draw-any-polygon-in-turtle-python/

    #This will be used to draw the edges
    listPosition = list()

    #Draw Vectors
    t.hideturtle()
    t.penup()
    t.setpos(0,300)
    t.speed(50)
    for i in grafo.listaVertices:
        listPosition.append(t.pos())
        t.dot(15) 
        t.write(f"V{i.getNome()}")
        t.forward(100)
        t.right(360/len(grafo.listaVertices))

    #Draw Edges
    t.showturtle()
    for i in grafo.listaAresta:
        v1 = i.getV1() 
        v2 = i.getV2()
        
        v1Position = listPosition[v1]
        v2Position = listPosition[v2]

        t.setpos(v1Position)
        t.pendown()
        t.goto(v2Position)
        t.penup()
        print(v1,v2)

    turtle.done()

def main():
    print("OK")

    grafo1 = Grafo()
    for i in range(25):
        grafo1.insereV()

    grafo1.vertices()

    #Lista após remoção
    print("\n"*5)
    grafo1.vertices()
    print(grafo1.getOrdem())
    print(grafo1.getTamanho())

    for i in range((len(grafo1.listaVertices)-1)):
        grafo1.insereA(i,i+1)
    
    grafo1.insereA(24,0)

    #estrela
    grafo1.insereA(19,6)
    grafo1.insereA(6, 0)
    grafo1.insereA(0, 14)
    grafo1.insereA(14, 2)
    grafo1.insereA(2, 19)

    graphic(grafo1)


    

if __name__ == "__main__":
    main()
