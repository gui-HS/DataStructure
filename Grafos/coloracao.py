from grafo import *
import turtle

class Coloracao:
    def __init__(self, G):
        self.G = G
        self.C = None
        self.f = set() # Lista de cores utilizadas

    def colorir(self):
        self.C = [x for x in self.G.listaVertices] # Lista de vértices não coloridos

        while self.C: 
            maiorVertice = self.C[0]

            for vertice in self.C: 
                # Pega o vértice não-colorido de maior ordem e maior grau colorido
                if len(vertice.adjV()) > len(maiorVertice.adjV()):
                    maiorVertice = vertice
                elif len(vertice.adjV()) == len(maiorVertice.adjV()):
                    if vertice.grauCor() > maiorVertice.grauCor():
                        maiorVertice = vertice
                
            # Obtém a menor cor disponível
            listaCores = maiorVertice.listaCores()
            novaCor = 0
            for cor in listaCores:
                if novaCor == cor:
                    novaCor += 1
                elif novaCor < cor:
                    break
            maiorVertice.cor = novaCor
            self.f.add(novaCor)
            self.C.remove(maiorVertice)

        return self.f
            
def test():
    # Teste com grafo ciclo
    grafo = Grafo()

    for _ in range(11):
        grafo.insereV()

    for i in range(10):
        grafo.insereA(grafo.listaVertices[i], grafo.listaVertices[i+1])

    grafo.insereA(grafo.listaVertices[0], grafo.listaVertices[10])
    coloracao1 = Coloracao(grafo)
    print("V = ", coloracao1.colorir(), "| Grafo ciclo C11")

    # Teste com grafo ciclo 2
    grafo2 = Grafo()

    for _ in range(10):
        grafo2.insereV()

    for i in range(9):
        grafo2.insereA(grafo2.listaVertices[i], grafo2.listaVertices[i+1])

    grafo2.insereA(grafo2.listaVertices[0], grafo2.listaVertices[9])
    coloracao2 = Coloracao(grafo2)
    print("V = ", coloracao2.colorir(), "| Grafo ciclo C10")

    # Teste com grafo completo (10 vértices)
    grafo3 = Grafo()

    for _ in range(10):
        grafo3.insereV()

    for i in range(10):
        for j in range(10):
            grafo3.insereA(grafo3.listaVertices[i], grafo3.listaVertices[j])

    coloracao3 = Coloracao(grafo3)
    print("V = ", coloracao3.colorir(), "| Grafo K10 completo")

    # Grafo bipartido
    grafo4 = Grafo()

    for _ in range(6):
        grafo4.insereV()

    for i in range(5):
        grafo4.insereA(grafo4.listaVertices[i], grafo4.listaVertices[i+1])

    coloracao4 = Coloracao(grafo4)
    print("V = ", coloracao4.colorir(), "| Grafo Bipartido K3,3")

test()

def graphic2(grafo):
    t = turtle.Turtle()

    t.speed(1)
    grafo = grafo.G
    #                    A        B          C          D        E        F       G        H             I              J           K       L
    listPosition = [(-250,250),(-150,175),(450,200),(350,100),(450,100),(550,100),(450,0),(-150,25),(-250,-50),(-350,25),(-350,175),(-250,100)]
    listaCores = ["red", "green", "blue"]

    # Draw Vectors
    t.hideturtle()
    t.penup()
    t.setpos(-250,250)
    t.speed(50)
    t.pensize(3)
    for i in grafo.listaVertices:
        t.goto(listPosition[i.getNome()])
        t.write(chr(i.getNome()+65), font=("Aerial", 16, "normal", "bold"))
        t.dot(15)

    #Draw Edges
    t.showturtle()
    for i in grafo.listaAresta:
        v1 = i.getV1() 
        v2 = i.getV2()
        
        v1Position = listPosition[v1.nome]
        v2Position = listPosition[v2.nome]

        t.setpos(v1Position)
        t.pendown()
        t.goto(v2Position)
        t.penup()
        t.hideturtle()

    # Pintar
    t.hideturtle()
    t.penup()
    t.speed(50)
    t.pensize(3)
    vertices_ordenados = sorted(grafo.listaVertices, 
                           key=lambda v: len(v.adjV()), 
                           reverse=True)
    for i in vertices_ordenados:
        t.goto(listPosition[i.getNome()])
        t.color(listaCores[i.cor])
        t.write(chr(i.getNome()+65), font=("Aerial", 16, "normal", "bold"))
        t.dot(15)

    t.goto(0,325)
    t.color("red")
    t.write("FELIZ NATAL!", font=("Aerial", 32, "normal", "bold"))
    t.color("blue")
    t.goto(315,325)
    t.write("🎅", font=("Aerial", 32, "normal", "bold"))
    t.color("green")
    t.goto(350,325)
    t.write("🎄", font=("Aerial", 32, "normal", "bold"))

    turtle.done()

grafo3 = Grafo()
for _ in range(12):
    grafo3.insereV()

grafo3.insereA(grafo3.listaVertices[0], grafo3.listaVertices[1]) # A - B
grafo3.insereA(grafo3.listaVertices[1], grafo3.listaVertices[2]) # B - C
grafo3.insereA(grafo3.listaVertices[2], grafo3.listaVertices[3]) # C - D
grafo3.insereA(grafo3.listaVertices[2], grafo3.listaVertices[4]) # C - E
grafo3.insereA(grafo3.listaVertices[2], grafo3.listaVertices[5]) # C - F
grafo3.insereA(grafo3.listaVertices[5], grafo3.listaVertices[6]) # F - G
grafo3.insereA(grafo3.listaVertices[4], grafo3.listaVertices[6]) # D - G
grafo3.insereA(grafo3.listaVertices[6], grafo3.listaVertices[4]) # G - E
grafo3.insereA(grafo3.listaVertices[6], grafo3.listaVertices[7]) # G - H
grafo3.insereA(grafo3.listaVertices[6], grafo3.listaVertices[3]) # G - D
grafo3.insereA(grafo3.listaVertices[7], grafo3.listaVertices[1]) # H - B
grafo3.insereA(grafo3.listaVertices[7], grafo3.listaVertices[8]) # H - I
grafo3.insereA(grafo3.listaVertices[8], grafo3.listaVertices[9]) # I - J
grafo3.insereA(grafo3.listaVertices[9], grafo3.listaVertices[10]) # J - K
grafo3.insereA(grafo3.listaVertices[10], grafo3.listaVertices[0]) # K - A

grafo3.insereA(grafo3.listaVertices[11], grafo3.listaVertices[0]) # L - A
grafo3.insereA(grafo3.listaVertices[11], grafo3.listaVertices[1]) # L - B
grafo3.insereA(grafo3.listaVertices[11], grafo3.listaVertices[7]) # L - H
grafo3.insereA(grafo3.listaVertices[11], grafo3.listaVertices[8]) # L - I
grafo3.insereA(grafo3.listaVertices[11], grafo3.listaVertices[9]) # L - J
grafo3.insereA(grafo3.listaVertices[11], grafo3.listaVertices[10]) # L - K

grafo3.insereA(grafo3.listaVertices[4], grafo3.listaVertices[3]) # E - D
grafo3.insereA(grafo3.listaVertices[4], grafo3.listaVertices[5]) # E - F
grafo3.insereA(grafo3.listaVertices[4], grafo3.listaVertices[6]) # E - G

coloracao5 = Coloracao(grafo3)

coloracao5.colorir()

graphic2(coloracao5)