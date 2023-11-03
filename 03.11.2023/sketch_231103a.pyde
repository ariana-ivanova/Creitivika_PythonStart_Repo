x=1
y=12

def setup():
    size(1000,1000)
    background(238,10,255)
    
def draw():
    global x,y
    x=x+5
    y=y+5
    strokeWeight(20)
    point(x,y)
    stroke(random(0,187),random(0,205),random(0,250))
    
    
    
    # push()
    #stroke(100)
    #point(x,300)
    #pop()
