

def setup():
    size(600, 600)
    background(171,245,240)
    
def draw():
    
    push()
    noStroke()
    rect(-10,400,800,600)#сугроб
    pop()
          #снеговик
    ellipse(450,350,150,150)
    ellipse(450,250,100,100)
    ellipse(450,180,60,60)
          #елка
    push()
    fill(9,108,1)
    triangle(300,200, 100,200, 200,70)
    triangle(300,300, 100,300, 200,170)
    triangle(300,400, 100,400, 200,250)
    pop()
    
    
    
    
    
    
    
    
    
    
    
