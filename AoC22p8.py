#!usr/bin/env python 3
#This is my solution to day 8 of Advent of Code's 2022 puzzles. 

f = open("p8input.txt")
#f = open("p8exampleinput.txt")

rows = []
grid = []
#for line in f:
#    rows.append(line.split("\n")[0])

y = 0
for line in f:
    grid.append([])
    sline = line.split("\n")[0]
    for value in sline:
        grid[y].append(int(value))
    y = y +1

print(grid)

dim = len(grid[0])
visible = 4*dim-4

def find_visibleLR(grid):
    dim = len(grid[0])
    visible = 4*dim-4
    for y, element in enumerate(grid):
        currentL = int(element[0])
        currentR = int(element[dim - 1])
        if y == 0 or y == dim - 1:
            continue
        for x, tree in enumerate(element):
            if x == 0 or x == dim -1:
                continue
            if int(tree) == 9:
                visible = visible + 1
                break
            if int(element[dim -1 - x]) == 9:
                visible = visible + 1
                break
            if int(tree) > currentL:
                visible = visible + 1
                currentL = int(tree)
            if int(element[dim - 1 - x]) > currentR:
                visible = visible + 1
                currentR = int(element[dim - 1 - x])
    return visible
    
def transpose(list_matrix):
    dim = len(list_matrix[0])
    transposed_matrix = list_matrix.copy()
    for y, row in enumerate(list_matrix):
        for x, element in enumerate(row):
            if y==0 :
                transposed_matrix[x] = element + transposed_matrix[x][1:dim]
            if y == dim -1:
                transposed_matrix[x] = transposed_matrix[x][0:dim-1] + element
            elif y != 0 :
                transposed_matrix[x] = transposed_matrix[x][0:y] + element + transposed_matrix[x][y+1:dim]
    return transposed_matrix

def isvisible(position, grid, dim):
    x, y = position
    lb = x
    visionL = True
    ub = dim - x
    visionR = True
    lbu = y
    visionU = True
    ubd = dim - y
    visionD = True
    for i in range(1,lb+1):
        if grid[y][x] - grid[y][x-i] <= 0:
            visionL = False
            break
    if visionL == True:
        return True, 0
    for i in range(1, ub):
        if grid[y][x] - grid[y][x+i] <= 0:
            visionR = False
            break
    if visionR == True:
        return True, 1
    for i in range(1, lbu+1):
        if grid[y][x] - grid[y-i][x] <=0:
            visionU = False
            break
    if visionU == True:
        return True, 2
    for i in range(1, ubd):
        if grid[y][x] - grid[y+i][x] <=0:
            visionD = False
            break
    if visionD == True:
        return True, 3
    return False, None

def max_scenic_score(grid, dim):
    maxss = 0
    for y, row in enumerate(grid):
        for x, tree in enumerate(row):
            lb = x
            ub = dim - x
            lbu = y
            ubd = dim - y
            counterL = 0
            for i in range(1,lb+1):
                if grid[y][x] - grid[y][x-i] <= 0: 
                    counterL = counterL + 1
                    break
                counterL = counterL + 1
            counterR = 0
            for i in range(1, ub):
                if grid[y][x] - grid[y][x+i] <=  0:
                    counterR = counterR + 1
                    break
                counterR = counterR + 1
            counterU = 0
            for i in range(1, lbu+1):
                if grid[y][x] - grid[y-i][x] <=0:
                    counterU = counterU + 1
                    break
                counterU = counterU + 1
            counterD = 0
            for i in range(1, ubd):
                if grid[y][x] - grid[y+i][x] <=0:
                    counterD = counterD + 1
                    break
                counterD = counterD + 1
            print(counterL, counterR, counterU, counterD)
            if counterD*counterU*counterR*counterL > maxss:
                maxss = counterD*counterU*counterR*counterL
    return maxss
            

counter = 0
for y, row in enumerate(grid):
    if y==0 or y == dim -1:
        continue
    for x, tree in enumerate(row):
        if x == 0 or x == dim - 1:
            continue
        vision, direction = isvisible((x,y), grid, dim)
        if vision == True:
            counter = counter + 1

print(counter + visible)
print(max_scenic_score(grid, dim))
