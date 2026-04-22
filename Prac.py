import sys, stdio, stdarray, stddraw, stdrandom #Type: ignore
from shooter import Shooter
from missile import Missile
from enemy import Easy, Intermediate, Hard, Vhard, Ehard, Position, Bomb, Bunker
from picture import Picture

#globals and constants

GameOn = False
score = 0


PLAYER_RADIUS = 25
PLAYER_Y = -325
TURRET_WIDTH = 5
TURRET_HEIGHT = 25
ENEMY_RADIUS = 15
BUNKER_HALFLENGTH = 70

#------------------------
# D Williams 29507820
#------------------------
def showInstructions(): #show main menu with instructions 

    #clear screen
    stddraw.clear(stddraw.GRAY)

    #add Text
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.picture(Picture("background.png"))
    
    stddraw.setFontSize(42)
    stddraw.text(0, 300, "COSMIC CONQUISTADORS")
    stddraw.text(0.5, 300, "COSMIC CONQUISTADORS")
    stddraw.text(0, 300.5, "COSMIC CONQUISTADORS")

    stddraw.setFontSize(28)
    stddraw.text(0, 250, "INSTRUCTIONS:")

    stddraw.setFontSize(24)

    #player 1 controls
    stddraw.setPenColor(stddraw.GREEN)
    
    stddraw.text(0, 200, "PLAYER 1:")
    stddraw.text(0.5, 200, "PLAYER 1:")
    stddraw.text(0, 200.5, "PLAYER 1:")
    stddraw.text(0, 150, "[A] Move Left, [S] Stop Moving, [D] Move right")
    stddraw.text(0, 100, "[Q] rotate left, [W] stop rotate, [E] rotate right")
    stddraw.text(0, 50, "[Space] to shoot")

    #player 2 controls
    stddraw.setPenColor(stddraw.ORANGE)
    
    stddraw.text(0, 0, "PLAYER 2:")
    stddraw.text(0.5, 0, "PLAYER 2:")
    stddraw.text(0, 0.5, "PLAYER 2:")
    stddraw.text(0, -40, "[J] left, [K] stop, [L] right")
    stddraw.text(0, -80, "[U] rotate left, [I] stop rotate, [O] rotate right")
    stddraw.text(0, -120, "[P] shoot")

    stddraw.setPenColor(stddraw.WHITE)
    stddraw.text(0, -200, "[H] for help")
    stddraw.text(0, -250, "[X] to quit")
    stddraw.text(0, -300, "Press any key to start")
    
    stddraw.show(10)

#------------------------
# D Williams 29507820
#------------------------
def showPauseMenu():

    global GameOn

    GamePaused = True 

    while GamePaused:

        #clear screen       
        stddraw.clear(stddraw.GRAY)

        #add Text
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
                GameOn = False #Closes current game loop
                GameOn = True
                beginGame() #Restarts game
            if (kbinput == "x"):
                GamePaused = False
                GameOn = False 

#------------------------
# D Williams 29507820
#------------------------
def GameOver():
    global GameOn, score
    GameOver = True

    while GameOver:
        stddraw.clear(stddraw.RED)
        stddraw.setPenColor(stddraw.WHITE)

        stddraw.setFontSize(30)
        stddraw.text(0, 250, "GAME OVER")

        stddraw.setFontSize(24)
        stddraw.text(0, 150, f"Final Score: {score}")
        stddraw.text(0, 100, "[R] RESTART")
        stddraw.text(0, 50, "[X] QUIT TO MENU")  

        stddraw.show(10)

        if stddraw.hasNextKeyTyped(): #check if user input anything
            kbinput = stddraw.nextKeyTyped() #read input
            if (kbinput == "r"):
                GameOver = False
                GameOn = True
                beginGame() #Restarts game
            if (kbinput == "x"):
                GameOver = False
          

#------------------------
# Everyone
#------------------------
def beginGame():
    
    global GameOn, score

    score = 0 

    #set both movement checks to false for both players

    stddraw.setPenColor(stddraw.BLUE)
    stddraw.rectangle(-225, -150, 70, 20)


    
    #player 1 movement
    p1_move_right = False
    p1_move_left = False
    p1_rotate_right = False
    p1_rotate_left = False

    #player 2 movement
    p2_move_right = False
    p2_move_left = False
    p2_rotate_right = False
    p2_rotate_left = False
    
    #player begins in middle of screen
    Player_x = 0 

    #ryley creating enemy grid
    rows = 3
    cols = 5
    vx = 3
    startT = 380 -45
    level = 1
    arr = enemyarr(rows, cols, level)
    bombs = []
