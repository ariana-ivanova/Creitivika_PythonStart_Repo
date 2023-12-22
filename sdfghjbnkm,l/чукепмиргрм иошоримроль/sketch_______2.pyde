y=50

def setup():
    size(600, 600)
    background(171,245,240)
    
def draw():
    global y
    y=y+1
    background(171,245,240)

    push()
    noStroke()
    rect(-10,400,800,600)#сугроб
    pop()
    #снеговик
    ellipse(450,350,150,150)
    ellipse(450,250,100,100)
    ellipse(450,180,60,60)
    # нос
    push()
    fill(255,98,0)
    triangle(410,195, 450,190, 450,200)
    pop()
    # пуговицы
    push()
    strokeWeight(10)
    point(465,180)
    point(440,180)
    point(450,340)
    point(450,290)
    point(450,240)
    pop()

    #снегопад
    push()
    strokeWeight(10)
    stroke(255,255,255)
    point(50,y)
    point(100,y-50)
    point(150,y-29)
    point(200,y-20)
    point(250,y-100)
    point(300,y-30)
    point(350,y-24)
    point(400,y-10)
    point(450,y-25)
    point(500,y-41)
    point(550,y-78)
    
    point(100,y-150)
    point(150,y-290)
    point(200,y-200)
    point(250,y-170)
    point(300,y-330)
    point(350,y-324)
    point(400,y-361)
    point(450,y-295)
    point(500,y-441)
    point(550,y-178)
    
    point(100,y-548)
    point(150,y-629)
    point(200,y-920)
    point(250,y-750)
    point(300,y-658)
    point(350,y-524)
    point(400,y-710)
    point(450,y-777)
    point(500,y-532)
    point(550,y-927)
    
    point(100,y-1592)
    point(150,y-1234)
    point(200,y-1111)
    point(250,y-1206)
    point(300,y-1002)
    point(350,y-1138)
    point(400,y-1196)
    point(450,y-1342)
    point(500,y-1198)
    point(550,y-1369)
    
    pop()
    negovik= loadImage("negovik.png")
    image(negovik,250,80,400,400)
    
    elka = loadImage("elka.png")
    image(elka,0,80,300,400)
    
    
