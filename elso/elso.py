import turtle

def negyzet_rajzolas(t, h):
    for i in range(4):
        t.forward(h)
        t.left(90)
        
        
#ablak
a = turtle.Screen()
a.bgcolor("white")
a.title("Negyzet")

#rajzeszkoz
toll = turtle.Turtle()
negyzet_rajzolas(toll, 50)

a.mainloop()