import turtle

turtle.speed(10)
turtle.color('blue', 'yellow')
turtle.begin_fill()
while True:
    turtle.forward(350)
    turtle.right(200)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()
turtle.done