#    bunker1 = Bunker(-220, 2)
#    bunker2 = Bunker(-100, 2)
#    bunker3 = Bunker(20, 2)
#    bunker4 = Bunker(140, 2)
#    bunkers = [bunker1, bunker2, bunker3, bunker4]


    player1 = Shooter(-120, PLAYER_Y, 3, stddraw.YELLOW)
    player2 = Shooter(120, PLAYER_Y, 3, stddraw.CYAN)
    missiles = []    
   
    #cooldown preventing player from spamming missiles
    cooldown_max = 8
    cooldown_left = 0

    while GameOn:

        #clear screen
        stddraw.clear(stddraw.GRAY)
        stddraw.picture(Picture("background.png"))
        
        #print player hp
        print_Playerhp(player1, player2)

        # ryley draw enemy pos
        draw_updatedEnemy(arr, rows, cols)


        if stddraw.hasNextKeyTyped(): #check if user input anything
            kbinput = stddraw.nextKeyTyped() #read input
            
            #checking for pause 
            if (kbinput == "\x1b"): #ASCII value for escape key 
                showPauseMenu()
            #checking for player 1 movement
            if (kbinput == "a"):
                p1_move_left = True
                p1_move_right = False
            if (kbinput == "d"):
                p1_move_left = False
                p1_move_right = True
            if (kbinput == "s"):
                p1_move_left = False
                p1_move_right = False
            if (kbinput == "q"):
                p1_rotate_right = False
                p1_rotate_left = True            
            if (kbinput == "e"):
                p1_rotate_right = True
                p1_rotate_left = False
            if (kbinput == "w"):
                p1_rotate_right = False
                p1_rotate_left = False
            if (kbinput == " "):
                if cooldown_left == 0:
                    missiles.append(Missile(player1.x, player1.y, player1.angle))
                    cooldown_left = cooldown_max
            
            #checking for player 2 movement
            if (kbinput == "j"):
                p2_move_left = True
                p2_move_right = False
            if (kbinput == "l"):
                p2_move_left = False
                p2_move_right = True
            if (kbinput == "k"):
                p2_move_left = False
                p2_move_right = False
            if (kbinput == "u"):
                p2_rotate_right = False
                p2_rotate_left = True
            if (kbinput == "o"):
                p2_rotate_right = True
                p2_rotate_left = False
            if (kbinput == "i"):
                p2_rotate_right = False
                p2_rotate_left = False
            if (kbinput == "p"):
                if cooldown_left == 0:
                    missiles.append(Missile(player2.x, player2.y, player2.angle))
                    cooldown_left = cooldown_max


        #move player 1
        if (p1_move_right):
            player1.move_right()
        if (p1_move_left):
            player1.move_left()
        if (p1_rotate_left):
            player1.rotate_left()
        if (p1_rotate_right):
            player1.rotate_right()
        
        #move player 2
        if (p2_move_right):
            player2.move_right()
        if (p2_move_left):
            player2.move_left()
        if (p2_rotate_left):
            player2.rotate_left()
        if (p2_rotate_right):
            player2.rotate_right()
        
        if cooldown_left > 0:
            cooldown_left -= 1

        #display pause UI
        stddraw.setFontSize(20)
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.text(215, 380, "[ESC] to pause")

        #------------------------------------------------------------------------------------------
        #RE animates enemies and checks if they have reached the edge of the screen, bouncing them
        Total_left = 0                             #intitialize new variable to see amount of enemies left
        update_positions(arr, rows, cols, vx)
        rightmost, leftmost = check_wall(arr, rows, cols)
        vx = bounce(arr, rows, cols, vx, rightmost, leftmost)
         
        #------------------------------------------------------------------------------------------

        #checking if game is over
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] is not None:
                    enemy_y = arr[i][j].position.y
                    if enemy_y <= PLAYER_Y:
                        GameOn = False 

        #-------------------------------------------------------------------------------------------------------
        # RE EVANS 28891058
        #-------------------------------------------------------------------------------------------------------
        #check if all enemies have been defeated
        #Total_left = 0                                  #Creating variable to count enemies left
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] is not None:
                    Total_left += 1                     #adds to total if enemies are left
        if Total_left == 0:                             #checks to see if all enemies have been defeated
            level += 1                                  #if true, change level state to next level

        #creating new enemyarr if level has been incrimented
        if level == 1 and Total_left == 0:                 #increases velocity for level 1
            vx = abs(vx) + 2
        if level == 2 and Total_left == 0:                 #will update to level 2 if there are no enemies left
            vx = abs(vx) + 1                               #increases velocity for l2 and promps new enemy grid
            arr = enemyarr(rows, cols, level)
        if level == 3 and Total_left == 0:                 #same procedure as level 2
            vx = abs(vx) + 1                               #increases velocity and promps new enemy grid
            arr = enemyarr(rows, cols, level)
        if level == 4 and Total_left == 0:                 #same procedure as level 2
            vx = abs(vx) + 1 
            arr = enemyarr(rows, cols, level)
        if level == 5 and Total_left == 0:                 #same procedure as level 2
            arr = enemyarr(rows, cols, level)
        #-----------------------------------------------------------------------------------------------------

        #move missiles
        for missile in missiles:
            missile.move()
        
        #remove missiles goingh off screen
        missiles[:] = [m for m in missiles if m.y < 400]

        #animate collision between missile and enemy AND update score
        score += handle_missile_hits(missiles, arr, rows, cols)
        
        #animate missiles
        for missile in missiles:
            missile.draw()
        #animate bombs
        bombs.extend(bomb_drop(arr, rows, cols, level))
        for bomb in bombs:
            bomb.move_y()
            bomb.draw()
        #potentially damage players from bombs
        player_hit(player1, player2, bombs)
        if player1.hp == 0 or player2.hp == 0:
            GameOn = False
        #bunkers
