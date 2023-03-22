import turtle
colors=["blue","red","green","pink","orange","yellow","purple"]
t=turtle.Pen()
turtle.bgcolor("black")
for x in range(600):
    t.pencolor(colors[x%7])
    t.width(x/10+1)
    t.forward(x)
    t.left(59)