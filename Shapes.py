import turtle
turtle.Screen().bgcolor("Green")

board = turtle.Turtle()

# triangle

board.forward(100)
board.right(120)
board.forward(100)
board.right(120)
board.forward(100)
board.right(45)
board.penup()
board.goto(50,100)

# square
board.pendown()
board.forward(100)
board.left(90)
board.forward(100)
board.left(90)
board.forward(100)
board.left(90)
board.forward(100)
board.left(90)
