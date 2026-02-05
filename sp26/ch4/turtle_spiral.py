import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(5)
alex.shape("turtle")

# draw a series of squares, each slightly rotated
for x in range(36):
    # draw one square
    for i in range(4):
        alex.forward(200)
        alex.left(90)
    alex.right(10)

wn.exitonclick()
