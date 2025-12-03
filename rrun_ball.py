import turtle
from balll import Ball
from sevensec import sec
import random
class run:
    def __init__(self):
        self.num_balls = 5
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        print(self.canvas_width, self.canvas_height)
        self.ball_radius = 0.05 * self.canvas_width
        turtle.colormode(255)
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []

        # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
        for i in range(self.num_balls):
            self.xpos.append(random.uniform(-1*self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius))
            self.ypos.append(random.uniform(-1*self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius))
            self.vx.append(10*random.uniform(-1.0, 1.0))
            self.vy.append(10*random.uniform(-1.0, 1.0))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2*self.canvas_width)
            turtle.left(90)
            turtle.forward(2*self.canvas_height)
            turtle.left(90)

Tom = turtle.Turtle()
tom_color = (255, 0, 0)
sc = sec(Tom,tom_color)
delay_in_seconds = 0.01
ip_b = Ball()
runn = run()
ct=0
fc=0
dt = 0.2 # time step
while (True):
    turtle.clear()
    runn.draw_border()
    for i in range(runn.num_balls):
        ip_b.draw_ball(runn.ball_color[i], runn.ball_radius, runn.xpos[i], runn.ypos[i])
        ip_b.move_ball(i, runn.xpos, runn.ypos, runn.vx, runn.vy, dt)
        ip_b.update_ball_velocity(i, runn.xpos, runn.ypos, runn.vx, runn.vy, runn.canvas_width, runn.canvas_height, runn.ball_radius)
    sc.clear()
    sc.draw(Tom, ct)
    
    fc += 1
    if fc >=20:
        ct = (ct+1)%10
        fc = 0
    sc.my_delay(delay_in_seconds)
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()



"""while True:
    for i in range(0, 10):
        sc.clear()
        sc.draw(Tom, i)
        sc.my_delay(delay_in_seconds)
        turtle.update()

turtle.done()"""