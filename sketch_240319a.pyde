x=1
y=1

def setup():
    size(300, 300)
    noFill()
    strokeWeight(5)
    background(255,155,254)
def draw():
    global x,y
    background(255,155,254)
    translate(150,150)
    rectMode(CENTER)
    rotate(radians(x))
    stroke(random(0, 255),random(0, 255),random(0, 255))
    ellipse(y,y,50,50)
    x=x+10
    y=y+1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
