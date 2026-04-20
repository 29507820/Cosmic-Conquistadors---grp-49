import stddraw
import math
from picture import Picture


PLAYER_RADIUS = 25
TURRET_WIDTH = 5
TURRET_HEIGHT = 25


class Shooter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 90

    def move_left(self):
        if self.x - 10 - PLAYER_RADIUS >= -300:
            self.x -= 10

    def move_right(self):
        if self.x + 10 + PLAYER_RADIUS <= 300:
            self.x += 10
    
    def rotate_left(self):
        if self.angle < 180:
            self.angle += 5

    def rotate_right(self):
        if self.angle > 0:
            self.angle -= 5
    
    def draw(self):
        stddraw.setPenColor(stddraw.YELLOW)
        stddraw.filledCircle(self.x, self.y, PLAYER_RADIUS)
        #stddraw.picture(Picture("player1.png"), self.x, self.y)
        
        stddraw.setPenColor(stddraw.GREEN)
        stddraw.setPenRadius(1)

        #move turret above monkey
        base_x = self.x
        base_y = self.y + PLAYER_RADIUS + 2

        end_x = base_x + TURRET_HEIGHT * math.cos(math.radians(self.angle))
        end_y = base_y + TURRET_HEIGHT * math.sin(math.radians(self.angle))

        stddraw.line(base_x, base_y, end_x, end_y)

        stddraw.setPenRadius()
