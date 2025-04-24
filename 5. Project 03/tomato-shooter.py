from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Camera-related variables
camera_pos = (0,500,500)
player_pos = [0, 0, 0]
angle = 0
enemy_list = [] 

fovY = 120  # Field of view
GRID_LENGTH = 200  # Length of grid lines


def enemy():
    def random_pick():
        if(random.choice([True, False])):
            return random.randint(-500, -200)
        else:
            return random.randint(200, 500)
        
    return (random_pick(), random_pick())

def enemies():
    global enemy_list
    for _ in range(5):
        enemy_list.append(enemy())
enemies()

def show_enemies():
    for points in enemy_list:
        glPushMatrix()

        glColor3f(1,0,0)
        glTranslatef(points[0], points[1], 0) 
        gluSphere(gluNewQuadric(), 50, 100, 10)

        glPopMatrix()

        glPushMatrix()

        glColor3f(0,0,0)
        glTranslatef(points[0], points[1], 50) 
        gluSphere(gluNewQuadric(), 25, 100, 10)

        glPopMatrix()


def player():
    glPushMatrix()
    glRotatef(angle, 0, 0, 1)  
    # glTranslatef(player_pos[0], player_pos[1], 0)

    glPushMatrix()
    # body
    glColor3f(0, 0.2, 0.1)
    glTranslatef(player_pos[0], player_pos[1], 0)  # setting the position 
    glScalef(1.5,1,1)
    glutSolidCube(100)
    glPopMatrix()


    # head 
    glPushMatrix()
    glColor3f(0,0,0)
    glTranslatef(player_pos[0], player_pos[1], 100) 
    gluSphere(gluNewQuadric(), 30, 100, 10)
    glPopMatrix()
  

    # right hand 
    glPushMatrix()
    glTranslatef(player_pos[0] - 50, player_pos[1], 50)
    glRotatef(90, 0, 1, 0)  
    glRotatef(90, 1, 0, 0)  
    glColor3f(0.34, 0.67, 0.87)
    gluCylinder(gluNewQuadric(), 30, 10, 100, 10, 10)
    glPopMatrix()

    #  right hand 
    glPushMatrix()
    glTranslatef(player_pos[0] + 50, player_pos[1], 50)
    glRotatef(90, 0, 1, 0)  
    glRotatef(90, 1, 0, 0)  
    glColor3f(0.34, 0.67, 0.87)
    gluCylinder(gluNewQuadric(), 30, 10, 100, 10, 10)
    glPopMatrix()

    # gun 
    glPushMatrix()
    glTranslatef(player_pos[0], player_pos[1], 50)
    glRotatef(90, 0, 1, 0)  
    glRotatef(90, 1, 0, 0)  
    glColor3f(0.18, 0.2, 0.17)
    gluCylinder(gluNewQuadric(), 30, 10, 200, 10, 10)
    glPopMatrix()

    glPopMatrix()

    

def draw_floor():
    glBegin(GL_QUADS)

    grid_start_x = 500
    grid_start_y = -500
    
    color = 1

    for row in range(11):
        grid_start_x = 500
        for col in range(11):
            if(color != 1):
                glColor3f(color, 0.74, 0.37)
                color = 1
            else:
                glColor3f(1, 1, color)
                color = 0
            
            glVertex3f(grid_start_x, grid_start_y, 0)
            glVertex3f(grid_start_x - 100, grid_start_y, 0)
            glVertex3f(grid_start_x - 100, grid_start_y + 100, 0)
            glVertex3f(grid_start_x, grid_start_y + 100, 0)

            grid_start_x -= 100
        grid_start_y += 100

    glEnd()


def setupCamera():
    """
    Configures the camera's projection and view settings.
    Uses a perspective projection and positions the camera to look at the target.
    """
    glMatrixMode(GL_PROJECTION)  # Switch to projection matrix mode
    glLoadIdentity()  # Reset the projection matrix
    # Set up a perspective projection (field of view, aspect ratio, near clip, far clip)
    gluPerspective(fovY, 1.25, 0.1, 1500) # Think why aspect ration is 1.25?
    glMatrixMode(GL_MODELVIEW)  # Switch to model-view matrix mode
    glLoadIdentity()  # Reset the model-view matrix

    # Extract camera position and look-at target
    x, y, z = camera_pos
    # Position the camera and set its orientation
    gluLookAt(x, y, z,  # Camera position
              0, 0, 0,  # Look-at target
              0, 0, 1)  # Up vector (z-axis)

def showScreen():
    """
    Display function to render the game scene:
    - Clears the screen and sets up the camera.
    - Draws everything of the screen
    """
    # Clear color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  # Reset modelview matrix
    glViewport(0, 0, 1000, 800)  # Set viewport size
    

    setupCamera()  # Configure camera perspective

    draw_floor()
    player()
    show_enemies()


    # Swap buffers for smooth rendering (double buffering)
    glutSwapBuffers()

def keyboardListener(key, x, y):
    # Move forward (W key)
    global angle
    if key == b'a':
        angle += 1

    if key == b'd':
        angle -= 1
        print(player_pos)

    if key == b'w':
        player_pos[1] -= 10

    if key == b's':
        player_pos[1] += 10


def specialKeyListener(key, x, y):
    """
    Handles special key inputs (arrow keys) for adjusting the camera angle and height.
    """
    global camera_pos
    x, y, z = camera_pos


    if key == GLUT_KEY_LEFT:
        x -= 5
        print("hello")

    if key == GLUT_KEY_RIGHT:
        x += 5 

    if key == GLUT_KEY_UP:
        y -= 5
        

    if key == GLUT_KEY_DOWN:
        y += 5 

    camera_pos = (x, y, z)

def idle():
    """
    Idle function that runs continuously:
    - Triggers screen redraw for real-time updates.
    """
    # Ensure the screen updates with the latest changes
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)  # Double buffering, RGB color, depth test
    glutInitWindowSize(1000, 800)  # Window size
    glutInitWindowPosition(0, 0)  # Window position
    wind = glutCreateWindow(b"3D OpenGL Intro")  # Create the window

    glutDisplayFunc(showScreen)  # Register display function
    glutIdleFunc(idle)  # Register the idle function to move the bullet automatically
    glutSpecialFunc(specialKeyListener)
    glutKeyboardFunc(keyboardListener)

    glutMainLoop()  # Enter the GLUT main loop

if __name__ == "__main__":
    main()