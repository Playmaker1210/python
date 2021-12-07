import turtle

a = turtle.Screen()
a.bgcolor('green')
a.title('Negyzet')

teknos = turtle.Turtle()
teknos.shape('turtle')
teknos.speed(100)
teknos.color('black')
def negyzet(t, n):
    for i in range(4):
        t.forward(n)
        t.left(90)

n = 20
x = 0
y = 0

for i in range(5):
    negyzet(teknos, n)
    n += 20
    x += -10
    y += -10
    teknos.penup()
    teknos.goto(x, y)
    teknos.pendown()
    
a.mainloop()