#        bunker_spawn(bunkers, level)
#        bunker_hit(bombs, bunkers)
#        for b in bunkers:
#            if b.hp != 0 and b.state == True:
#                stddraw.setPenColor(stddraw.BLUE)
#                stddraw.filledRectangle(b.x, -220, 70, 20)
               

        #animate players
        player1.draw()
        player2.draw()
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.text(-250, 350, f"Score: {score}")
        stddraw.text(150, 350, f"Level: {level}")
        stddraw.text(0, 350, f"Cooldown: {cooldown_left}")
        stddraw.show(30)
    GameOver()

#-------------------------------------------------------------------------------------------------------
# RE EVANS 28891058
#-------------------------------------------------------------------------------------------------------
#This function creates an array of enemies, including different types.

def enemyarr(rows, cols, level):
    x = -200                                             #starting x pos
    y = 300                                              #starting y pos
    move_X = 40                                          #move_X and move_Y represent the distance between the enemies 
    move_Y = 40
    arr = stdarray.create2D(rows, cols, None)            #creating 2d array to store enemies 
    for i in range(0, rows):                             
        for j in range(0, cols):
            p = stdrandom.uniformFloat(0, 1)             #generating random float between 0 and 1 ro use as a probability
            if level == 1:
                arr[i][j] = Easy(x, y)                   #creating new easu enemy at positions xy and storing it at array index
            elif level == 2:                             #if level 2, continues to fill enemy grid with around 60% intermediate enemies
                if p>=0.4:                               
                    arr[i][j] = Intermediate(x, y)       #if p>=0.5 then fill that index in the array with an intermediate enemy 
                elif p<0.4:                         
                    arr[i][j] = Easy(x, y)               #if p<0.5 then fill with easy enemies
            elif level == 3:                             #functionally the same as level 2 except now it includes Hard enemies
                if p>=0.5:
                    arr[i][j] = Hard(x, y)               
                elif 0.15<=p<0.5:
                    arr[i][j] = Intermediate(x, y)
                elif p<0.15:
                    arr[i][j] = Easy(x, y)
            elif level == 4:                             #functionally the same as level 2 except now it includes Hard enemies
                if p>=0.5:
                    arr[i][j] = Vhard(x, y)               
                elif 0.15<=p<0.5:
                    arr[i][j] = Hard(x, y)
                elif p<0.15:
                    arr[i][j] = Intermediate(x, y)
            elif level == 5:                             #if level 2, continues to fill enemy grid with around 60% intermediate enemies
                if p>=0.4:                               
                    arr[i][j] = Ehard(x, y)       #if p>=0.5 then fill that index in the array with an intermediate enemy 
                elif p<0.4:                         
                    arr[i][j] = Vhard(x, y)               #if p<0.5 then fill with easy enemies
            x += move_X                                  #shifting x in row
        y -= move_Y                                      #shifting y in col
        x -= move_X*cols                                 #returning to origional x after each row
    return arr

