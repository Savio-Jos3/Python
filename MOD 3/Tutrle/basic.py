import turtle

# Create a turtle screen (the window where drawing happens)
screen = turtle.Screen()  

# Set the background color of the screen
screen.bgcolor("white")  

# Create a turtle object
t = turtle.Turtle()  

# Set the shape of the turtle (options: "arrow", "turtle", "circle", "square", etc.)
t.shape("turtle")  

# Set the drawing color (pen color)
t.color("blue")  

# Set the fill color (for shapes)
t.fillcolor("yellow")  

# Set the width of the pen
t.pensize(3)  

# Move the turtle forward by a given number of units (pixels)
t.forward(100)  

# Move the turtle backward by a given number of units
t.backward(50)  

# Turn the turtle clockwise by given angle
t.right(90)  

# Turn the turtle counter-clockwise by given angle
t.left(45)  

# Move turtle to a specific (x, y) coordinate
t.goto(0, 0)  

# Draw a circle with a given radius
t.circle(50)  

# Lift the pen (so it doesn’t draw while moving)
t.penup()  

# Lower the pen to resume drawing
t.pendown()  

# Start filling the shape drawn after this call
t.begin_fill()  

# End filling the shape (must match a begin_fill())
t.end_fill()  

# Clear the entire drawing (turtle stays in place)
t.clear()  

# Reset turtle to initial position and clear drawing
t.reset()  

# Hide the turtle cursor (for cleaner visuals)
t.hideturtle()  

# Show the turtle cursor (if hidden)
t.showturtle()  

# Set turtle drawing speed (1 slow – 10 fast or "fastest")
t.speed(5)  

# Write text at current turtle location
t.write("Hello", font=("Arial", 16, "normal"))  

# Stop the window from closing immediately
screen.mainloop()  
