from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

x_point, y_point = 0, 0
def convert_coordinate(x, y):
    window_height = 500
    a = x
    b = window_height - y
    return a, b

def mouseListener(button, state, x, y):
    global x_point, y_point
    if(button == GLUT_LEFT_BUTTON):
        if(state == GLUT_DOWN):
            print(x, y)
            actual_x, acutal_y = convert_coordinate(x, y)
            print(x,y,actual_x, acutal_y)
            x_point, y_point = actual_x, acutal_y
           

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
    glVertex2f(x_point, y_point) 
    glEnd()

    glutSwapBuffers()

#initializing
glutInit()
glutInitDisplayMode(GLUT_RGBA) #we will use Colorful stuff
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0) # from the where the program will run compare to my monitor
wind = glutCreateWindow(b"OpenGL First Code") #window name
glutDisplayFunc(showScreen) 
glutMouseFunc(mouseListener)


glutMainLoop() # it continously runs my program 