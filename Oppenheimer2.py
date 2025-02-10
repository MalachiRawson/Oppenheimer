import turtle

jeff = turtle.Turtle()
wn = turtle.Screen()

#-425,300
topLeft = [-425,300]

jeff.speed(5)
jeff.pensize(5)
jeff.color('blue')
wn.bgcolor('green')

def drawCircle(t,sz):
    jeff.penup()
    jeff.goto(topLeft)
    jeff.pendown()
    jeff.circle(sz)
    topLeft[0] = topLeft[0]+100

def circleLine(t,sz):
    for a in range(2):
        topLeft[0] = -425
        for i in range(2):
            drawCircle(t,sz)
            topLeft[1] = topLeft[1]-100
        topLeft[0] = -425


circleLine(jeff,50)