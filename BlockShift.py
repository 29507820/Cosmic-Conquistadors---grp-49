import stddraw
import sys
import stdio
import stdarray

RADIUS = 0.04

def main():
    #creating array to store positions in
    stddraw.setXscale(-1.0, 1.0)
    stddraw.setYscale(-1.0, 1.0)
    y = 3
    x = 5
    k = 0
    pos = stdarray.create2D(y, x, 0.0)
    for i in range(0, y):
        for j in range(0, x):
            pos[i][j]= k
            k += 0.1
        k = 0
    vx = 0.0002 #velocity in x direction
    ry = 1
    #loop to move positions
    while ry-0.3>-1: #while the last row is not out of frame
        if abs(pos[0][0]+vx) + RADIUS > 1.0 or abs(pos[0][x -1]+vx) + RADIUS > 1.0: #depending on position of last/first element, shift row right or left
            vx = -vx
            ry = ry - 0.1
        for i in range(0, y):
            for j in range(0, x):
                pos[i][j] += vx

        stddraw.clear(stddraw.GRAY)
        for i in range(0, y):
            for j in range(0, x):
                stddraw.filledCircle(pos[i][j], ry-i*0.1, RADIUS)
        stddraw.show(0)

    sys.exit()

if __name__ == '__main__': main()



