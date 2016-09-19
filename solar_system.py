import turtle
import math
import random

def randcolor():
  r = lambda: random.randint(0,255)
  return '#%02X%02X%02X' % (r(),r(),r())

class SolarSystem():
  def __init__(self):
    self.sun = Sun((0,0), 100, "yellow")
    self.planets = []
    self._lastClicked = None
    for i in range(random.randint(3,6)):
      planet = Planet(self.sun, random.randint(100, 350), random.randint(20, 70), randcolor(), random.uniform(0.009, 0.02))
      for i in range(random.randint(0,4)):
        moon = Planet(planet, random.randint(30, 60), random.randint(5, 20), randcolor(), random.uniform(0.04, 0.08))
        self.planets.append(moon)
      self.planets.append(planet)

  def draw(self):
    self.sun.draw()
    for p in self.planets:
      p.draw()
      p.move()

  def onClick(self, coords):
    self.sun.onClick(coords)
    for p in self.planets:
      p.onClick(coords)

class Sun:
  def __init__(self,center,size,color):
    self.center = center
    self.size = size
    self.color = color

  def setColor(self):
    print("in setColor")
    self.color = randcolor()

  def inside(self, location):
    if ((location[0] - self.center[0])**2 + (location[1] - self.center[1])**2 < ((self.size/2)**2)):
      return True

  def onClick(self, location):
    if self.inside(location):
      self.setColor()

  def getCenter(self):
    return self.center

  def draw(self):
    turtle.penup()
    turtle.goto(self.center)
    turtle.dot(self.size, self.color)
    # self.size is diameter

class Planet(Sun):
  def __init__(self, orbitAround, orbitRadius, size, color, speed):
    self.orbitAround = orbitAround
    self.orbitRadius = orbitRadius
    self.speed = speed
    self.angle = 0
    #size and color are inherited from Sun class

    super().__init__(self.getCenter(), size, color)

  def getCenter(self):
    return [x+self.orbitRadius*f(self.angle)
    for x,f in zip(self.orbitAround.getCenter(), (math.sin,math.cos))]

  def move(self):
    self.center = self.getCenter()
    self.angle += self.speed

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
screen.listen()
turtle.mainloop()