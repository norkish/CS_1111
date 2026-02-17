import turtle

def draw_polygon(turt, num_sides, side_len):
    """draw a square"""
    for side in range(num_sides):
        turt.forward(side_len)
        turt.left(360/num_sides)


window = turtle.Screen()

alex = turtle.Turtle()
alex.speed(9)
for i in range(36):
    draw_polygon(alex, i, i * 5)
    # rotate 10 before next square
    alex.left(20)

window.exitonclick()
