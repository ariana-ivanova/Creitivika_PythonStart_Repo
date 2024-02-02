mercedes=300
lamborghini=20

def setup():
    global mercedes,lamborghini
    size(800,600)
    mercedes= loadImage("mercedes.png")
    lamborghini = loadImage("lamborghini.png")

def draw():
    global mercedes,lamborghini
    image(mercedes,0,0,800,600)
    image(lamborghini,280,180,130,100)

    
    
    
