import random
from time import sleep

def playspace(space, farx, fary, borderx, bordery, clutter_set):
    for border_line in range(bordery):
        space.append(''.join(clutter_set[1] * (farx + (borderx * 2))))
    for full_row in range(fary):
        full_line = [''.join(clutter_set[1] * borderx)]
        for column in range(farx):
            full_line.append(clutter_set[random.randint(0, len(clutter_set) - 1)])
        if full_row == fary//2:
            del full_line[-1]
            full_line.append(clutter_set[0] * (borderx + 1))
        else:
            full_line.append(clutter_set[1] * borderx)
        space.append(''.join(full_line))
    for border_line in range(bordery):
        space.append(''.join(clutter_set[1] * (farx + (borderx * 2))))
    space = ''.join(space)
    return 

def render(board, xpos, length, ypos, height, curser, health, enemy_list, enemy_xpos, enemy_ypos):
    screen = []
    screen.append(curser * health)
    screen.append("#" * length)
    for row in range(ypos, ypos + height - 2):
        line = "#"
        for column in range(xpos , xpos + length - 2):
            filled = False
            for enemy in enemy_list:
                if row == enemy_ypos[enemy] + (height//2) and column == enemy_xpos[enemy] + (length//2):
                    line += "H"
                    filled = True
                    if row == ypos + (height//2)  and column == xpos + (length//2):
                        health -= 1
                    
            if filled == False:
                if row == ypos + (height//2)  and column == xpos + (length//2):
                    line += curser
                else:
                    line += board[row][column]
        line += "#"
        screen.append(line)
    screen.append("#" * length)
    print('\n'.join(screen))
    return health

def run(max_width, max_height, window_width, window_height):
    space = []
    xpos = 0
    global xrange
    xrange = window_width - 1
    ypos = max_height//2
    global yrange
    yrange = window_height - 2
    curser = ">"
    health = 10
    global youre_winner
    youre_winner = False
    clutter = [" ","█"," "," "]#[" ","_"," ","|"," ",
               #"_"," ","|"," ","_",
               #" ","|"," ","_"," ",
               #"|"," ","_"," ","|"]
    
    hostile = 0
    enemy_list = [0]
    enemy_xpos = []
    enemy_ypos = []
    while (2 ** (hostile + 1)) < (((max_width**2) + (max_height**2))**(1/2))//1:
        hostile += 1
        enemy_list.append(hostile)

    playspace(space, max_width, max_height, xrange//2, yrange//2, clutter)
##    while check(space, xrange, yrange) == "failure":
##        playspace(space, max_width, max_height, xrange//2, yrange//2, clutter)

    for enemy in range(hostile + 1):
        enemy_x = random.randint(0, max_width)
        enemy_y = random.randint(0, max_height)
        while space[enemy_y + yrange//2][enemy_x + xrange//2] == clutter[1]:
            enemy_x = random.randint(0, max_width)
            enemy_y = random.randint(0, max_height)
#            if enemy_x > max_width//2:
#                enemy_x -= 1

#            if enemy_x < max_width//2:
#                enemy_x += 1

#            if enemy_x == xrange//2:
#                if enemy_y < max_height//2:
#                    enemy_y += 1
#                if enemy_y > max_height//2:
#                    enemy_y -= 1

        enemy_xpos.append(enemy_x)
        enemy_ypos.append(enemy_y)


    while youre_winner == False and health > 0 :
        #print(curser * health)
        health = render(space, xpos, xrange, ypos, yrange, curser, health, enemy_list, enemy_xpos, enemy_ypos)
        global direction
        if microsoft_cmd == True:
            direction = msvcrt.getch()

            if b'w' in direction or b'8' in direction:
                if ypos <= 0:
                    ypos = 0
    ##            elif space[ypos + yrange//2 - 1][xpos + xrange//2] == "_":
    ##                pass
                elif space[ypos + yrange//2 - 1][xpos + xrange//2] == clutter[1]:
                    pass
                else:
                    ypos -= 1
                curser = "^"

            elif b's' in direction or b'2' in direction:
                if ypos + yrange >= len(space):
                    ypos = len(space) - yrange
    ##            elif space[ypos + yrange//2][xpos + xrange//2] == "_":
    ##                pass
                elif space[ypos + yrange//2 + 1][xpos + xrange//2] == clutter[1]:
                    pass
                else:
                    ypos += 1
                curser = "v"

            elif b'a' in direction or b'4' in direction:
                if xpos <= 0:
                    xpos = 0
                elif space[ypos + yrange//2][xpos + xrange//2 - 1] == clutter[1]:
                    pass
                else:
                    xpos -= 1
                curser = "<"

            elif b'd' in direction or b'6' in direction:
                if xpos + 1 == max_width and ypos == max_height//2:
                    youre_winner = True
                    break
                elif xpos + xrange >= len(space[ypos]):
                    xpos = len(space[ypos]) - xrange
                elif space[ypos + yrange//2][xpos + xrange//2 + 1] == clutter[1]:
                    pass
                else:
                    xpos += 1
                curser = ">"

            elif b'e' in direction or b'5' in direction:
                pass

            elif b'r' in direction:
                break

            elif b'q' in direction:
                break

        else:
            direction = input(">>> ")

            if 'w' in direction or '8' in direction:
                if ypos <= 0:
                    ypos = 0
    ##            elif space[ypos + yrange//2 - 1][xpos + xrange//2] == "_":
    ##                pass
                elif space[ypos + yrange//2 - 1][xpos + xrange//2] == clutter[1]:
                    pass
                else:
                    ypos -= 1
                curser = "^"

            elif 's' in direction or '2' in direction:
                if ypos + yrange >= len(space):
                    ypos = len(space) - yrange
    ##            elif space[ypos + yrange//2][xpos + xrange//2] == "_":
    ##                pass
                elif space[ypos + yrange//2 + 1][xpos + xrange//2] == clutter[1]:
                    pass
                else:
                    ypos += 1
                curser = "v"

            elif 'a' in direction or '4' in direction:
                if xpos <= 0:
                    xpos = 0
                elif space[ypos + yrange//2][xpos + xrange//2 - 1] == clutter[1]:
                    pass
                else:
                    xpos -= 1
                curser = "<"

            elif 'd' in direction or '6' in direction:
                if xpos + 1 == max_width and ypos == max_height//2:
                    youre_winner = True
                    break
                elif xpos + xrange >= len(space[ypos]):
                    xpos = len(space[ypos]) - xrange
                elif space[ypos + yrange//2][xpos + xrange//2 + 1] == clutter[1]:
                    pass
                else:
                    xpos += 1
                curser = ">"

            elif 'e' in direction or '5' in direction:
                pass

            elif 'r' in direction:
                break

            elif 'q' in direction:
                break


    return

# let user set perameters
size_key =["~","!","@","#","$","%","^","&","*","(",")","_","+","Q","W","E","R","T","Y","U","I","O","P","{","}","|","A","S","D","F","G","H","J","K","L",":","\"","Z","X","C","V","B","N","M","<",">","?","`","1","2","3","4","5","6","7","8","9","0","-","=","q","w","e","r","t","y","u","i","o","p","[","]","\\","a","s","d","f","g","h","j","k","l",";","'","z","x","c","v","b","n","m",",",".","/"]
print(" Welcome to an everlasting labyrinth.")
if "n" in input("\n Have you been here before?\n>>> "):
    print(" Ok...\n\n\n",
          "Watching from above, you are in control of the arrow in the middle of the screen.\n\n",
          "The \"W\" key will move the arrow toward the top of the screen. ^\n",
          "The \"A\" key will do the same toward the left. <\n",
          "The \"S\" key will send the arrow down. v\n",
          "And \"D\" for rightward movement.>\n\n",
          "\"Q\" quits\n and \"R\" resets the current level, if you get boxed in.")
    
else:
    print(" Good")

global microsoft_cmd
if "n" not in input("\n\n Is this program running in Microsoft command line?\n>>> "):
    microsoft_cmd = True
    import msvcrt
else:
    microsoft_cmd = False

if "n" in input("\n\n Do you know how many characters this window can display vertically?\n>>> "):
    for key in size_key:
        print(key)
    size_key.reverse()
    tall_size = size_key.index(str(input(" What character is the closest to the top of the screen?(case matters)\n>>> "))) + 3
else:
    tall_size = int(input(" Window height\n>>> "))

if "n" in input("\n\n Do you know how many characters this window can display horizontally?\n>>> "):
    print(' '.join(size_key))
    wide_size = size_key.index(str(input(" What character is the closest to the edge of the screen before overflow?(case matters)\n>>> "))) * 2
else:
    wide_size = int(input(" Window width\n>>> "))

full_size = 10
run(full_size * 2, full_size, wide_size, tall_size)
# 600 600 168 44
level = 1

while True:
    if youre_winner == True:
        doorway = 1
        for line in range(tall_size):
            ceiling = xrange - (line * 2)
            print("█" * line + "#" * ceiling + "█" * line)
        sleep(0.125)
        for frame in range(xrange//2 + 1):
            display_frame = []
            wait = 0.03125
            for line in range(tall_size - doorway//2):
                ceiling = xrange - (line * 2)
                display_frame.append("█" * line + "#" * ceiling + "█" * line)
                wait = 0.125
            for line in range(doorway//2):
                wall = xrange//2 - doorway//2
                display_frame.append("█" * wall + " " * doorway + "█" * wall)
            print('\n'.join(display_frame))
            doorway += 2
            sleep(wait)
        full_size *= 2
        run(full_size * 2, full_size, wide_size, tall_size)
        level += 1

    elif direction == b'r' or direction == 'r':
        run(full_size * 2, full_size, wide_size, tall_size)
        
    else:
        print("\n Thanks for playing\n You made it to level", level)
        sleep(5)
        break
