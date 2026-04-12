import sys, stdio, stdarray, stddraw #Type: ignore
from shooter import Shooter

#globals and constants

GameOn = False

PLAYER_RADIUS = 25
PLAYER_Y = -325
TURRET_WIDTH = 5
TURRET_HEIGHT = 25
ENEMY_RADIUS = 15

#------------------------
# D Williams 29507820
#------------------------
def showInstructions(): #show main menu with instructions 

    #clear screen
    stddraw.clear(stddraw.GRAY)

    # Add Text
    stddraw.setPenColor(stddraw.WHITE)

    stddraw.setFontSize(42)
    stddraw.text(0, 300, "COSMIC CONQUISTADORS")

    stddraw.setFontSize(28)
    stddraw.text(0, 200, "INSTRUCTIONS:")

    stddraw.setFontSize(24)
    stddraw.text(0, 150, "[A] Move Left, [S] Stop Moving, [D] Move right")
    stddraw.text(0, 100, "[Q] rotate left, [W] stop rotate, [E] rotate right")
    stddraw.text(0, 50, "[Space] to shoot")
    stddraw.text(0, -150, "[H] for help")
    stddraw.text(0, -100, "[X] to quit")
    stddraw.text(0, -300, "Press any key to start")
    
    stddraw.show(10)

#------------------------
# D Williams 29507820
#------------------------
def showPauseMenu():

    GamePaused = True 

    while GamePaused:

        #clear screen
        stddraw.clear(stddraw.GRAY)

        # Add Text
        stddraw.setPenColor(stddraw.WHITE)

        stddraw.setFontSize(42)
        stddraw.text(0, 300, "COSMIC CONQUISTADORS")

        stddraw.setFontSize(28)
        stddraw.text(0, 200, "GAME PAUSED")

        stddraw.setFontSize(24)
        stddraw.text(0, 150, "[Space] RESUME")
        stddraw.text(0, 100, "[R] RESTART")
        stddraw.text(0, 50, "[X] QUIT TO MENU")

        stddraw.show(10)
        
        if stddraw.hasNextKeyTyped(): #check if user input anything
            kbinput = stddraw.nextKeyTyped() #read input
            if (kbinput == " "):
                GamePaused = False
            if (kbinput == "r"):
                GamePaused = False
                beginGame()
            if (kbinput == "x"):
                GamePaused = False
                #GameOn = False (Doesn't work will figure it out dw)
                sys.exit() #close program for now


#------------------------
# Everyone
#------------------------
def beginGame():
    
    GameOn = True
    #set both movement checks to false
    move_right = False
    move_left = False
    rotate_right = False
    rotate_left = False
    
    #player begins in middle of screen
    Player_x = 0 

    #ryley creating enemy grid
    rows = 3
    cols = 5
    vx = 1.5
    startT = 380 -45
    ry = startT
    pos = start_positions(rows, cols)

    player = Shooter(Player_x, PLAYER_Y)
    
    while GameOn:

        #clear screen
        stddraw.clear(stddraw.GRAY)

        # ryley draw enemy pos
        draw_updatedEnemy(pos, ry)

        if stddraw.hasNextKeyTyped(): #check if user input anything
            kbinput = stddraw.nextKeyTyped() #read input
            
            #checking for pause 
            if (kbinput == "\x1b"): #ASCII value for escape key 
                showPauseMenu()
            #checking for movement
            if (kbinput == "a"):
                move_left = True
                move_right = False
            if (kbinput == "d"):
                move_left = False
                move_right = True
            if (kbinput == "s"):
                move_left = False
                move_right = False
            if (kbinput == "q"):
                rotate_right = False
                rotate_left = True            
            if (kbinput == "e"):
                rotate_right = True
                rotate_left = False
            if (kbinput == "w"):
                rotate_right = False
                rotate_left = False
               
        if (move_right):
            player.move_right()
        if (move_left):
            player.move_left()
        if (rotate_left):
            player.rotate_left()
        if (rotate_right):
            player.rotate_right()

        #display pause UI
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.text(215, 380, "[ESC] to pause")

        #animate enemies
        update_positions(pos, vx)
        #ryley checking if edge of canvas (enemies)
        if check_ifwall(pos, vx):
            vx = -vx
            ry -= 45

        #animate player
        player.draw()
        stddraw.show(50)

#------------------------
# R Evans 28891058
#------------------------
def start_positions(rows, cols):
    pos = stdarray.create2D(rows, cols, 0.0)
    for i in range(0, rows):
        k = -280
        for j in range(0, cols):
            pos[i][j] = k
            k += 45
    return pos

#------------------------
# R Evans 28891058
#------------------------
def update_positions(pos, vx):
    rows = len(pos)
    cols = len(pos[0])
    for i in range(0, rows):
        for j in range(0, cols):
            pos[i][j] += vx

#------------------------
# R Evans 28891058
#------------------------
def check_ifwall(pos, vx):
    return (abs(pos[0][0]+vx)+ENEMY_RADIUS>300 or abs(pos[0][len(pos[0])-1]+vx)+ENEMY_RADIUS>300)

#------------------------
# R Evans 28891058
#------------------------
def draw_updatedEnemy(pos, ry):
    stddraw.clear(stddraw.GRAY)
    rows = len(pos)
    cols = len(pos[0])
    for i in range(0, rows):
        for j in range(0, cols):
            stddraw.filledCircle(pos[i][j], ry - i*45, ENEMY_RADIUS)
    stddraw.show(0)

def main() -> None:

    # set size and background
    stddraw.setCanvasSize(600, 800)
    stddraw.setXscale(-300, 300)
    stddraw.setYscale(-400, 400)
    
    while True: 
        # Display menu screen
        showInstructions()
    
        #Check for user input 
        while True:

            if stddraw.hasNextKeyTyped(): #check if user input anything
                kbinput = stddraw.nextKeyTyped() #read input

                if (kbinput == "x"):
                    sys.exit() #close program
                else:
                    beginGame()
                    break
            stddraw.show(10)


if __name__ == "__main__": main()

