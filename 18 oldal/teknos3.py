import turtle       
        
#ablak
a = turtle.Screen()
a.bgcolor("white")
a.title("Negyzet")

#rajzeszkoz
Eszti = turtle.Turtle()
Eszti.forward(40)

for i in range(18):
    turtle.forward(45)
    turtle.right(360 / 18)

a.mainloop()