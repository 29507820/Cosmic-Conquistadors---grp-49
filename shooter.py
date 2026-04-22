#----------------------------
# J Klagsbrun 29076137
#----------------------------

import stddraw
import math
from picture import Picture

#defining sizes for turret and player
PLAYER_RADIUS = 25
TURRET_WIDTH = 5
TURRET_HEIGHT = 25


class Shooter:
    #storing shooters position
    def __init__(self, x, y, hp, color=stddraw.YELLOW):
        self.x = x
        self.y = y
        self.hp = hp

        #initial angle for turret must be 90* pointing straight up
        self.angle = 90
        self.color = color

    def damagetaken(self, damage):
        self.hp -= damage

#moving player left and right, making sure it stays within the screen bounds
    def move_left(self):
        if self.x - 10 - PLAYER_RADIUS >= -300:
            self.x -= 10

    def move_right(self):
        if self.x + 10 + PLAYER_RADIUS <= 300:
            self.x += 10

#prints shooter health
    def print_Playerhp(self):
        stddraw.setPenColor(stddraw.RED)
        if self.hp == 1:
            stddraw.filledCircle(-185, y, 5)
        if self.hp == 2:
            stddraw.filledCircle(-185, y, 5)
            stddraw.filledCircle(-170, y, 5)
        if self.hp == 3:
            stddraw.filledCircle(-185, y, 5)
            stddraw.filledCircle(-170, y, 5)
            stddraw.filledCircle(-155, y, 5)


#rotating turret: MAX 180* MIN 0*
    def rotate_left(self):
        if self.angle < 180:
            self.angle += 5

    def rotate_right(self):
        if self.angle > 0:
            self.angle -= 5

    #drawing shooter
    def draw(self):
        stddraw.setPenColor(self.color)
        stddraw.filledCircle(self.x, self.y, PLAYER_RADIUS)
        #stddraw.picture(Picture("player1.png"), self.x, self.y)
        
        #drawing turret
        stddraw.setPenColor(stddraw.GREEN)
        stddraw.setPenRadius(1)

        #move turret above shooter
        base_x = self.x
        base_y = self.y + PLAYER_RADIUS + 2

        #turret endpoint calculations
        end_x = base_x + TURRET_HEIGHT * math.cos(math.radians(self.angle))
        end_y = base_y + TURRET_HEIGHT * math.sin(math.radians(self.angle))

        stddraw.line(base_x, base_y, end_x, end_y)

        stddraw.setPenRadius()





