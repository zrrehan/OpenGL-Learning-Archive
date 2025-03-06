from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

dots = []
speed = 0.1
freeze = False
blink = False
blink_idx = 0
dot_movements = [(speed, speed), (speed, -speed), (-speed, speed), (-speed, -speed)]
def convert_coordinate(x, y):
    return [x, 500-y]

def animation():
    global dots
    if(not freeze):
        for dot in dots:
            dot["position"][0] += dot["movement"][0] * speed
            dot["position"][1] += dot["movement"][1] * speed

            if(dot["position"][0] >= 490 or dot["position"][0] <= 10):
                dot["movement"] = (dot["movement"][0] * -1, dot["movement"][1])
            if(dot["position"][1] >= 490 or dot["position"][1] <= 10):
                dot["movement"] = (dot["movement"][0], dot["movement"][1] * -1)
            glutPostRedisplay()

def keyboard_listener(key, x, y):
    global freeze
    if(key == b" "):
        freeze = not freeze

def mouse_listener(button, state, x, y):
    global dots, blink
    if(button == GLUT_RIGHT_BUTTON):
        if(state == GLUT_DOWN):
            single_dot = {
                "position": convert_coordinate(x, y),
                "color": (random.random(), random.random(), random.random()),
                "movement":  random.choice(dot_movements)
            }
            dots.append(single_dot)
    
    if(button == GLUT_LEFT_BUTTON):
        if(state == GLUT_DOWN):
            blink = not blink

def special_keyboard_listener(button,x, y):
    global speed
    if(button == GLUT_KEY_DOWN and speed > 0):
        speed -= 0.05
        if(speed < 0):
            speed = 0
    if(button == GLUT_KEY_UP):
        speed += 0.05

def iterate():
    # this is all setup
    glViewport(0, 0, 500, 500) # bezzle select kore 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0) # (x-axis starts, x-axis ends, y-axis starts, y-axis end, zaxis, zaxis)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global dots, blink_idx
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # learn after mid
    glLoadIdentity() # learn after mid
    iterate() # calling the iterate function
    


    #call the draw methods here ---------------------------------------
    

    glColor3f(1.0, 0.0, 0.0)
    glPointSize(10)

    glBegin(GL_LINES)
    glVertex2f(10, 10)
    glVertex2f(490, 10)

    glVertex2f(490, 10)
    glVertex2f(490, 490)

    glVertex2f(10, 490)
    glVertex2f(490, 490)

    glVertex2f(10, 490)
    glVertex2f(10, 10)
    glEnd()

    glBegin(GL_POINTS)
    for dot in dots:
        if(blink):
            if(blink_idx % 10000 < 5000):
                glColor3f(0, 0, 0)
            else:
                glColor3f(dot["color"][0], dot["color"][1], dot["color"][2])
            blink_idx += 1
        else:
            glColor3f(dot["color"][0], dot["color"][1], dot["color"][2])
        glVertex2f(dot["position"][0], dot["position"][1])
    glEnd()

    glutSwapBuffers()

#initializing
glutInit()
glutInitDisplayMode(GLUT_RGBA) #we will use Colorful stuff
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0) # from the where the program will run compare to my monitor
wind = glutCreateWindow(b"OpenGL First Code") #window name
glutDisplayFunc(showScreen) 
glutIdleFunc(animation)
glutMouseFunc(mouse_listener)
glutSpecialFunc(special_keyboard_listener)
glutKeyboardFunc(keyboard_listener)

glutMainLoop() # it continously runs my program 