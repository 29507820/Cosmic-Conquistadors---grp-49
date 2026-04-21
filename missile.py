#--------------------------
# J Klagsbrun 29076137
#--------------------------

import stddraw
import math

#constants controlling missile speed and size
MISSILE_RADIUS = 5
MISSILE_SPEED = 10


class Missile:

    #storing missile start pos
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y

        #storing direction missile is being shot depending on turret angle
        self.angle = angle

    # Update x and y position based on speed and direction
    # cos(angle) controls horizontal movement
    # sin(angle) controls vertical movement
    def move(self):
        self.x += MISSILE_SPEED * math.cos(math.radians(self.angle))
        self.y += MISSILE_SPEED * math.sin(math.radians(self.angle))

    def draw(self):
        stddraw.setPenColor(stddraw.RED)
        stddraw.filledCircle(self.x, self.y, MISSILE_RADIUS)
