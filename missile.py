import stddraw
import math

MISSILE_RADIUS = 5
MISSILE_SPEED = 10


class Missile:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def move(self):
        self.x += MISSILE_SPEED * math.cos(math.radians(self.angle))
        self.y += MISSILE_SPEED * math.sin(math.radians(self.angle))

    def draw(self):
        stddraw.setPenColor(stddraw.RED)
        stddraw.filledCircle(self.x, self.y, MISSILE_RADIUS)
