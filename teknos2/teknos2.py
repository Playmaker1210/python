import turtle       
        
#ablak
a = turtle.Screen()
a.bgcolor("white")
a.title("Negyzet")

#rajzeszkoz
Eszti = turtle.Turtle()
Eszti.left(60)
Eszti.forward(100)
Eszti.left(240)
Eszti.forward(100)
Eszti.left(240)
Eszti.forward(100)
#negyzet
Eszti.forward(100)
Eszti.left(90)
Eszti.forward(100)
Eszti.left(90)
Eszti.forward(100)
Eszti.left(90)
Eszti.forward(100)
#hexagon
for i in range(6):
    Eszti.forward(90)
    Eszti.left(300)
    
#oktagon
for i in range(8):
    Eszti.forward(100)
    Eszti.left(45)


a.mainloop()