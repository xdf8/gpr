from turtle import forward, left, done

def draw_turtle(list):
    for item in list:
        left(item[0])
        forward(item[1])
    done()



draw_turtle([(0, 30), (60, 50), (-120, 50), (60, 30)])