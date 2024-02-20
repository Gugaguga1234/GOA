from turtle import *
#we want to paint a house 

color("purple")
#step 1: draw a square 
speed(32)
width(3)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
#end of square 

#building the door 

left(90)
forward(70)
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
# end of drawing the door 

#drawing the roof 

penup()
goto(200, 200)
pendown()
right(150)
forward(200)
left(120)
forward(200)

#end of drawing the roof 

#drawing the windows

penup()
goto(20, 120 )
pendown()
left(120)
forward(45)
left(90)
forward(55)
left(90)
forward(50)
left(90)
forward(55)
left(90)
forward(4)



#end of drawing 1 window

#drawing second one 

penup()
goto(150, 170)
pendown()
left(90)
forward(4)
left(90)
forward(30)
left(90)
forward(55)
left(90)
forward(50)

left(90)
forward(55)
left(90)
forward(30)

# end of drawing windows 

# end of the 1st house 

#drawing second house


penup()
goto(-50, -50)
pendown()
width(5)

#drawing a square2 
forward(180)
left(90)
forward(180)
left(90)
forward(70)
left(90)
forward(90)
right(90)
forward(45)
right(90)
forward(90)
left(90)
forward(65)
left(90)
forward(180)
left(90)
forward(180)
left(90)
forward(180)
left(90)
forward(180)
left(90)
forward(180)
left(45)
forward(150)
left(100)
forward(130)



#end of drawing the roof
# end of drawing the house 
#drawing the tree
color("green")
penup()
goto(-100, 210)
pendown()
left(35)
forward(170)
left(90)
forward(30)
left(90)
forward(170)
color("brown")
left(90)
forward(90)
right(90)
forward(90)
right(90)
forward(130)
right(90)
forward(90)
right(90)
forward(90)
#end of drawing the tree
#drawing the window because i forgot 
penup()
goto(-50, -50)
pendown()
forward(40)
left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)



#end of drawing the second house window



#start drawining the sun
penup()
goto(350,300)
pendown()




import turtle



t =turtle.turtle()


color("yellow")
t.circle(100)

turtle.done()
         
         



exitonclick()




