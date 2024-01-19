x=1
y=1
e=5
def setup():
    size(300, 300)
    noFill()
    strokeWeight(5)
    background(255,155,254)
def draw():
    global x,y,e
  #  background(255,155,254)
    translate(150,150)
    rectMode(CENTER)
    rotate(radians(x))
    stroke(random(0, 255),random(0, 255),random(0, 255))
    ellipse(y,y,e,e)
    x=x+10
    y=y+1
    e=random(0,20)
    
    
    
    
    
    
    
    
    
    
    
    
    
