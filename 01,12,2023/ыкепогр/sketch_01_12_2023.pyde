x = 10

def setup():
    size(600, 600)
    background(255)
    strokeWeight(20)
def draw():
    global x

    colorMode(RGB,255,0,0)# красный
    stroke(255,100,100)
    point(50,x)

    colorMode(RGB,0,255,0)#зеленый
    stroke(255,100,100)
    point(150,x)
    
    colorMode(RGB,0,0,255)#синий
    stroke(255,100,100)
    point(250,x)
    
    colorMode(RGB,255,255,0)#желтый
    stroke(255,100,100)
    point(350,x)

    colorMode(RGB,0,255,255)#берюзовый
    stroke(255,100,100)
    point(450,x)
    
    colorMode(RGB,255,0,255)#розовый
    stroke(255,100,100)
    point(550,x)

    x = x + 1

    if x >= 0:
        noLoop()
