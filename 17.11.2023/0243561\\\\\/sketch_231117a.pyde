# scale(2)   - увеличивает
# scale(1)   - не меняет
# scale(0.1) - уменьшает
# scale(0)   - исчезает

# Задание 1
# 1. Нарисуй круг размером больше холста.
# 2. Сделай так, чтобы круг уменьшался на 2 за кадр.
# 3. На каждом кадре цвет меняется на случайный. 
# 4. Поменяй скорость уменьшения,
#    убери обводку.
a=1

def setup():
    size(600, 600)
    frameRate(15)
    
def draw():
    noStroke()
    global a
    a=a-0.01
    translate(300,300)
    scale(a) 
    fill(random(0,250),random(0,250),random(0,250))
    ellipse(0,0,700,700)
    
    
    
