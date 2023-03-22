from turtle import *
color("green","black")
begin_fill()
while 1:
    forward(250)
    left(170)
    if abs(pos())<1:
       break
end_fill()
done()