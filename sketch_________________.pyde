x=500
q=500
e=500
a=500
def setup():
    size(1000,1000)
    background(238,10,255)
    
def draw():
    background(238,10,255)
    fill(random(0,270),random(0,280),random(0,230) )
    global x,q,e,a
    x=x-5
    e=e+5
    ellipse(x,x,30,30)
    ellipse(x,e,30,30)
    ellipse(e,e,30,30)
    ellipse(e,x,30,30)
    
    
    
    
    
    
    # push()
    #stroke(100)
    #point(x,300)
    #pop()
