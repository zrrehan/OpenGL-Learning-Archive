from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

score = 0 
game_over = False
diamond_color = 0
catcher_points = [(200, 50), (300, 50)]
move = True
diamond_points = [(), (), (), ()]
speed = 0.3
left_point_x = random.randint(0, 480)
diamond_points = [(left_point_x + 10, 600),
                          (left_point_x + 20, 590),
                            (left_point_x + 10, 580),
                              (left_point_x, 590)]
diamon_color_change = True

def draw_cross():
    glColor3f(1, 0, 0)
    eight_way_symmetry([10, 690], [50, 640])
    eight_way_symmetry([10, 640], [50, 690])

def draw_pause_resume():
    glColor3f(1, 1, 0)
    if(move):
        eight_way_symmetry([245, 690], [245, 640])
        eight_way_symmetry([255, 690], [255, 640])
    else:
        eight_way_symmetry([235, 690], [235, 640])
        eight_way_symmetry([235, 690], [265, 665])
        eight_way_symmetry([235, 640], [265, 665])


def draw_restart():
    glColor3f(0.52, 0.8, 0.9)
    eight_way_symmetry([450, 665], [490, 665])
    eight_way_symmetry([450, 665], [470, 690])
    eight_way_symmetry([450, 665], [470, 640])


def convert_coordinate(x, y):
    window_height = 700
    a = x
    b = window_height - y
    return a, b

def mouseListener(button, state, x1, y1):
    global game_over, move, score, diamond_color, catcher_points, diamond_points, speed, left_point_x, diamond_points, diamon_color_change
    if(button == GLUT_LEFT_BUTTON):
        if(state == GLUT_DOWN):
            x, y = convert_coordinate(x1, y1)
            if(10 <= x <= 50 and 640 <= y <= 690):
                glutLeaveMainLoop()
            if(235 <= x <= 265 and 640 <= y <= 690):
                move = not move
            if(450 <= x <= 490 and 640 <= y <= 690):
                score = 0 
                diamond_color = 0
                catcher_points = [(200, 50), (300, 50)]
                move = True
                diamond_points = [(), (), (), ()]
                speed = 0.3
                left_point_x = random.randint(0, 480)
                game_over = False
                diamond_points = [(left_point_x + 10, 600),
                                        (left_point_x + 20, 590),
                                            (left_point_x + 10, 580),
                                            (left_point_x, 590)]
                diamon_color_change = True
                print("Starting Over!!")
                glColor3f(1.0, 0.0, 0.0) #konokichur color set (RGB) [255 = 1, 0 = 0, range != 0-255 but 0-1] 
                glPointSize(2)
                diamont_catch()
                draw_cross()
                draw_pause_resume()
                draw_restart()


def change_catcher_left(key, x, y):
    if(not move): return

    x1, y1 = catcher_points[0]
    x2, y2 = catcher_points[1]
    if(key == GLUT_KEY_LEFT):
        if(x1 - 20 < 0):
            x1 = 20
            x2 = x2 + 20
        catcher_points[0] = (x1 - 20, y1)
        catcher_points[1] = (x2 - 20, y2)
        glutPostRedisplay()
    if(key == GLUT_KEY_RIGHT):
        if(x2 + 20 > 500):
            x2 = 480
            x1 = x1 -20
        catcher_points[0] = (x1 + 20, y1)
        catcher_points[1] = (x2 + 20, y2)
        glutPostRedisplay()

def draw_catcher(): 
    x1, y1 = catcher_points[0]
    x2, y2 = catcher_points[1]

    # glColor3f(1, 1, 1)
    eight_way_symmetry([x1, y1], [x2, y2])
    eight_way_symmetry([x1 + 10, y1 - 10], [x2 - 10, y2 - 10])
    eight_way_symmetry([x1, y1], [x1 + 10, y1 - 10])
    eight_way_symmetry([x2 - 10, y2 - 10], [x2, y2])

def diamont_animation():
    global diamond_points, speed
    if(not move): return 
    up, left, bottom, right = diamond_points
    diamond_points = [
        (up[0], up[1] - speed),
        (left[0], left[1] - speed),
        (bottom[0], bottom[1] - speed),
        (right[0], right[1] - speed)
    ]
    glutPostRedisplay()

