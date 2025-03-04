from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def iterate():
    # this is all setup
    glViewport(0, 0, 500, 500) # bezzle select kore 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0) # (x-axis starts, x-axis ends, y-axis starts, y-axis end, zaxis, zaxis)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # learn after mid
    glLoadIdentity() # learn after mid
    iterate() # calling the iterate function
    


    #call the draw methods here ---------------------------------------
    # draw_points(250, 250)

    glColor3f(1.0, 0.0, 0.0) #konokichur color set (RGB) [255 = 1, 0 = 0, range != 0-255 but 0-1] 
    glPointSize(5)

    # drawing a dot 
    glBegin(GL_POINTS)
    glVertex2f(450, 100) 
    glEnd()

    # drawing a line
    glBegin(GL_LINES)
    glVertex2f(350, 50) 
    glVertex2f(350, 200) 
    glEnd()

    # drawing a triangle 
    glBegin(GL_TRIANGLES) 
    glVertex2f(250, 250) 
    glVertex2f(250, 500)
    glVertex2f(500, 250)
    glEnd() 


    # drawing two traingles one blue and another gradient 
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 1)
    glVertex2f(30, 30)
    glVertex2f(30, 200)
    glVertex2f(100, 200)

    # creating the Gradient 
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(30, 230)
    glColor3f(1.0, 1, 0)
    glVertex2f(30, 400)
    glColor3f(1.0, 1, 1)
    glVertex2f(100, 400)
    glEnd()

    glutSwapBuffers()

#initializing
glutInit()
glutInitDisplayMode(GLUT_RGBA) #we will use Colorful stuff
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0) # from the where the program will run compare to my monitor
wind = glutCreateWindow(b"OpenGL First Code") #window name
glutDisplayFunc(showScreen) 

glutMainLoop() # it continously runs my program 