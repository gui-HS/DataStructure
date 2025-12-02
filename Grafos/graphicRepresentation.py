import turtle
from grafo import Grafo

def graphic(grafo):
    t = turtle.Turtle()
    # https://www.geeksforgeeks.org/python/draw-any-polygon-in-turtle-python/

    # This will be used to draw the edges
    listPosition = list()

    # Draw Vectors
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
        
        v1Position = listPosition[v1.nome]
        v2Position = listPosition[v2.nome]

        t.setpos(v1Position)
        t.pendown()
        t.goto(v2Position)
        t.penup()
        print(v1,v2)

    turtle.done()


grafo1 = Grafo()
for i in range(25):
    grafo1.insereV()

grafo1.insereA(grafo1.listaVertices[0], grafo1.listaVertices[12])
grafo1.insereA(grafo1.listaVertices[12], grafo1.listaVertices[2])
grafo1.insereA(grafo1.listaVertices[2], grafo1.listaVertices[3])

graphic(grafo1)
