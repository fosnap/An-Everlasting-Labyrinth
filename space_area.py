import random
import msvcrt

def playspace(space, farx, fary, clutter_set):
    for full_row in range(fary):
        full_line = []
        for full_column in range(farx):
            full_line.append(clutter_set[random.randint(0,
                                                        len(clutter_set) - 1)])
        space.append(full_line)
    return 

def render(board, clutter, labels, xpos, length, ypos, height, curser):
    if ypos + height < len(board):
        if xpos + length < len(board[0]):
            print(labels[clutter.index(board[ypos+(height//2)][xpos+(length//2)])])
            print("_" * length)
            for row in range(ypos, ypos + height - 2):
                line = "|"
                for column in range(xpos, xpos + length - 2):
                    if row == ypos + (height//2) and column == xpos + (length//2):
                        line += curser
                    else:
                        line += board[row][column]
                line += "|"
                print(line)
            print("I" * length)
    return

def display(ship_bay, cargo):
    ship = [
        """ Cockpit
     _  ______/|
  _/_O_|       |<|
 /     |_______|<|
 \_____|_______|<|""",

        """ Crew quarters
    ___ ______/|
  _/ _ |       |<|
 /     |_______|<|
 \_ _ _|_______|<|""",

        """ Engine room
    ___  _ _ _/|
  _/___|       |<|
 /     |_ _ _ _|<|
 \_____|_______|<|""",

        """ Cargo
    ___ ______/|
  _/___|       |<|
 /     | _ _ _ |<|
 \_____|_ _ _ _|<|""",

        """ Cargo
    ___ ______/|
  _/___|       |<|
 /     | _ _ _ |<|
 \_____|# _ _ _|<|""",

        """ Cargo
    ___ ______/|
  _/___|       |<|
 /     | _ _ _ |<|
 \_____|##_ _ _|<|""",

        """ Cargo
    ___ ______/|
  _/___|       |<|
 /     | _ _ _ |<|
 \_____|### _ _|<|""",

        """ Cargo
    ___ ______/|
  _/___|       |<|
 /     | _ _ _ |<|
 \_____|####_ _|<|""",

        """ Cargo
    ___ ______/|
  _/___|       |<|
 /     | _ _ _ |<|
 \_____|##### _|<|""",

        """ Cargo
    ___ ______/|
  _/___|       |<|
 /     | _ _ _ |<|
 \_____|######_|<|""",

        """ Cargo
    ___ ______/|
  _/___|       |<|
 /     | _ _ _ |<|
 \_____|#######|<|"""]

    if cargo > 7:
        cargo = 7
    
    if ship_bay == 3 and 0 < cargo <= 7:
        ship_bay += cargo
    
    print(ship[ship_bay])
    return

def run(max_width, max_height, window_width, window_height):
    print("\n Your ship has successfully undocked.\n",
          "\n In case you were asleep during briefing:\n",
          "w, s, 8, and 2 will change the pitch of this ship\n",
          "a, d, 4, and 6 will turn this ship\n\n",
          "i, and 1 will allow you to check up on this ship\n",
          "o, and 3 will make you see stars\n\n",
          "e, and 5 allow you to select options\n\n",
          "q will dock your ship")
    input("\n\n\n\n If you are in full screen and ready to proceed, press enter.\n >>> ")
    print("\n Loading presets")

    space = []
    bay = 0
    xpos = max_width//2
    xrange = window_width - 1
    ypos = max_height//2
    yrange = window_height - 3
    curser = "+"
    debris_in_cargo = 0
    storage = 0

    clutter = [" "," "," "," ",".",
               " "," "," "," ","*",
               " "," "," "," ","#",
               " "," "," "," "]
    labels = [" Space"," Space"," Space"," Space"," Distant star",
              " Space"," Space"," Space"," Space"," Star",
              " Space"," Space"," Space"," Space"," Debris",
              " Space"," Space"," Space"," Space"]
    in_space = True
    print("\n Done")

    print("\n Loading space")
    playspace(space, max_width, max_height, clutter)
    print("\n Done")

    print("\n Load complete\n>>>")
    while True:
        if in_space == True:
            render(space, clutter, labels, xpos, xrange, ypos, yrange, curser)
            print(" >>> ")
            direction = msvcrt.getch();

            if direction == b'w' or direction == b'2':
                if ypos <= 0:
                    ypos = 0
                else:
                    ypos -= 1

            elif direction == b's' or direction == b'8':
                if ypos + yrange >= len(space) - 1:
                    ypos = (len(space) - 1) - yrange
                else:
                    ypos += 1

            elif direction == b'a' or direction == b'4':
                if xpos <= 0:
                    xpos = 0
                else:
                    xpos -= 1

            elif direction == b'd' or direction == b'6':
                if xpos + xrange >= len(space[0]) -1:
                    xpos = (len(space[0]) - 1) - xrange
                else:
                    xpos += 1

            elif direction == b'e' or direction == b'5':
                if space[ypos+yrange//2][xpos+xrange//2]=="#"and debris_in_cargo < 7:
                    space[ypos+yrange//2][xpos+xrange//2]=clutter[random.randint(0,len(clutter) - 1)]
                    debris_in_cargo += 1
                if debris_in_cargo > 7:
                    debris_in_cargo = 7
                    
            elif direction == b'i' or direction == b'1':
                in_space = False

            elif direction == b'q':
                break

        elif in_space == False:
            display(bay, debris_in_cargo)
            print("\n" * (yrange - 4), ">>> ")
            choose_bay = msvcrt.getch();

            if choose_bay == b'w' or choose_bay == b'8':
                if bay == 1:
                    bay = 0

                elif bay == 3:
                    bay = 2

            elif choose_bay == b's' or choose_bay == b'2':
                if bay == 0:
                    bay = 1

                elif bay == 2:
                    bay = 3

            elif choose_bay == b'a' or choose_bay == b'4':
                if bay == 2:
                    bay = 0

                elif bay == 3:
                    bay = 1

            elif choose_bay == b'd' or choose_bay == b'6':
                if bay == 0:
                    bay = 2

                elif bay == 1:
                    bay = 3

            elif choose_bay == b'e' or choose_bay == b'5':
                if bay == 0:
                    display(bay, debris_in_cargo)
                    print(" Would you like to change your curser?",
                          "\n" * (yrange - 4))
                    cockpit_answer = input(" >>> ").strip().lower()
                    if cockpit_answer == "yes" or cockpit_answer == "y":
                        display(bay, debris_in_cargo)
                        print(" What single keyboard character would you like to use?",
                              "\n" * (yrange - 4))
                        curser = input(" >>> ").strip()

                elif bay == 1:
                    display(bay, debris_in_cargo)
                    print(" You are the only one left on the ship",
                          "\n" * (yrange - 4))
                    input(" >>> ")

                elif bay == 2:
                    display(bay, debris_in_cargo)
                    print(" Running strong!",
                          "\n" * (yrange - 4))
                    input(" >>> ")

                elif bay == 3:
                    if debris_in_cargo > 0:
                        display(bay, debris_in_cargo)
                        print(" Would you like to jettison the cargo?",
                              "\n" *(yrange - 4))
                        cargo_answer = input(" >>> ").strip().lower()
                        
                        if "y" in cargo_answer:
                            debris_in_cargo = 0

                        elif "n" in cargo_answer:
                            display(bay, debris_in_cargo)
                            print(" Deposit cargo?",
                                  "\n" *(yrange - 4))
                            cargo_answer = input(" >>> ").strip().lower()

                            if "y" in cargo_answer:
                                storage += debris_in_cargo
                                debris_in_cargo = 0

                    else:
                        display(bay, debris_in_cargo)
                        print(" Running empty!",
                              "\n" * (yrange - 4))
                        input(" >>> ")
    
            elif choose_bay == b'o' or choose_bay == b'3':
                in_space = True

            elif choose_bay == b'q':
                break
    print("\n Docking")
    if storage == 1:
        print(" You have stored", storage, "chunk of debris")
    else:
        print(" You have stored", storage, "chunks of debris")
    return

run(600, 600, 168, 44)