#----------------
#update_positions/ Takes enemy array, dimentions and velocity as arguments

def update_positions(arr, rows, cols, vx):              
    for i in range(0, rows):
        for j in range(0, cols):
            if arr[i][j] is not None:
                arr[i][j].position.x += vx               #increases all elements x position by the velocity in the x direction

#---------------
#check ifwall/ takes enemy array and dimentions as arguments

def check_wall(arr, rows, cols):
    rightmost = -10000                                   #abitrary large/ small values so that our position is never greater
    leftmost = 10000                                     #this just makes it so that the first check where posX is greater/ smaller ->
    for i in range(0, rows):                             #-> than an arbitrarily small/ large number is always true
        for j in range(0, cols):
            if arr[i][j] is not None:                    #true only for remaining enemies 
                positionX = arr[i][j].position.x         #holds x position of enemy           
                if positionX > rightmost:                #looking for the remaining enemy closest to the right in the array
                    rightmost = positionX
                if positionX < leftmost:                 #looking for closest to left
                    leftmost = positionX
    return rightmost, leftmost                           #values used to see when to bounce off of the wall

#------------------------------------------
#changes the direction if there is a wall

def bounce(arr, rows, cols, vx, rightmost, leftmost):                   
    if leftmost-ENEMY_RADIUS<=-300 or rightmost+ENEMY_RADIUS>=300:             #seeing if either end touches a wall
        vx = -vx                                         #if so changes direction
        for i in range(0, rows):
            for j in range(0, cols):
                if arr[i][j] is not None:
                    arr[i][j].position.y -= 45           #after bouncing it also decreases all elements y value
    return vx

#-------------------------
#draws the updated enemy

def draw_updatedEnemy(arr, rows, cols):
    for i in range(0, rows):
        for j in range(0, cols):
            if arr[i][j] is not None and arr[i][j].hp == 1:
                stddraw.picture(Picture("enemy1.png"), arr[i][j].position.x, arr[i][j].position.y)
                #stddraw.setPenColor(stddraw.YELLOW)
                #stddraw.filledCircle(arr[i][j].position.x, arr[i][j].position.y, ENEMY_RADIUS) #draws enemy
            elif arr[i][j] is not None and arr[i][j].hp == 2:
                stddraw.picture(Picture("enemy2.png"), arr[i][j].position.x, arr[i][j].position.y)
                #stddraw.setPenColor(stddraw.ORANGE)
                #stddraw.filledCircle(arr[i][j].position.x, arr[i][j].position.y, ENEMY_RADIUS) #draws enemy
            elif arr[i][j] is not None and arr[i][j].hp == 3:
                stddraw.picture(Picture("enemy3.png"), arr[i][j].position.x, arr[i][j].position.y)
                #stddraw.setPenColor(stddraw.RED)
                #stddraw.filledCircle(arr[i][j].position.x, arr[i][j].position.y, ENEMY_RADIUS) #draws enemy
            elif arr[i][j] is not None and arr[i][j].hp == 4:
                stddraw.picture(Picture("enemy4.png"), arr[i][j].position.x, arr[i][j].position.y)
            elif arr[i][j] is not None and arr[i][j].hp == 5:
                stddraw.picture(Picture("enemy5.png"), arr[i][j].position.x, arr[i][j].position.y)

#------------
#drops bomb

