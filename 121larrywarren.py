# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random


#-----game configuration----

shape = "turtle"
size = 2
color = "red"
score = 0

timer = 15
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----

Dante = trtl.Turtle(shape = shape)
Dante.color(color)
Dante.shapesize(size)
Dante.speed(0)

Counter = trtl.Turtle()
Counter.ht()
Counter.penup()
Counter.goto(-370,270)
font_setup = ("Comic Sans" , 30 , "bold")

counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(260,270)


#-----game functions--------

def turtle_clicked(x,y):
    print("Dante was clicked")
    changed_position()
    score_counter()
    size_change()

def changed_position():
    Dante.penup()
    Dante.ht()
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(-300,300)
    Dante.goto(new_xpos , new_ypos)
    Dante.st()

def size_change():
    new_size = random.randint(1,7)
    Dante.shapesize(new_size)


def score_counter():
    global score
    score += 1
    print(score)
    Counter.clear()
    Counter.write(score , font=font_setup)
  
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.goto(0,-50)
    counter.write("You suck. .", font=font_setup)
    timer_up = True
    game_over()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)


def game_over():
    wn.bgcolor("Red")
    Dante.ht()
    Dante.goto(500,500)

#-----events----------------
Dante.onclick(turtle_clicked)



wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
