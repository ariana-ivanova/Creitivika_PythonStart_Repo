
lamborghini=20
mercedes=20
melodi=20
def setup():
    global dom,mercedes,kuromi
    size(800,600)

    kitti = loadImage("lamborghini.png")
    kuromi = loadImage("mercedes.png")
    melodi = loadImage("melodi.png")
def draw():
    global dom,mercedes,melodi
    image(mercedes,0,0,800,600)
    image(kitti,280,180,130,100)
    image(kuromi,480,230,90,100)

    
