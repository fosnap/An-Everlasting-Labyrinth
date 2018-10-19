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
        space.append(''.join("@" * (farx + (borderx * 2))))
    space = ''.join(space)
    return 

def render(board, xpos, length, ypos, height, curser):#, enemy_list, enemy_xpos, enemy_ypos):
    print("@" * length)
    for row in range(ypos, ypos + height - 2):
        line = "@"
        for column in range(xpos , xpos + length - 2):
            filled = False
##            for enemy in enemy_list:
##                if row == enemy_ypos[enemy] and column == enemy_xpos[enemy]:
##                    line += "H"
##                    filled = True
##                    break
            if filled == False:
                if row == ypos + (height//2)  and column == xpos + (length//2):
                    line += curser
                else:
                    line += board[row][column]
        line += "@"
        print(line)
    print("@" * length)
    return

def run(max_width, max_height, window_width, window_height):
    space = []
    xpos = 0
    global xrange
    xrange = window_width - 1
    ypos = max_height//2
    global yrange
    yrange = window_height - 3
    curser = ">"
    health = 10
    global youre_winner
    youre_winner = False
    clutter = [" ","_"," ","|"," ",
               "_"," ","|"," ","_",
               " ","|"," ","_"," ",
               "|"," ","_"," ","|"]
    
##    hostile = 0
##    enemy_list = [0]
##    enemy_xpos = []
##    enemy_ypos = []
##    while (2 ** (hostile + 1)) < (((max_width**2) + (max_height**2))**(1/2))//1:
##        hostile += 1
##        enemy_list.append(hostile)

    playspace(space, max_width, max_height, xrange//2, yrange//2, clutter)

##    for enemy in range(hostile + 1):
##        enemy_x = random.randint(xrange//2, max_width + xrange//2)
##        enemy_y = random.randint(yrange//2, max_height + yrange//2)
##        while space[enemy_y][enemy_x] == "|" or space[enemy_y][enemy_x] == "@" or space[enemy_y][enemy_x] == "H":
##            if enemy_x > xrange//2:
##                enemy_x -= 1
##
##            elif enemy_x == xrange//2:
##                if enemy_y < (max_height + yrange)//2:
##                    enemy_y += 1
##                elif enemy_y > (max_height + yrange)//2:
##                    enemy_y -= 1
##
##        enemy_xpos.append(enemy_x)
##        enemy_ypos.append(enemy_y)


    while youre_winner == False:
        print(curser * health)
        render(space, xpos, xrange, ypos, yrange, curser)#, enemy_list, enemy_xpos, enemy_ypos)
        print(" >>> ")
        global direction
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

        elif direction == b'r':
            break

        elif direction == b'q':
            break

    return

# let user set perameters
size_key =["~","!","@","#","$","%","^","&","*","(",")","_","+","Q","W","E","R","T","Y","U","I","O","P","{","}","|","A","S","D","F","G","H","J","K","L",":","\"","Z","X","C","V","B","N","M","<",">","?","`","1","2","3","4","5","6","7","8","9","0","-","=","q","w","e","r","t","y","u","i","o","p","[","]","\\","a","s","d","f","g","h","j","k","l",";","'","z","x","c","v","b","n","m",",",".","/"]
print(" Welcome to an everlasting labyrinth.")
if "n" in input("\n Have you been here before?\n >>> "):
    print(" Ok...\n\n\n",
          "Watching from above, you are in control of the arrow in the middle of the screen.\n\n",
          "The \"W\" key will move the arrow toward the top of the screen. ^\n",
          "The \"A\" key will do the same toward the left. <\n",
          "The \"S\" key will send the arrow down. v\n",
          "And \"D\" for rightward movement.>\n\n",
          "\"Q\" quits\n and \"R\" resets the current level, if you get boxed in.")
    
else:
    print(" Good")

if "n" in input("\n\n Do you know how many characters this window can display vertically?\n >>> "):
    for key in size_key:
        print(key)
    size_key.reverse()
    tall_size = size_key.index(str(input(" What character is the closest to the top of the screen?(case matters)\n >>> "))) + 3
else:
    tall_size = int(input(" Window height\n >>> "))

if "n" in input("\n\n Do you know how many characters this window can display horizontally?\n >>> "):
    print(' '.join(size_key))
    wide_size = size_key.index(str(input(" What character is the closest to the edge of the screen before overflow?(case matters)\n >>> "))) * 2
else:
    wide_size = int(input(" Window width\n >>> "))

full_size = 10
run(full_size * 2, full_size, wide_size, tall_size)
# 600 600 168 44
level = 1

while True:
    if youre_winner == True:
        doorway = 1
        for line in range(tall_size):
            ceiling = xrange - (line * 2)
            print("@" * line + "#" * ceiling + "@" * line)
        sleep(0.125)
        for frame in range(xrange//2 + 1):
            wait = 0.03125
            for line in range(tall_size - doorway//2):
                ceiling = xrange - (line * 2)
                print("@" * line + "#" * ceiling + "@" * line)
                wait = 0.125
            for line in range(doorway//2):
                wall = xrange//2 - doorway//2
                print("@" * wall + " " * doorway + "@" * wall)
            doorway += 2
            sleep(wait)
        full_size *= 5
        run(full_size * 2, full_size, wide_size, tall_size)
        level += 1

    elif direction == b'r':
        run(full_size * 2, full_size, wide_size, tall_size)
        
    else:
        print("\n Thanks for playing\n You made it to level", level)
        break