def draw_diamond():
    global diamond_points, left_point_x
    eight_way_symmetry(diamond_points[0], diamond_points[1])
    eight_way_symmetry(diamond_points[1], diamond_points[2])
    eight_way_symmetry(diamond_points[2], diamond_points[3])
    eight_way_symmetry(diamond_points[3], diamond_points[0])
     

def zone_calculate(m):
    if(0 <= m <= 1):
        return 0
    elif(m > 1):
        return 1
    elif(0 > m >= -1):
        return 3
    else:
        return 2
def zone_convert(point, zone, convertion_state = "zero2some"):
    x, y = point
    if(zone == 0):
        return [x, y]
    
    if(convertion_state == "zero2some"):
        if(zone == 1):
            return [y, x]
        elif(zone == 2):
            return [-y, x]
        else:
            return [-x, y]
    else:
        if(zone == 1):
            return [y, x]
        elif(zone == 2):
            return [y ,-x]
        else: 
            return [-x, y] 
        
def midpoint_line_drawing(start, end, zone):
    x1, y1 = start
    x2, y2 = end 

    dy = y2-y1
    dx = x2-x1

    d = 2*dy - dx
    dne = 2*dy - 2*dx 
    de = 2 * dy

    x, y = x1, y1

    while(x <= x2 and y <= y2):
        original = zone_convert([x, y], zone, "zero2some")
        draw_points(original[0], original[1])
        if(d > 0):
            d = d + dne 
            x += 1
            y += 1
        else:
            d = d + de
            x += 1
        

def eight_way_symmetry(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    if(y2 < y1):
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    draw_points(x1, y1)
    draw_points(x2, y2)
    if(x2 - x1 != 0):
        m = (y2 - y1) / (x2 - x1)
    else: 
        m = float("inf")
    zone = zone_calculate(m)

    point1_0 = zone_convert([x1, y1], zone, "some2zero")
    point2_0 = zone_convert([x2, y2], zone, "some2zero")

    midpoint_line_drawing(point1_0, point2_0, zone)

def diamont_catch():
    global score, diamond_points, move, diamon_color_change, diamond_color, speed, game_over
    glColor3f(1,1,1)
    draw_catcher()
    if(diamon_color_change):
        diamond_color = random.randint(50, 100) / 100, random.randint(50, 100) / 100, random.randint(50, 100) / 100
        glColor3f(diamond_color[0], diamond_color[1], diamond_color[2])
        diamon_color_change = False
        draw_diamond()
    else: 
        glColor3f(diamond_color[0], diamond_color[1], diamond_color[2])
        draw_diamond()
    
    if(diamond_points[2][1] <= 50 and diamond_points[1][1] >= 50):
        for points in range(catcher_points[0][0], catcher_points[1][0] + 1):
            if( 
                diamond_points[3][0] <= points <= diamond_points[1][0]  
            ):
                score += 1
                speed += 0.1
                print("Score: ", score)
                random_x = random.randint(0, 480)
                diamond_points = [(random_x + 10, 600),
                            (random_x + 20, 590),
                                (random_x + 10, 580),
                                (random_x, 590)]
                diamon_color_change = True
                break 
    
    if(diamond_points[0][1] <= 0):
        if(not game_over):
            print("Game over! Score:", score)
        move = False
        game_over = True
        glColor3f(1, 0, 0)
        draw_catcher()



def draw_points(x, y):
    glPointSize(2) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def iterate():
    # this is all setup
    glViewport(0, 0, 500, 700) # bezzle select kore 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 700, 0.0, 1.0) # (x-axis starts, x-axis ends, y-axis starts, y-axis end, zaxis, zaxis)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # learn after mid
    glLoadIdentity() # learn after mid
    iterate() # calling the iterate function
    

    glColor3f(1.0, 0.0, 0.0) #konokichur color set (RGB) [255 = 1, 0 = 0, range != 0-255 but 0-1] 
    glPointSize(2)

    diamont_catch()
    draw_cross()
    draw_pause_resume()
    draw_restart()

    glutSwapBuffers()

#initializing
glutInit()
glutInitDisplayMode(GLUT_RGBA) #we will use Colorful stuff
glutInitWindowSize(500, 700) #window size
glutInitWindowPosition(0, 0) # from the where the program will run compare to my monitor
wind = glutCreateWindow(b"Diamond Catcher") #window name
glutDisplayFunc(showScreen) 
glutSpecialFunc(change_catcher_left)
glutIdleFunc(diamont_animation)
glutMouseFunc(mouseListener)


glutMainLoop() # it continously runs my program 