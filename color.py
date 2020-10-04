import turtle


colors = ['red','purple','blue','green','orange','yellow']
t = turtle.Pen()
t.speed(100)
turtle.bgcolor("Black")
for x in range(360):
	t.pencolor(colors[x%6])
	t.width(x/100+1)
	t.forward(x)
	t.left(59)

for i in range(360,0,-1):
	t.pencolor(colors[i%6])
	t.width(i/100+1)
	t.forward(i)
	t.left(59)



turtle.done()
