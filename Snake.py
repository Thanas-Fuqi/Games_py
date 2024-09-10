#Importing the needed modules
import random
import turtle
import time
turtle.tracer(0, 0)
turtle.colormode(255)
screen = turtle.Screen()

#Variables of the program
track_score = 0
num_square = 9
step_size = 21
turtles = []
action = [2] #Right

#Border and font declaration
dist = num_square *step_size +step_size/2
style = ('Courier', 25, 'italic')

#Direction vectors
directions = [
  (0, step_size), #Up
  (0,-step_size), #Down
  (step_size, 0), #Right
  (-step_size,0)  #Left
]

#New body piece function
def new_body():
  body = turtle.Turtle()
  body.shape("square")
  body.shapesize(1)
  body.speed(0)
  body.penup()
  return body

#Moving the apple on the screen  
def move_apple():
  x = random.randint(-num_square, num_square) 
  y = random.randint(-num_square, num_square)
  used = [t.pos() for t in turtles]
  while (x*step_size, y*step_size) in used: 
    x = random.randint(-num_square, num_square) 
    y = random.randint(-num_square, num_square) 
  apple.goto(x*step_size, y*step_size)

  apple.color(
    random.randint(10, 255),
    random.randint(10, 255),
    random.randint(10, 255)
  )

#Keep track of the score
def write_score():
  #Clearing the old score
  track.color("white")
  track.write(chr(9608).join(
    [chr(9608) for i in range(10)]
  ), font=style, align="right")
  #Writing the new score
  track.color("black")
  track.write(
    "Score :"+str(track_score),
    font=style, align='right'
  )

#Drawing lines of the grid
def grid_drawer():
  one, two = 0, 90
  for i in range(2):
    for j in range(num_square*2+1):
      for k in range(2):
        track.setheading(two)
        track.forward(dist*2)
        track.backward(dist*2)  
        track.setheading(one)
      track.forward(step_size)
    one, two = 90, 180
  track.setheading(two)
  track.forward(dist*2)
  
#Creating the Head and Apple
head, apple = new_body(), new_body()
turtles.append(head)
move_apple()
turtles.append(apple)

#Creating the drawer
track = new_body()
track.hideturtle()
track.color("red")
track.width(10)

#Creating a square 
track.goto(-dist-5, -dist-5)
track.pendown()
track.goto( dist+5, -dist-5)
track.goto( dist+5,  dist+5)
track.goto(-dist-5,  dist+5)
track.goto(-dist-5, -dist-5)
track.goto(-dist, -dist)

#Creating a grid 
track.width(1)
track.speed(0)
track.color("orange")
grid_drawer()

#Setting the track
track.penup()
x, y = track.pos()
track.goto(x+285, y+20)

write_score()
turtle.update()

#Main loop of the game
def begin():
  global track_score, action
  while True:
    X, Y = head.pos()
    x, y = apple.pos()

    #Checking if the apple was hit
    if (X, Y) == (x, y):
      track_score += 1
      write_score()
      move_apple()
      turtles.append(new_body())
      action.insert(0, 0)

    #Increment the X, Y for next pos
    dx, dy = directions[action[-1]]
    X += dx 
    Y += dy

    if X<-dist or X>dist or Y<-dist or Y>dist:
      break #Break if wall is hitted
    if (X, Y) in [t.pos() for t in turtles[2:]]:
      break #Break if self-collide

    head.goto(X, Y) #Move the head
    action.append(action[-1])
    action.pop(0)
    #Move the body of the snake
    for i in range(2, len(turtles)):
      dx, dy = directions[action[-i]]
      turtles[i].goto(X-dx, Y-dy)
      X, Y = turtles[i].pos()

    turtle.update()
    time.sleep(0.1)

#Key Press function declaration
def moveUp():
  action[-1] = 0
def moveDown():
  action[-1] = 1
def moveRight():
  action[-1] = 2
def moveLeft():
  action[-1] = 3

#Key Press bindings to keyboard
screen.onkey(moveUp, "Up")
screen.onkey(moveDown, "Down")
screen.onkey(moveRight, "Right")
screen.onkey(moveLeft, "Left")
screen.onkey(begin, "b")
screen.listen()
