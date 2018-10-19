import msvcrt

# Levels
floor = [
  [
    # Floor 0 (Outside)
    #x0  x1  x2  x3  x4
    ["o"," ","D"," ","o"],#y0
    [" "," "," "," "," "],#y1
    [" "," "," "," "," "]#y2
  ],
  [
    # Floor 1 (Lobby)
    #x0  x1  x2  x3  x4  x5
    [" ","n","r"," "," ","E"],#y0
    ["r","r","r"," "," "],#y1
    [" "," "," "," "," "],#y2
    [" "," "," "," "," "],#y3
    [" "," ","D"," "," "]#y4
  ],
  [
    # Floor 2 (to be determined)
    #x0  x1  x2  x3  x4  x5
    [" "," "," "," "," ","E"],#y0
    [" "," "," "," "," "],#y1
    [" "," "," "," "," "],#y2
    [" "," "," "," "," "],#y3
    [" "," "," "," "," "]#y4
  ],
  [
    # Floor 3 (to be determined)
    #x0  x1  x2  x3  x4  x5
    [" "," "," "," "," ","E"],#y0
    [" "," "," "," "," "],#y1
    [" "," "," "," "," "],#y2
    [" "," "," "," "," "],#y3
    [" "," "," "," "," "]#y4
  ],
  [
    # Roof (layout to be determined)
    #x0  x1  x2  x3  x4  x5
    [" "," "," "," "," ","E"],#y0
    [" "," "," "," "," "],#y1
    [" "," "," "," "," "],#y2
    [" "," "," "," "," "],#y3
    [" "," "," "," "," "]#y4
  ]
]

# Centering character
floor_number = 0# Outside
y = 2# Autological but inversed
x = 2# Autological

# Setup for user
print("\n Use w, a, s, and d on you keyboard to move.\n")# Instruction
print(" E is an elevator.\n\n D is a door.\n\n You are N."
      "\n\n Everything else is decoration.\n")# Instruction
print(" l o a d i n g\n\n")# Filler line for amusement
floor[floor_number][y][x] = "n"# Character
for y_iter in range(len(floor[floor_number])):
    print(floor[floor_number][y_iter])
print(" Outside\n\n")# Setting the stage    

# Loop for full walkthrough of the building
while True:
    # Setting current position empty before values are changed
    floor[floor_number][y][x] = " "
    # Input from user as to direction of movement
    # direction = input(">>> ");
    direction = msvcrt.getch()
    # Checking for a "forward" request
    if (direction == b'w'):
        # Reduce y to move "n" toward top of screen
        y -= 1
        # Check for edge
        if y <= -1:
            # Correct error if over edge
            y = 0
        # Edge detection of uneven areas of levels
        elif x > len(floor[floor_number][y]) - 1:
            # Position fix
            y += 1
        # Edge detection for avoidance of a traceback index error
        elif 0 <= x <= len(floor[floor_number][y]) - 1:
            # Checking for walkable areas
            if floor[floor_number][y][x] not in [" ", "E", "n", "D"]:
                # Collision correction
                y += 1

    # Checking for a "backward" request
    if (direction == b's'):
        
        y += 1
        if y >= len(floor[floor_number]):
            y = len(floor[floor_number]) - 1
        elif x > len(floor[floor_number][y]) - 1 :
            y -= 1
        elif 0 <= x <= len(floor[floor_number][y]) - 1:
            if floor[floor_number][y][x] not in [" ", "E", "n", "D"]:
                y -= 1

    if (direction == b'a'):
        x -= 1
        if x <= -1:
            x = 0
        elif floor[floor_number][y][x] not in [" ", "E", "n", "D"]:
            x += 1

    if (direction == b'd'):
        x += 1
        if x >= len(floor[floor_number][y]):
            x = len(floor[floor_number][y]) - 1
        elif floor[floor_number][y][x] not in [" ", "E", "n", "D"]:
            x -= 1

    if (direction == b'q'):
        break

    if floor[floor_number][y][x] == "E":
        if floor_number == 4:
            floor_number = 1
        else:
            floor_number += 1
        print("elevator")
    
    if floor[floor_number][y][x] == "D":
        if floor_number == 0:
            floor_number = 1
            y = 3
            x = 2
        elif floor_number == 1:
            floor_number = 0
            y = 1
            x = 2

    floor[floor_number][y][x] = "n"

    if (direction == b'e'):
        if floor[1][2][1] == "n":
            print("Your office is on the second floor.")
        if floor[2][4][0] == "n":
            print("here it is")
    
    floor[0][0][2] = "D"
    floor[1][4][2] = "D"
    floor[1][0][5] = "E"
    floor[2][0][5] = "E"
    floor[3][0][5] = "E"
    floor[4][0][5] = "E"

    for y_iter in range(len(floor[floor_number])):
        print(floor[floor_number][y_iter])

    if floor_number == 0:
        print(" Outside\n\n")
    else:
        print(" Floor ",floor_number,"\n\n")
