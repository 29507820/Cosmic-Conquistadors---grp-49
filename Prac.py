import stddraw #Type: ignore

def main() -> None:

    # Display menu screen
    
    # set size and background
    stddraw.setCanvasSize(600, 750)
    stddraw.setXscale(0, 600)
    stddraw.setYscale(0, 750)
    
    stddraw.setPenColor(stddraw.GRAY)
    stddraw.filledSquare(0,0,1000)
    
    # Add Text
    stddraw.setPenColor(stddraw.WHITE)

    stddraw.setFontSize(42)
    stddraw.text(300, 700, "COSMIC CONQUISTADORS")

    stddraw.setFontSize(28)
    stddraw.text(300, 600, "INSTRUCTIONS:")

    stddraw.setFontSize(24)
    stddraw.text(300, 550, "[A] Move Left, [S] Stop Moving, [D] Move right")
    stddraw.text(300, 500, "[Q] rotate left, [W] stop rotate, [E] rotate right")
    stddraw.text(300, 450, "[Space] to shoot")
    stddraw.text(300, 350, "[H] for help")
    stddraw.text(300, 300, "[X] to quit")
    stddraw.text(300, 150, "Press any key to start")
    
    # Display menu (5 seconds for now, Code quit button later)
    stddraw.show(5000)

if __name__ == "__main__": main()

