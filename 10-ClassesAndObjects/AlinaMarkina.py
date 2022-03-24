import turtle as tur
from turtle import Turtle, Screen
import random
class Shapes(Turtle):
    def __init__(self):
        super().__init__(shape='turtle', visible=False)
        tur.bgcolor("AntiqueWhite3")
        self.penup()
        self.speed("fastest")
        arr = ["Cyan", "Blue", "Salmon", "Pink", "Goldenrod"]
        self.array = ["burlywood", f"burlywood{random.randint(1, 4)}",
                      "cornsilk", f"cornsilk{random.randint(1, 4)}", "azure", f"azure{random.randint(1, 4)}",
                      "coral", f"coral{random.randint(1, 4)}", "gray", f"gray{(random.randint(3, 9))*10}",
                      f"Light{random.choice(arr)}", f"Light{random.choice(arr)}{random.randint(1, 2)}",
                      f"LavenderBlush", f"LavenderBlush{random.randint(1, 4)}", "honeydew", f"honeydew{random.randint(1, 4)}",
                      "PeachPuff", f"PeachPuff{random.randint(1, 4)}"]
        
    def circle(self):
        self.speed(0)
        tur.pensize(3)
        def cir(a, b):
            self.c = random.randint(50, 90)
            tur.penup()
            tur.goto(self.c+a, self.c+b)
            tur.pendown()
            tur.pencolor(random.choice(self.array))
            tur.fillcolor(random.choice(self.array))
            tur.begin_fill()
            tur.circle(self.c)
            tur.end_fill()
        cir(-420, -225)
        cir(-420, 25)
        cir(300, 25)
        cir(300, -225)
    
    def star(self, a, b):
        self.a = a
        self.b = b
        tur.penup()
        tur.goto(self.a-144, self.b+200)
        tur.pendown()
        tur.pensize(4)
        for i in range(5):
            tur.pencolor(random.choice(self.array))
            tur.forward(200)
            tur.right(144)
            
    def heart(self):
        tur.up()
        tur.goto(0,0)
        tur.down()
        tur.pensize(3)
        def curve():
            for i in range(200):
                tur.right(1)
                tur.forward(1)
        tur.fillcolor(f'LightPink{random.randint(1, 4)}')
        tur.begin_fill()
        tur.left(140)
        tur.forward(113)
        curve()
        tur.left(120)
        curve()
        tur.forward(112)
        tur.end_fill()
        
    def hexagon(self, a, b):
        self.a = a
        self.b = b
        tur.up()
        tur.goto(self.a, self.b)
        tur.down()
        tur.pensize(4)
        tur.fillcolor(random.choice(self.array))
        tur.begin_fill()
        for i in range(6):
            tur.pencolor(random.choice(self.array))
            tur.forward(102)
            tur.left(300)
        tur.end_fill()
            
    def crescent(self, a, b):
        self.a = a
        self.b = b
        tur.penup()
        tur.goto(self.a, self.b)
        tur.begin_fill()
        tur.color("MistyRose")
        tur.circle(100)
        tur.end_fill()
        tur.up()
        if int(self.a)>0:
            tur.goto((self.a)+45, self.b)
        elif int(self.a)<0:
            tur.goto((self.a)-45, self.b)
        elif int(self.b)>0:
            tur.goto(self.a, (self.b)+45)
        else:
            tur.goto(self.a, (self.b)-45)
        tur.begin_fill()
        tur.color("AntiqueWhite3")
        tur.circle(100)
        tur.end_fill()
    
    #drawing a resulting picture 
    def draw_pic(self):
        #4 moons in 4 different corners
        self.crescent(-800, -100)
        self.crescent(800, -100)
        self.crescent(0, 300)
        self.crescent(0, -500)
        
        #4 stars with random side colours after each moon
        self.star(-550, 100)
        self.star(350, 210)
        self.star(700, -400)
        self.star(-250, -550)
        
        #4 hexagons with random side colours after each star
        self.hexagon(-350, 475)
        self.hexagon(550, 350)
        self.hexagon(300, -295)
        self.hexagon(-620, -125)

        #4 circles with random side colours and positions around the flower
        self.circle()

        #flower from 5 colourful hearts in center
        for i in range(1,6):
            self.heart()

    #personal data in the upper right corner
    def draw_name(self):
        tur.up()
        tur.setpos(750, 400)
        tur.down()
        tur.color('white')
        style = ('Verdana', 16, 'bold')
        tur.write("Alina Markina\nZZISS1-1112", font=style)
        
sh = Shapes()
sh.draw_pic()
sh.draw_name()
sc = Screen()
sc.exitonclick()
