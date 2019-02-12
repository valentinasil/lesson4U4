from turtle import *

leo=Turtle()
almond= Turtle()

leo.color('purple')
leo.pensize(6)
leo.speed(8)
leo.shape('turtle')

for x in range(3):
	leo.forward(100)
	leo.left(120)

almond.color('green')
almond.pensize(5)
almond.speed(4)
almond.shape('turtle')

almond.circle(50)


mainloop()