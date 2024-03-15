r=0
e=0
def setup():
    size(600, 600)
    background(0)
    global r,e
def draw():
    if mousePressed:
        if mouseButton==LEFT :  
            global r,e
            background(0)
            ellipse(300,300, r, e)
            r=r+3
            e=e+3
            if e >= 600: e = 0
            if r >= 600: r = 0
    #  stroke(random(0,255), random(0,255),random(0,255))
  #   strokeWeight(1)
  #  line(mouseX,mouseY ,pmouseX, pmouseY)
