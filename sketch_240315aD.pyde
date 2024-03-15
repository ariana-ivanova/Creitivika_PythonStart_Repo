r=0
e=0
def setup():
    size(600, 600)
    background(0)
def draw():
    background(0)
    global r,e
    
    ellipse(300,300, r, e)
    r=r+3
    e=e+3
    if e >= 600: e = 0
    if r >= 600: r = 0
    
    
    if mousePressed:
        background(0)
    #  stroke(random(0,255), random(0,255),random(0,255))
  #   strokeWeight(1)
  #  line(mouseX,mouseY ,pmouseX, pmouseY)
