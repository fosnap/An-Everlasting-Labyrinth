la = [[" "," ","m"," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "]]
lb = [[" "," "," "," ","m"],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "]]
lc = [[" "," "," ","I"," "],[" ","I"," ","I"," "],[" ","I"," ","I"," "],[" ","I"," ","I"," "],["m","I"," "," "," "]]
ld = [[" "," "," "," "," "," "],[" ","I","I","I","I"," "],[" ","I"," ","m","I"," "],[" ","I"," ","I","I"," "],[" ","I"," "," "," "," "]]

a = la
c = 1
x = 2
y = 2

print("use w,a,s,d, to move")
print("m is your goal")
print("the last level is a free roam \n")
print("l o a d i n g")
print("\n",a[0],"\n",a[1],"\n",a[2],"\n",a[3],"\n",a[4])
a[y][x] = "n"
print("\n",a[0],"\n",a[1],"\n",a[2],"\n",a[3],"\n",a[4],"\n","level 1")

while True:
    a[y][x] = " "
    b = input(": ");

    if "w" in b:
        y -= 1
        if y <= -1:
            y = 0
        elif x > len(a[y]) - 1:
            y += 1
            d += 1
        elif 0 <= x <= len(a[y]) - 1:
            if a[y][x] not in [" ", "m", "n"]:
                y += 1

    if "s" in b:
        y += 1
        if y >= len(a):
            y = len(a) - 1
        elif x > len(a[y]) - 1 :
            y -= 1
            d += 1
        elif 0 <= x <= len(a[y]) - 1:
            if a[y][x] not in [" ", "m", "n"]:
                y -= 1

    if "a" in b:
        x -= 1
        if x <= -1:
            x = 0
        elif a[y][x] not in [" ", "m", "n"]:
            x += 1

    if "d" in b:
        x += 1
        if x >= len(a[y]):
            x = len(a[y]) - 1
        elif a[y][x] not in [" ", "m", "n"]:
            x -= 1

    if a[y][x] == "m":
        c += 1
        if c == 1:
            a = la
        elif c == 2:
            a = lb
        elif c == 3:
            a = lc
        elif c == 4:
            a = ld
        else:
            a = la
            a[0][2] = " "
            a[2][2] = "o"
    a[y][x] = "n"
    print("\n",a[0],"\n",a[1],"\n",a[2],"\n",a[3],"\n",a[4],"\n","level ",c)
