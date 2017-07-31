# import turtle

# turtle.shape('square')
# turtle.goto(0,100)
# turtle.goto(100,100)
# turtle.goto(100,0)
# turtle.goto(0,0)

# triangle = turtle.clone()
# triangle.shape('triangle')
# triangle.penup()
# triangle.goto(-100,-100)
# triangle.pendown()
# triangle.goto(-100,-50)
# triangle.goto(-50,-100)
# triangle.goto(-100,-100)


# turtle.mainloop()

import turtle


turtle.shape('square')
turtle.goto(0,100)
turtle.stamp()
turtle.goto(100,100)
turtle.stamp()
turtle.goto(100,0)
turtle.stamp()
turtle.goto(0,0)
turtle.stamp()

triangle = turtle.clone()
triangle.shape('triangle')
triangle.penup()
triangle.goto(-100,-100)
triangle.pendown()
triangle.stamp()
triangle.goto(-100,-50)
triangle.stamp()
triangle.goto(-50,-100)
triangle.stamp()
triangle.goto(-100,-100)
