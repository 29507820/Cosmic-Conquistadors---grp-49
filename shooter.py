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

        for i in range(-2, 3):
            offset_x = i * math.cos(math.radians(self.angle + 90))
            offset_y = i * math.sin(math.radians(self.angle + 90))

            start_x = self.x + offset_x
            start_y = self.y + offset_y

            end_x = start_x + TURRET_HEIGHT * math.cos(math.radians(self.angle))
            end_y = start_y + TURRET_HEIGHT * math.sin(math.radians(self.angle))

            stddraw.line(start_x, start_y, end_x, end_y)
