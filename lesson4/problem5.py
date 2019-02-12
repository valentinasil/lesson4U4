from turtle import *

leo=Turtle()

leo.color('purple')
leo.pensize(6)
leo.speed(8)
leo.shape('turtle')

for x in range(20):
	leo.forward(x*10)
	leo.right(144)

mainloop()