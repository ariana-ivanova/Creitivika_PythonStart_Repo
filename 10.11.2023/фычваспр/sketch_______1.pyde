# Задание 1
# 1. Из центра по косой линии движется точка. 
# 2. Сделай, чтобы это была не точка, а конец линии, начало которой всегда в центре. 
# 3. Не стирай предыдущие кадры. 
# 4. Используй случайный цвет.

x =300
y =300


def setup():
    size(600, 600)  
    background(random(0,255),random(0,255),random(0,255))
    
def draw():
    global x,y
    translate(3, 3)
    strokeWeight(10)
    stroke(random(0,255),random(0,255),random(0,255))
    line(300,300,x,y)
    
    
    
    
    
    
    
    x = x + 5
    y = y + 5


    
