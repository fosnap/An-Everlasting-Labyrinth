import random
import msvcrt
from time import sleep

def playspace(space, farx, fary, borderx, bordery, clutter_set):
    for border_line in range(bordery):
        space.append(''.join("@" * (farx + (borderx * 2))))
    for full_row in range(fary):
        full_line = [''.join("@" * borderx)]
        for column in range(farx):
            full_line.append(clutter_set[random.randint(0,
                                                        len(clutter_set) - 1)])
        if full_row == fary//2:
            del full_line[-1]
            full_line.append(" " * (borderx + 1))
        else:
            full_line.append("@" * borderx)
        space.append(''.join(full_line))
    for border_line in range(bordery):
        space.append(''.join("@" * farx))
    space = ''.join(space)
    return 

def render(board, xpos, length, ypos, height, curser):
    print("@" * length)
    for row in range(ypos, ypos + height - 2):
        line = "@"
        for column in range(xpos , xpos + length - 2):
            if row == ypos + (height//2)  and column == xpos + (length//2):
                line += curser
            else:
                line += board[row][column]
        line += "@"
        print(line)
    print("@" * length)
    return

#set to inventory
##def display(ship_bay, cargo):
##    ship = [
##        """ Cockpit
##     _  ______/|
##  _/_O_|       |<|
## /     |_______|<|
## \_____|_______|<|""",
##
##        """ Crew quarters
##    ___ ______/|
##  _/ _ |       |<|
## /     |_______|<|
## \_ _ _|_______|<|""",
##
##        """ Engine room
##    ___  _ _ _/|
##  _/___|       |<|
## /     |_ _ _ _|<|
## \_____|_______|<|""",
##
##        """ Cargo
##    ___ ______/|
##  _/___|       |<|
## /     | _ _ _ |<|
## \_____|_ _ _ _|<|""",
##
##        """ Cargo
##    ___ ______/|
##  _/___|       |<|
## /     | _ _ _ |<|
## \_____|# _ _ _|<|""",
##
##        """ Cargo
##    ___ ______/|
##  _/___|       |<|
## /     | _ _ _ |<|
## \_____|##_ _ _|<|""",
##
##        """ Cargo
##    ___ ______/|
##  _/___|       |<|
## /     | _ _ _ |<|
## \_____|### _ _|<|""",
##
##        """ Cargo
##    ___ ______/|
##  _/___|       |<|
## /     | _ _ _ |<|
## \_____|####_ _|<|""",
##
##        """ Cargo
##    ___ ______/|
##  _/___|       |<|
## /     | _ _ _ |<|
## \_____|##### _|<|""",
##
##        """ Cargo
##    ___ ______/|
##  _/___|       |<|
## /     | _ _ _ |<|
## \_____|######_|<|""",
##
##        """ Cargo
##    ___ ______/|
##  _/___|       |<|
## /     | _ _ _ |<|
## \_____|#######|<|"""]
##
##    if cargo > 7:
##        cargo = 7
##    
##    if ship_bay == 3 and 0 < cargo <= 7:
##        ship_bay += cargo
##    
##    print(ship[ship_bay])
##    return

def run(max_width, max_height, window_width, window_height):
##    print("\n Your ship has successfully undocked.\n",
##          "\n In case you were asleep during briefing:\n",
##          "w, s, 8, and 2 will change the pitch of this ship\n",
##          "a, d, 4, and 6 will turn this ship\n\n",
##          "i, and 1 will allow you to check up on this ship\n",
##          "o, and 3 will make you see stars\n\n",
##          "e, and 5 allow you to select options\n\n",
##          "q will dock your ship")
    input("\n\n\n\n If you are in full screen and ready to proceed, press enter.\n >>> ")
##    print("\n Loading presets")

    space = []
    xpos = 590
    xrange = window_width - 1
    ypos = max_height//2
    yrange = window_height - 3
    curser = ">"
    health = 10
    youre_winner = False

    clutter = [" ","_"," ","|"," ",
               "_"," ","|"," ","_",
               " ","|"," ","_"," ",
               "|"," ","_"," ","|"]
##    labels = [" Space"," Space"," Space"," Space"," Distant star",
##              " Space"," Space"," Space"," Space"," Star",
##              " Space"," Space"," Space"," Space"," Debris",
##              " Space"," Space"," Space"," Space"]

##    print("\n Done")
##
##    print("\n Loading space")
    playspace(space, max_width, max_height, xrange//2, yrange//2, clutter)
##    print("\n Done")
##
##    print("\n Load complete\n>>>")
    while youre_winner == False:
        print(curser * health, xpos, ypos)
        render(space, xpos, xrange, ypos, yrange, curser)
        print(" >>> ")
        direction = msvcrt.getch();

        if direction == b'w' or direction == b'8':
            if ypos <= 0:
                ypos = 0
            elif space[ypos + yrange//2 - 1][xpos + xrange//2] == "_":
                pass
            elif space[ypos + yrange//2 - 1][xpos + xrange//2] == "|":
                pass
            else:
                ypos -= 1
            curser = "^"

        elif direction == b's' or direction == b'2':
            if ypos + yrange >= len(space):
                ypos = len(space) - yrange
            elif space[ypos + yrange//2][xpos + xrange//2] == "_":
                pass
            elif space[ypos + yrange//2 + 1][xpos + xrange//2] == "|":
                pass
            else:
                ypos += 1
            curser = "v"

        elif direction == b'a' or direction == b'4':
            if xpos <= 0:
                xpos = 0
            elif space[ypos + yrange//2][xpos + xrange//2 - 1] == "|":
                pass
            else:
                xpos -= 1
            curser = "<"

        elif direction == b'd' or direction == b'6':
            if xpos + 1 == max_width and ypos == max_height//2:
                youre_winner = True
                break
            elif xpos + xrange >= len(space[ypos]):
                xpos = len(space[ypos]) - xrange
            elif space[ypos + yrange//2][xpos + xrange//2 + 1] == "|":
                pass
            else:
                xpos += 1
            curser = ">"

        elif direction == b'e' or direction == b'5':
            pass
##                if space[ypos+yrange//2][xpos+xrange//2]=="#"and debris_in_cargo < 7:
##                    space[ypos+yrange//2][xpos+xrange//2]=clutter[random.randint(0,len(clutter) - 1)]
##                    debris_in_cargo += 1
##                if debris_in_cargo > 7:
##                    debris_in_cargo = 7
                
        elif direction == b'i' or direction == b'1':
            #inventory
            pass

        elif direction == b'q':
            break

    if youre_winner == True:
        doorway = 1
        for line in range(window_height):
            print("#" * xrange)
        sleep(1)
        for frame in range(xrange//2 + 1):
            for line in range(window_height - doorway//2):
                print("#" * xrange)
            for line in range(doorway//2):
                wall = xrange//2 - doorway//2
                print("#" * wall + " " * doorway + "#" * wall)
            doorway += 2
            sleep(0.125)
    elif direction == b'q':
        print("\n Thanks for playing")
    return

run(600, 600, 168, 44)
