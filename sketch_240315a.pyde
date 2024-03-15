
def setup():
    size(1000,800)
    background(0)
def draw():
    stroke(255)
    strokeWeight(5)
    point(random(0,1000),random(0,800))
    if mousePressed:
        background(0)
    
  #  stroke(random(0,255), random(0,255),random(0,255))
  #   strokeWeight(1)
  #  line(mouseX,mouseY ,pmouseX, pmouseY)
