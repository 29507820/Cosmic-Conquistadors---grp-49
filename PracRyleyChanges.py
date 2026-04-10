import sys, stdio, stddraw, stdarray #Type: ignore

#globals
PLAYER_RADIUS = 25
PLAYER_Y = -325
TURRET_WIDTH = 5
TURRET_HEIGHT = 25
ENEMY_RADIUS = 15
#------------------------
# D Williams 29507820
#------------------------
def showInstructions() -> None: #show main menu with instructions 

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
    
    stddraw.show(0)

#------------------------
# D Williams 29507820
#------------------------
def beginGame(Player_x) -> None:
    
    GameOn = True
    #set both moovement checks to false
    move_right = False
    move_left = False

    #ryley    creating enemy grid
    rows = 3
    cols = 5
    vx = 1.5
    startT = 380
    ry = startT
    pos = start_positions(rows, cols)
    
    while GameOn:
        
        #clear screen
        stddraw.clear(stddraw.GRAY)
        # ryley draw enemy pos
        draw_updatedEnemy(pos, ry)
        #place/move player
        movePlayer(Player_x,PLAYER_Y)

        if stddraw.hasNextKeyTyped(): #check if user input anything
            kbinput = stddraw.nextKeyTyped() #read input
            
            #checking for quit, may create a pause screen later 
            if (kbinput == "x"):
                sys.exit() #close program
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

        #update player position if possible
        if (Player_x + PLAYER_RADIUS + 10 > 300):
            move_right = False
        if (Player_x - PLAYER_RADIUS - 10 < -300):
            move_left = False

        if (move_right):
            Player_x += 2
        if (move_left):
            Player_x -= 2

        update_positions(pos, vx)

        #ryley checking if edge of canvas
        if check_ifwall(pos, vx):
            vx = -vx
            ry -= 45
        
        stddraw.show(0)

#------------------------
# D Williams 29507820
#------------------------
def movePlayer(x,y) -> None:
    stddraw.setPenColor(stddraw.YELLOW)
    stddraw.filledCircle(x,y,PLAYER_RADIUS)

    stddraw.setPenColor(stddraw.GREEN)
    stddraw.filledRectangle(x-(TURRET_WIDTH/2),y,TURRET_WIDTH,TURRET_HEIGHT)

    stddraw.show(10)

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
#------------------------
# D Williams 29507820
#------------------------

    # set size and background
    stddraw.setCanvasSize(600, 800)
    stddraw.setXscale(-300, 300)
    stddraw.setYscale(-400, 400)
    
    # Display menu screen
    showInstructions()
    
    #Check for user input 
    while True:

        if stddraw.hasNextKeyTyped(): #check if user input anything
            kbinput = stddraw.nextKeyTyped() #read input

            if (kbinput == "x"):
                sys.exit() #close program
            else:
                beginGame(0)
                break
        stddraw.show(0)


if __name__ == "__main__": main()

