#!usr/bin/env python 3
#This is my solution to day 14 of Advent of Code's 2022 daily puzzles. 

f = open("p14input.txt")
#f = open("p14sampleinput.txt")

#converting input to a list of lists. Each list in the list contains a line of the input 
#split into tuples that tell you where the rocks are. 
instructions = []
for line in f:
    steps = line.split("->")
    line_instructions = []
    for step in steps:
        coords = step.strip().split(",")
        line_instructions.append((int(coords[0]), int(coords[1])))
    instructions.append(line_instructions)

#Finding bounds of the grid kinda
grid = {}
y_max = 0
x_max = 0
x_min = instructions[0][0][0]
y_min = instructions[0][0][1]
for line in instructions:
    for step in line:
        if step[0] > x_max:
            x_max = step[0]
        if step[0]< x_min:
            x_min = step[0]
        if step[1] > y_max:
            y_max = step[1]
        if step[1] < y_min:
            y_min = step[1]

#Hard coded the bounds of the grid because I lazy and don't know how 
#to estimate bounds for part 2 :C
x_min = x_min -1
y_max = y_max + 3
x_max = x_max + 200

#Making an empty dictionary grid. Each column is given a dictionary labeled with it's x coordinate
#and each column dictionary has dictionaries labeled with y coordinates that contain either
#a True or False value (True if no rock amd no sand and False if rock or sand).
#So grid[0] = {0: True, 1: True, 2: True...}
def make_grid(x_min, x_max, y_min, y_max):
    grid = {}
    for x in range(x_min, x_max+1):
        grid[x] = {0: True}
        for y in range(y_min, y_max+1):
            grid[x][y] = True
    return grid

grid = make_grid(0, x_max, 0, y_max)

#Filling the grid with rocks
for line in instructions:
    for j, step in enumerate(line):
       # print(step)
        x, y = step
        if j == 0:
            curr = (x,y)
            grid[x][y] = False
            continue
        if curr[0] == x:
            if y > curr[1]:
                for i in range(0, y - curr[1]):
                    grid[x][curr[1]+i+1] = False
            if y < curr[1]:
                for i in range(0, curr[1] - y):
                    grid[x][curr[1] - i - 1] = False
            curr = (x, y)
            continue
        if curr[1] == y:
            if x > curr[0]:
                for i in range(0, x- curr[0]):
                    grid[curr[0]+i+1][y] = False
            if x < curr[0]:
                for i in range(0, curr[0] - x):
                    grid[curr[0]-i-1][y] = False
            curr = (x, y)
            continue
        curr = (x, y)

#Function to visualize the grid full of rocks. Also tells you how many things in the grid
#are either rock or sand. The grid is just full of rocks right now so keep tally of the number 
#of rocks now will let us know how much sand is in the grid when it comes to rest. 
def print_grid(grid):
    lines = []
    count = 0
    for index in range(len(grid[0].keys())):
        lines.append([""])
    for x in grid:
        for k, y in enumerate(grid[x]):
            if grid[x][y] and x >= x_min-30:
                lines[k][0] = lines[k][0] + "."
            elif not grid[x][y]:
                count = count + 1
                lines[k][0] = lines[k][0] + "#"
    for line in lines:
        print(line[0])
    print(count)
    return count

count_ngrid = print_grid(grid)

########
#This was the code I had before to solve this problem.
#It's very bad and was recursive before. Doesn't quite work
#when you need to recurse 27000 times. 
#bad code :C
####
"""
def gen_sand(start, grid, floor, counter = 0):
    x, y = start
    print(x,y, counter)
    print(grid[500][0])
    if not grid[500][0]:
        return False, counter
    #for k, coord in enumerate(grid):
    #    if coord[0] == x and coord[1] >= y:
    #        break
    #    else:
    #        if k == len(grid) - 1:
    #            return False
    if y != None and y == floor:
        grid[x][y-1] = False
        counter = counter + 1
        return gen_sand((500, 0), grid, floor, counter)
    if not grid[x][y]:
        #print('first if')
        if not grid[x-1][y]:
            #print("second if")
            if not grid[x+1][y]:
                grid[x][y-1] = False
                counter = counter + 1
                return gen_sand((500, 0), grid, floor, counter)
            else:
                return gen_sand((x+1, y), grid, floor, counter)
        else:
            return gen_sand((x-1,y), grid, floor, counter)
       
    else: 
        i = 0
 #       print(i, (x, y))
       # while ((x, y + i) not in grid and not y != floor) or (not ((x, y + i) not in grid) and y != floor):
        #    i = i + 1
        for j in grid[x]:
            #print(j)
            if floor != None and j==floor:
                return gen_sand((x,j), grid, floor, counter)
            if not grid[x][j]:
                if j >=y:
                    return gen_sand((x, j), grid, floor, counter)
        #counter = counter + 1
        return False, counter
        #return gen_sand((x, y + i), grid, floor)
"""

#Better way of doing this problem is in a loop. I changed my approach to make a dictionary grid
#where each point is either True or False. True if no rock and no sand and False if rock or sand
#Each loop it checks if it's at the floor, then if the left is clear (if clear start over), then if the right is 
#clear (if clear start over), and then places sand in floor, left, and right aren't clear  
def clear_left(current, grid, floor):
    x, y = current
    #print(x,y,"clear")
    if not grid[x-1][y]:
        return x, y, False
    else:
        return x-1, y, True
def clear_right(current, grid, floor):
    x, y = current
    if not grid[x+1][y]:
        return x, y, False
    else:
        return x+1, y, True

def gen_sand_nr(source, grid, floor, counter = 0):
    x, y = source
    while True:
        #print(x,y)
        if not grid[source[0]][source[1]]:
            break
        for j in grid[x]:
            if j < y:
                continue
            y = j
            if floor != None and j == floor:
                #print(x,y,"floor")
                grid[x][j-1] = False
                x = 500
                y = 0
                counter = counter + 1
                break
            if not grid[x][j]:
                #print(x, y, "clearing")
                new_x, new_y, clear_L = clear_left((x,j), grid, floor)
                if clear_L:
                    x = new_x
                    y = new_y
                    break
                new_x, new_y, clear_R = clear_right((x, j), grid, floor)
                if clear_R:
                    x = new_x
                    y = new_y
                    break
                #print(x,y, "cleared")
                grid[x][y-1] = False
                x = 500
                y = 0
                counter = counter + 1
                break
    return counter

cgrid = grid.copy()
#boo, count = gen_sand((500,0), cgrid, 11)

count = gen_sand_nr((500, 0), cgrid, y_max-1)
#print(cgrid)
#print(count)

count_fgrid = print_grid(cgrid)
print(count_fgrid - count_ngrid)
#part 2 I wrote this a while ago and this was where I was 
#gonna write stuff to do part 2 but now I've just made this code handle both cases
#Dead unfinished code lay below 

"""
y_max = 0
for step in cgrid:
    if step[1] > y_max:
        y_max = step[1]

floor = y_max + 2

while gen_sand((500, 0), grid, floor):
    counter = counter + 1
    print(grid)

"""



