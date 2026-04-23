import stdio # type: ignore
import stddraw # type: ignore

#-----------------
#RE 28891058
#-----------------
#Subclass structure
#https://stackoverflow.com/questions/1607612/python-how-do-i-make-a-subclass-from-a-superclass 
#bomb class for storing and changing positions 
class Bomb:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move_y(self):
        self.y -=7
    def draw(self):
        stddraw.setPenColor(stddraw.GREEN)
        stddraw.filledCircle(self.x, self.y, 10)

#enemy class for storing enemytype, hp and positions
class Enemy:
    def __init__(self, enemyType, hp, position):
        self.hp = hp
        self.enemyType = enemyType
        self.position = position

#class store enemy positions
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#different subclasses that pass through main class defining enemies
class Easy(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, "easy", 1, Position(x, y))

class Intermediate(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, "intermedite", 2, Position(x, y))

class Hard(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, "hard", 3, Position(x, y))

class Vhard(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, "vhard", 4, Position(x, y))

class Ehard(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, "ehard", 5, Position(x, y))


