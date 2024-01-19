x=1
def setup():
    size(300, 300)
    noFill()
    strokeWeight(5)
    
def draw():
    global x
   # background(255,155,254)
    translate(150,150)
    rectMode(CENTER)
    rotate(radians(x))
    stroke(random(0, 255),random(0, 255),random(0, 255))
    line(0,0,50,50)
    x=x+1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
