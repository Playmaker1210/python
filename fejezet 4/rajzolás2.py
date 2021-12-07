import turtle

def negyzet(t):
    for i in range(4):
        t.forward(100)
        t.left(90)

ablak = turtle.Screen()
ablak.title("Gyönyörű minta")
ablak.bgcolor("green")

teknos = turtle.Turtle()
teknos.color("blue")
teknos.pensize(3)
teknos.speed(10)

for i in range(20):
    negyzet(teknos)
    teknos.left(18)

ablak.mainloop()