def bomb_drop(arr, rows, cols, level):
    bombs = []
    if level >= 2:
        for i in range(0, rows):
            for j in range(0, cols):
                p2 = stdrandom.uniformFloat(0, 1)
                if p2<=0.0015 and arr[i][j] is not None:
                    bomb_x = arr[i][j].position.x
                    bomb_y = arr[i][j].position.y
                    bombs.append(Bomb(bomb_x, bomb_y))
    return bombs

#-------------
#checks if bomb hit player

def player_hit(player1, player2, bombs):
    for bomb in bombs[:]:
        if ((bomb.x <= player1.x+PLAYER_RADIUS and bomb.x >= player1.x-PLAYER_RADIUS) and (bomb.y <= player1.y+PLAYER_RADIUS and bomb.y >= player1.y-PLAYER_RADIUS)):
            player1.damagetaken(1)
            bombs.remove(bomb)
        elif ((bomb.x <= player2.x+PLAYER_RADIUS and bomb.x >= player2.x-PLAYER_RADIUS) and (bomb.y <= player2.y+PLAYER_RADIUS and bomb.y >= player2.y-PLAYER_RADIUS)):
            player2.damagetaken(1)
            bombs.remove(bomb)

#prints player hp
def print_Playerhp(player1, player2):
    stddraw.setPenColor(stddraw.RED)
    if player1.hp == 1:
        stddraw.filledCircle(-185, 358, 5)
    if player1.hp == 2:
        stddraw.filledCircle(-185, 358, 5)
        stddraw.filledCircle(-170, 358, 5)
    if player1.hp == 3:
        stddraw.filledCircle(-185, 358, 5)
        stddraw.filledCircle(-170, 358, 5)
        stddraw.filledCircle(-155, 358, 5)

    stddraw.setPenColor(stddraw.BLUE)
    if player2.hp == 1:
        stddraw.filledCircle(-185, 342, 5)
    if player2.hp == 2:
        stddraw.filledCircle(-185, 342, 5)
        stddraw.filledCircle(-170, 342, 5)
    if player2.hp == 3:
        stddraw.filledCircle(-185, 342, 5)
        stddraw.filledCircle(-170, 342, 5)
        stddraw.filledCircle(-155, 342, 5)

#randomly spawns a player bunker
#def bunker_spawn(bunkers, level):
#    if level >= 2:
#        p = stdrandom.uniformFloat(0, 1)
#        if p<=0.01:
#            remaining_bunkers = [b for b in bunkers if b.hp != 0]
#            if remaining_bunkers:
#                p2 = stdrandom.uniformInt(0, len(remaining_bunkers))
#                b = remaining_bunkers[p2]
#                b.state = True

#def bunker_hit(bombs, bunkers):
#    for bomb in bombs[:]:
#        for bunker in bunkers:
#            if ((bomb.x <= bunker.x+BUNKER_HALFLENGTH and bomb.x >= bunker.x-BUNKER_HALFLENGTH) and (bomb.y <= -200 and bomb.y >= -240)):
#                bunker.damagetaken(1)
#                bombs.remove(bomb)

        
#-----------------------------------------------------------------------------------------------------------
# J Klagsbrun 29076137
#------------------------
def handle_missile_hits(missiles, arr, rows, cols):
    score_increase = 0
    rows = len(arr)
    cols = len(arr[0])

    missiles_to_remove = []

    for missile in missiles:
        for i in range(rows):
            for j in range(cols):

                if arr[i][j] is None:
                    continue

                enemy_x = arr[i][j].position.x
                enemy_y = arr[i][j].position.y

                dx = missile.x - enemy_x
                dy = missile.y - enemy_y

                distance_squared = dx * dx + dy * dy
                
                #removing hit enemy
                if distance_squared <= (ENEMY_RADIUS + 5) ** 2:
                    arr[i][j].hp -= 1                                 #RE subtracts 1 hp every time is hit
                    missiles_to_remove.append(missile)
                    if arr[i][j].hp == 0:                             #RE if hp is 0 then it removes enemy 
                        arr[i][j] = None
                        score_increase += 1
    
    #removing missiles 
    for m in missiles_to_remove:
        if m in missiles:
            missiles.remove(m)

    return score_increase

def main() -> None:

    global GameOn

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
                    GameOn = True
                    beginGame()
                    break
            stddraw.show(10)


if __name__ == "__main__": main()

