from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

rain_drop = [] 
rain_y_axis = [100, 500, 800, 400, 900, 1000, 700, 200, 300, 600]
rain_x_axis_init = []
for i in range(-20, 1020, 20):
    rainY = random.choice(rain_y_axis)

    rain_x_axis_init.append(i)
    rain_drop += [[i, rainY]] +  [[i, rainY + 100]] + [[i, rainY+ 600]] + [[i, rainY + 700]]

rain_x = 0
def animate():
    global rain_drop
    for rain_idx in range(len(rain_drop)):
        rains = rain_drop[rain_idx]
        rains[1] -= 0.5
        rains[0] += rain_x
        if(rain_idx % 2 == 1 and rains[1] < 0):
            rain_drop[rain_idx][1] = 1700
            rain_drop[rain_idx - 1][1] = 1600
            
        if((rain_idx % 2 == 1 and rains[0] < 0) or (rain_idx % 2 == 1 and rains[0] > 1000)):
            if(rains[0] < 0):
                new_x = random.randint(500, 1000)
            if(rains[0] > 1000):
                new_x = random.randint(0, 500)


            rain_drop[rain_idx -1][0] = new_x + (rain_drop[rain_idx -1][0] - rain_drop[rain_idx][0])
            rain_drop[rain_idx][0] = new_x 
            rain_drop[rain_idx][1] = 600
            rain_drop[rain_idx - 1][1] = 500
        glutPostRedisplay()
    


def keyboard_listen(key, x, y):
    global rain_drop, rain_x
    if(key == GLUT_KEY_RIGHT):
        rain_x += 0.001
        for rain_idx in range(len(rain_drop)):
            if(rain_idx % 2 == 0):
                rain_drop[rain_idx][0] += 0.2
                glutPostRedisplay()
    
    if(key == GLUT_KEY_LEFT):
        rain_x -= 0.001
        for rain_idx in range(len(rain_drop)):
            if(rain_idx % 2 == 0):
                rain_drop[rain_idx][0] -= 0.2
                glutPostRedisplay()
    

day_color = [[0, 0, 0], [0.23, 0.23, 0.23], [.4,.4,.4], [.6,.6,.6]]
color = day_color[0]
color_idx = 0
def change_day(key, x, y):
    global color_idx, color
    if(key == b"a"):
        if(color_idx != 0):
            color_idx -= 1
            color = day_color[color_idx]
            glClearColor(color[0], color[1], color[2], 0)
            glutPostRedisplay()
    if(key == b"d"):
        if(color_idx != 3):
            color_idx += 1
            color = day_color[color_idx]
            glClearColor(color[0], color[1], color[2], 0)
            glutPostRedisplay()

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def iterate():
    # this is all setup
    glViewport(0, 0, 1000, 500) # bezzle select kore 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 500, 0.0, 1.0) # (x-axis starts, x-axis ends, y-axis starts, y-axis end, zaxis, zaxis)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # learn after mid
    glLoadIdentity() # learn after mid
    iterate() # calling the iterate function
    


    #call the draw methods here ---------------------------------------
    # draw_points(250, 250) 
    glPointSize(5)

    glBegin(GL_QUADS)
    glColor3f(0.11, 0.812, 0.03)
    glVertex2f(0, 0)
    glVertex2f(1000, 0)
    glColor3f(0.74, 0.92, 0.15)
    glVertex2f(1000, 150)
    glVertex2f(0, 150)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1, 0)
    glVertex2f(500, 300)
    glColor3f(1, 0, 0)
    glVertex2f(300, 200)
    glVertex2f(700, 200) 
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex2f(320, 200)
    glVertex2f(320, 100)
    glVertex2f(680, 100)
    glVertex2f(680, 200)
    glEnd()

    
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(160 + 320, 150)
    glVertex2f(160 + 320, 100)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(160 + 320, 100)
    glVertex2f(200 + 320, 100)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(200 + 320, 100)
    glVertex2f(200 + 320, 150)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(200 + 320, 150)
    glVertex2f(160 + 320, 150)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0, 0, 1)
  
    for rain in rain_drop:
        glVertex2f(rain[0], rain[1])
        
        
    glEnd()

    glutSwapBuffers()

#initializing
glutInit()
glutInitDisplayMode(GLUT_RGBA) #we will use Colorful stuff
glutInitWindowSize(1000, 500) #window size
glutInitWindowPosition(0, 0) # from the where the program will run compare to my monitor
wind = glutCreateWindow(b"OpenGL First Code") #window name
glClearColor(color[0], color[1], color[2], 0)
glutDisplayFunc(showScreen) 
glutIdleFunc(animate)
glutSpecialFunc(keyboard_listen)
glutKeyboardFunc(change_day)

glutMainLoop() # it continously runs my program 