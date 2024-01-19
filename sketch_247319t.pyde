x=0
e=40
def setup():
    size(800,800)
    # noFill()
    strokeWeight(5)
    background(255,155,254)
def draw():
    global x,e
    
    translate(400,400)
    rotate(radians(e))
    
    rotate(radians(x))
    
    stroke(random(0, 255),random(0, 255),random(0, 255))
    triangle(10+90,40, 10+90,-40, 150+90,0)

    x=x+40
    if frameCount%8:
       # background(255,155,254)
        e=e+5
    
    
    
    
    
    
    
    
    
    
    
    
    
