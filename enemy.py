import stdarray
import stdio
import sys
import math
import stddraw

class Bomb:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move_y(self):
        self.y -=10
    def draw(self):
        stddraw.setPenColor(stddraw.RED)
        stddraw.filledCircle(self.x, self.y, 5)

class Enemy:
    def __init__(self, enemyType, damage, hp, position):
        self.hp = hp
        self.enemyType = enemyType
        self.damage = damage
        self.position = position
    def damagetaken(self, damage):
        self.hp -= damage

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Easy(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, "easy", 1, 1, Position(x, y))

class Intermediate(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, "intermedite", 1, 2, Position(x, y))

class Hard(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, "hard", 1, 3, Position(x, y))

class Vhard(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, "vhard", 1, 4, Position(x, y))

class Ehard(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, "ehard", 1, 5, Position(x, y))


