import stddraw  


PLAYER_RADIUS = 25
TURRET_WIDTH = 5
TURRET_HEIGHT = 25


class Shooter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move_left(self):
        if self.x - 10 - PLAYER_RADIUS >= -300:
            self.x -= 10

    def move_right(self):
        if self.x + 10 + PLAYER_RADIUS <= 300:
            self.x += 10
    
    def draw(self):
        stddraw.setPenColor(stddraw.YELLOW)
        stddraw.filledCircle(self.x, self.y, PLAYER_RADIUS)

        stddraw.setPenColor(stddraw.GREEN)
        stddraw.filledRectangle(
            self.x - (TURRET_WIDTH / 2),
            self.y,
            TURRET_WIDTH,
            TURRET_HEIGHT
        )
