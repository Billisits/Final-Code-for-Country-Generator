import turtle
import os
import time
from random import random
from random import randint
from random import choice
t = turtle.Turtle()
s = turtle.Screen()
r = random()
c = turtle.Turtle()
c.hideturtle()
c.penup()
s.colormode(255)

t.hideturtle()
t.penup()
t.color("Black")
t.pencolor("Black")
t.shape("circle")
s.bgcolor(200,200,200)
t.speed(0)
t.goto(0,-60)
shapes = ["arrow", "turtle", "circle", "square", "square", "triangle", "classic"]

#numShapes = randint(1,2)
numShapes = 1

sum = 0
imp = 0

while sum < numShapes:
#while False:
  #time.sleep(1)
  t.begin_fill()
  t.pendown()
  t.lt(r * 120 - 20)
  t.fd(r * 30 + (imp * imp)/5000)
  imp = imp + 1
  x = t.xcor()
  y = t.ycor()
  r = random()
  t.goto(0,0)
  t.end_fill()
  t.goto(x,y)
  t.begin_fill()
  #print (x)
  #print (y)
  #print ("")
  if sum == 0:
    if imp == 10:
      xc = t.xcor()
      yc = t.ycor()
      c.color(255,0,0)
      c.goto(xc,yc)
  if (x*x + (y+60)*(y+60)) > 10000:
    t.goto(0,-60)
    t.end_fill()
    sum = sum + 1
    imp = 0
    #rr = random() * 255
    #gg = random() * 255
    #bb = random() * 255
    #t.color(rr,gg,bb)
    #t.fillcolor(rr,gg,bb)
    #rr = 255 - random() * 100
    #gg = 255 - random() * 100
    #bb = 255 - random() * 100
    #s.bgcolor(rr,gg,bb)
t.hideturtle()
t.penup()

prefix = ["Kingdom of", "Central", "Middle", "Federation of", "The", "United States of", "Democratic Republic of", "East", "North", "South", "West", "Democratic Free People's Republic of", "Free State of", "Commonwealth of", "", "", "", "", "", "New", "Empire of"]
name1 = ["Danq", "Scot", "Tyr", "Cr", "St", "Cauc", "Kurd", "Mor", "Alab", "St. P", "Ch", "Sherm", "Lee-Dav", "Brad", "Grant", "Mac", "Scott", "F", "C", "G", "H", "J", "K", "L", "M", "P", "R", "S", "T", "W", "X", "Z", "Dak", "Car", "Sag", "Beaver", "B", "Eis", "Oak", "Lex", "Galv", "Simp", "Lib", "Leb", "Monr", "Arst", "D", "Gen", "Riv", "Whit", "Afr", "Isr", "Par", "Br", "Russ", "Y", "Kak", "Nar", "Jot", "Avd", "Val", "El Dor", "Austr", "Chin", "Patag", "Ne", "Holl", "All", "Pen", "Sw", "Fin", "Turk", "Constant", "Bor", "Kaz", "Mex", "V", "N", "Ytterb", "Eur", "Tan", "Jap", "Kyl", "Cyd", "Wall", "Nether", "Van de W", "Calif", "Brit", "Amer", "Penns", "Fr", "Frank", "Ger", "Pan-", "Al-", "Great T", "Den", "Can"]
name2 = ["uah", "oil", "ica", "ioh", "ama", "ester", "esterton", "anton-by-the-River", "akota", "olina", "isi", "ton", "engard", "erborough", "embourg", " Island", "opol", "ingrad", "erpool", "orcestershire", "otska", "ayah", "io", "ancia", "encia", "aro", "ol", "ympia", "obi", "all", "alia", "ado", "alia", "erland", "opolis", "ian Lands", "edonia", "yria", "-cake", "is", "eden", "inland", "ete", "os", "inople", "enistan", "istan", "an", "oland", "land", "a", "ussia", "asia", "on", "aton", "ert", "ia", "ornia", "ylvania", "ada", "iver", "io-Verona", "onia", "atavia", "anon", "estine", "exico"]

t.goto(-150,160)
t.write(str(str(choice(prefix)) + " " + str(choice(name1)) + str(choice(name2))))

t.home()
t.goto(-150,90)

sum2 = 0
vert = randint(0,3)
tri = randint(0,1)

