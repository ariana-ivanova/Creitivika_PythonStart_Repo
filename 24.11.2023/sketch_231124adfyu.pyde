a=500
def setup():
    size(600,600)
    background(251,136,145)      
    
def draw():
    background(251,136,145) 
    global a
    # translate(0,a)
    strokeWeight(5) 
    line(300,600,300,a)
    fill(255,255,255)
    ellipse(300,a+50,100,100)#верхний
    fill(255,255,255)
    ellipse(350,a,100,100)#справа
    fill(255,255,255)
    ellipse(300,a-50,100,100)#снизу
    fill(255,255,255)
    ellipse(250,a,100,100)#слева
    fill(254,255,0)
    ellipse(300,a,100,100)# центр

    a=a-1
