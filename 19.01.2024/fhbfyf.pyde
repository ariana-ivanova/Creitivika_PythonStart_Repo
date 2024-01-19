dom=300
kitti=20
kuromi=20
melodi=20
def setup():
    global dom,kitti,kuromi,melodi
    size(800,600)
    dom = loadImage("dom.jpg")
    kitti = loadImage("kitti.png")
    kuromi = loadImage("kuromi.png")
    melodi = loadImage("melodi.png")
def draw():
    global dom,kitti,kuromi,melodi
    image(dom,0,0,800,600)
    image(kitti,280,180,130,100)
    image(kuromi,480,230,90,100)
    image(melodi,450,330,160,100)
    
    
    
    
    
    
    
    
    
    