rr = int(random() * 255)
gg = int(random() * 255)
bb = int(random() * 255)

ff = rr
hh = gg
ii = bb

if vert == 0:
  while sum2 < 3:
    t.color(rr,gg,bb)
    t.fillcolor(rr,gg,bb)
    if tri == 0:
      if sum2 ==2:
        t.color(ff,hh,ii)
        t.fillcolor(ff,hh,ii)
    t.begin_fill()
    t.fd(30)
    t.lt(90)
    t.fd(60)
    t.lt(90)
    t.fd(30)
    t.lt(90)
    t.fd(60)
    t.lt(90)
    t.end_fill()
    rr = int(random() * 255)
    gg = int(random() * 255)
    bb = int(random() * 255)
    t.fd(30)
    sum2 = sum2 + 1
    
if vert == 1:
  t.lt(90)
  while sum2 < 3:
    t.color(rr,gg,bb)
    t.fillcolor(rr,gg,bb)
    if tri == 0:
      if sum2 == 2:
        t.color(ff,hh,ii)
        t.fillcolor(ff,hh,ii)
    t.begin_fill()
    rr = int(random() * 255)
    gg = int(random() * 255)
    bb = int(random() * 255)
    t.fd(20)
    t.rt(90)
    t.fd(90)
    t.rt(90)
    t.fd(20)
    t.rt(90)
    t.fd(90)
    t.end_fill()
    t.rt(90)
    t.fd(20)
    sum2 = sum2 + 1
  t.rt(90)
  
if vert == 2:
  t.color(rr,gg,bb)
  t.fillcolor(rr,gg,bb)
  t.begin_fill()
  t.fd(90)
  t.lt(90)
  t.fd(60)
  t.lt(90)
  t.fd(90)
  t.lt(90)
  t.fd(60)
  t.lt(90)
  t.end_fill()
  rr = int(random() * 255)
  gg = int(random() * 255)
  bb = int(random() * 255)
  t.color(rr,gg,bb)
  t.fillcolor(rr,gg,bb)
  t.begin_fill()
  t.fd(10)
  t.lt(32.00538321)
  t.fd(94.33981132)
  t.lt(57.99461679)
  t.fd(10)
  t.lt(90)
  t.fd(10)
  t.lt(32.00538321)
  t.fd(94.33981132)
  t.lt(57.99461679)
  t.fd(10)
  t.lt(90)
  t.end_fill()
  t.lt(90)
  t.fd(60)
  t.rt(90)
  t.begin_fill()
  t.fd(10)
  t.rt(32.00538321)
  t.fd(94.33981132)
  t.rt(57.99461679)
  t.fd(10)
  t.rt(90)
  t.fd(10)
  t.rt(32.00538321)
  t.fd(94.33981132)
  t.rt(57.99461679)
  t.fd(10)
  t.rt(90)
  t.end_fill()
  
undouble = False

if vert == 3:
  t.color(rr,gg,bb)
  t.fillcolor(rr,gg,bb)
  t.begin_fill()
  t.fd(90)
  t.lt(90)
  t.fd(60)
  t.lt(90)
  t.fd(90)
  t.lt(90)
  t.fd(60)
  t.lt(90)
  t.end_fill()
  t.goto(-105,120)
  rr = random() * 255
  gg = random() * 255
  bb = random() * 255
  undouble = True
  
t.goto(-150,70)
t.color("Black")
t.write("Population: " + str(randint(1,1000000)))
t.goto(-150,50)
t.write("WHO Development Ranking: " + str(randint(1,205)))

t.color(rr,gg,bb)

t.goto(-105,120)

t.lt(90)
rr = int(random() * 255)
gg = int(random() * 255)
bb = int(random() * 255)
t.color(rr,gg,bb)
emblem = choice(shapes)
if emblem == "arrow":
  t.fd(-5)
if emblem == "square":
  if randint(0,1) == 1:
    t.rt(45)
if emblem == "classic":
  t.fd(5)
if emblem == "triangle":
  t.fd(-3)
if emblem == "turtle":
  t.fd(-2)
t.shape(emblem)
shows = randint(0,1)
if (shows == 1 or undouble ==True):
  t.showturtle()

c.begin_fill()
c.circle(2)
c.end_fill()
c.fd(5)
c.write(str(choice(name1)) + str(choice(name2)))
