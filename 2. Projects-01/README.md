# Project 1: Building a House in Rainfall
- Draw a house with a raindrop using the base primitives: points, lines, or triangles. You can use ONLY GL_POINTS, GL_LINES, or GL_TRIANGLES for designing this house. A diagram has been provided as an example. You can modify the house design to your liking. The rain drops should be animated to fall from top to bottom.

- It has been raining unwantedly for the last few days, so let’s control its direction by designing a key that will change the direction of the rain when clicked (slightly bending the rainfall). Design this functionality such that the left arrow will gradually bend the rain to the left and the right arrow will gradually bend the rain to the right.

- Formulate two more keys(assign whatever key you like); pressing one will gradually change the skin colour from dark to light simulating night to day, and the other will change it from light to dark simulating day to night . You must also consider the rain and the house visibility in different background colours.
	


# Project 2: Building the Amazing Box
- Design a box with the following functionalities and ensure they all work independently and in any combination. Check out the gifs along with instructions for better understanding.

- The right button click on a mouse will generate random movable points with different colours going in any random direction diagonally within a boundary region. For instance, if a point is generated at (0,0), it can go to (-1, 1), (-1, -1), (1,1), or (1, -1), and so on. The points should be spawned where the right button click will be given in the box and the colour and direction of movement should be random. The points will continue to move in the same direction and will bounce back from the wall of the boundary. [Bouncing from the wall can be implemented by changing the sign of corresponding position update parameter]

- Pressing the “up arrow” key on the keyboard will increase the speed of all the points generated so far and pressing the “down arrow” key on the keyboard will decrease the speed.
The left button click on a mouse will make the points blink i.e. if a point is in red, it will go background color(here it’s black) and return to red, and this transition should take place within a second while the transition cycle goes on. [Think how you can easily implement this]. Clicking the left button again will bring back the scenario in the original state.

- Pressing the “Spacebar” on the keyboard should freeze all the points and none of the above functionalities will work when frozen. The same “Spacebar” should unfreeze them.
