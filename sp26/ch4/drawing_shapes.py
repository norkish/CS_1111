import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(10)
alex.shape("turtle")

# square
# for i in [0, 1, 2, 3]:
#     alex.forward(50)
#     alex.left(90)

# # triangle
# for i in [0, 1, 2]:
#     alex.forward(175)
#     alex.left(120)

# pentagon
# for i in [0, 1, 2, 3, 4]:
#     alex.forward(75)
#     alex.left(72)

# pentagon with range
# for i in range(5):
#     alex.forward(75)
#     alex.left(72)

side_count = int(input("How many sides for ya? "))
alex.left(180)
# polygon w/ arbitrary # of sides using range function
for i in range(side_count):
    alex.forward(1)
    alex.right(360/side_count)

wn.exitonclick()
