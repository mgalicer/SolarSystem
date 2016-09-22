#Mari Galicer ^_^

import turtle
import math
import random

def randcolor():
  r = lambda: random.randint(0,255)
  return '#%02X%02X%02X' % (r(),r(),r())

class SolarSystem():
  def __init__(self):
    self._sun = Sun((0,0), 100, "yellow")
    self._planets = [] #change variables to start with _
    self._lastClicked = None

    for i in range(random.randint(3,6)):
      planet = Planet(self._sun, random.randint(100, 350), random.randint(20, 70), randcolor(), random.uniform(0.009, 0.02))
      for i in range(random.randint(0,4)):
        moon = Planet(planet, random.randint(30, 60), random.randint(5, 20), randcolor(), random.uniform(0.04, 0.08))
        self._planets.append(moon)
      self._planets.append(planet)

  def draw(self):
    self._sun.draw()
    for p in self._planets:
      p.draw()
      p.move()

  def onClick(self, coords):
    if self._sun.onClick(coords):
      self._lastClicked = self._sun
    for p in self._planets:
      if p.onClick(coords):
        self._lastClicked = p

  def Up(self):
    if self._lastClicked:
      self._lastClicked._size += 10

  def Down(self):
    if self._lastClicked > 11:
      self._lastClicked._size -= 10

  def Left(self):
    if self._lastClicked and self._lastClicked != self._sun:
      if self._lastClicked._orbitRadius > 10:
        self._lastClicked._orbitRadius -= 10

  def Right(self):
    if self._lastClicked and self._lastClicked != self._sun:
      self._lastClicked._orbitRadius += 10

  def leftBracket(self):
    if self._lastClicked:
      self._lastClicked._speed += 0.01

  def rightBracket(self):
    if self._lastClicked:
      if self._lastClicked._speed > 0:
        self._lastClicked._speed -= 0.01

  def newMoon(self):
    if self._lastClicked:
      moon = Planet(self._lastClicked, random.randint(30, 60), random.randint(5, 20), randcolor(), random.uniform(0.04, 0.08))
      self._planets.append(moon)

  def changeColor(self):
    if self._lastClicked:
      self._lastClicked._color = randcolor()

class Sun:
  def __init__(self,center,size,color):
    self._center = center
    self._size = size
    self._color = color

  def setColor(self):
    self._color = randcolor()

  def inside(self, location):
    if ((location[0] - self._center[0])**2 + (location[1] - self._center[1])**2 < ((self._size/2)**2)):
      return True

  def onClick(self, location):
    if self.inside(location):
      self.setColor()
      return True

  def getCenter(self):
    return self._center

  def draw(self):
    turtle.penup()
    turtle.goto(self._center)
    turtle.dot(self._size, self._color)
    # self._size is diameter

class Planet(Sun):
  def __init__(self, orbitAround, orbitRadius, size, color, speed):
    self._orbitAround = orbitAround
    self._orbitRadius = orbitRadius
    self._speed = speed
    self._angle = 0
    #size and color are inherited from Sun class

    super().__init__(self.getCenter(), size, color)

  def getCenter(self):
    return [x+self._orbitRadius*f(self._angle)
    for x,f in zip(self._orbitAround.getCenter(), (math.sin,math.cos))]

  def move(self):
    self._center = self.getCenter()
    self._angle += self._speed

def start(): #having two "Draw" functions was very confusing.
  turtle.clear()
  system.draw()
  screen.ontimer(start,0)

def onClick(x,y):
  system.onClick((x,y))

system = SolarSystem()
system.draw()

turtle.tracer(0,0)
turtle.hideturtle()
screen=turtle.Screen()
screen.onkey(turtle.bye,"q")
screen.ontimer(start,0)
screen.onclick(onClick)
screen.onkey(system.Up, "Up")
screen.onkey(system.Down, "Down")
screen.onkey(system.Left, "Left")
screen.onkey(system.Right, "Right")
screen.onkey(system.leftBracket, "[")
screen.onkey(system.rightBracket, "]")
screen.onkey(system.newMoon, "n")
screen.onkey(system.changeColor,"space")


screen.listen()
turtle.mainloop()