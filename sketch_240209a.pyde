e=0
mode="вправо"
y=0

def setup():
    size(600,600)

def draw():
    global e,mode,y
    translate(300,300)
    frameRate(100)
    rotate(y)
    fill(random(0,255),random(0,255),random(0,255))
    rect(0,0,e,e)  
    
    if mode== "вправо":
        e=e+3
        y=y+5
        #rotate(radians(180))
    if mode== "влево":
        e=e-3
        y=y-5
        #rotate(radians(180))
    if e>=600:
        mode= "влево"
   
    if e<=0:
        mode= "вправо"
     
   
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
