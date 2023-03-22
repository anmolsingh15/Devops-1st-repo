import turtle
wn=turtle.Screen()
wn.bgcolor("light green")
p=turtle.Turtle()
p.color("blue")
def func(size):
    for x in range(14):
        p.fd(size)
        p.left(90)
        size=size +15
func(6)
func(36)
func(42)
func(46)
func(56)
func(86)
func(136)