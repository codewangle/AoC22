#!usr/bin/env python 3
#This is my second attempt at problem 12 of Advent of Code's 2022 daily puzzles. This puzzle involves finding the fastest route from point A to 
#point B in a graph. 

f = open("p12input.txt")
#f = open("p12exampleinput.txt")

grid = []
for y, line in enumerate(f):
    grid.append([])
    for x, letter in enumerate(line.strip()):
        if ord(letter) == 83:
            start = (x,y)
            grid[y].append(ord("a"))
            continue
        if ord(letter) == 69:
            end = (x,y)
            grid[y].append(ord("z"))
            continue
        grid[y].append(ord(letter))

class node:
    def __init__(self, coord, up_connected, down_connected):
        self.coord = coord
        self.up_connected = up_connected
        self.down_connected = down_connected



#Here I'm trying to create the graph for the map we are given. I've created a class for a node type object and I want this 
#object to have an attribute that points to every node it's connected. However, we must note that nodes are connected differently
#if the user is trying to climb vs trying to descend. A user can only move up one unit but can move down any number of units. Thus
#we have node.up_connected, which should be a list of coordinates of all nodes that are one unit higher or of the same height, and we 
#have node.down_connected, which should be a list of coordinates of all nodes that are lower in height. 

def check_connections(coord, grid):
    x, y = coord
    connected = []
    dconnected = []
    if x + 1 < len(grid[0]) and (grid[y][x] - grid[y][x+1] == -1 or grid[y][x] - grid[y][x+1] == 0):
        connected.append((x+1, y))
    elif x + 1 < len(grid[0]) and grid[y][x] - grid[y][x+1] >= 1:
        dconnected.append((x+1,y))
    if x - 1 >= 0 and (grid[y][x] - grid[y][x-1] == -1 or grid[y][x] - grid[y][x-1] == 0):
        connected.append((x-1, y))
    elif x -1 >= 0 and grid[y][x] - grid[y][x-1] >= 1:
        dconnected.append((x-1,y))
    if y + 1 < len(grid) and (grid[y][x] - grid[y+1][x] == -1 or grid[y][x] - grid[y+1][x] == 0):
        connected.append((x, y+1))
    elif y+1 < len(grid) and grid[y][x] - grid[y+1][x] >= 1:
        dconnected.append((x, y+1))
    if y - 1 >= 0 and (grid[y][x] - grid[y-1][x] == -1 or grid[y][x] - grid[y-1][x] == 0):
        connected.append((x, y-1))
    elif y - 1 >= 0 and grid[y][x] - grid[y-1][x] >= 1:
        dconnected.append((x, y-1))
    return connected, dconnected

graph = []

for y, row in enumerate(grid):
    grow = []
    for x, point in enumerate(row):
        uconnected, dconnected = check_connections((x,y), grid)
        grow.append(node((x,y), uconnected, dconnected))
    graph.append(grow)

print(start, end)

def find_route(graph, start, end, history, count):
    if count >= 500:
        return count
    next_step = []
    #print("This is the start list")
    #print(start)
    for coord in start:
        if coord in history:
            continue
        x, y = coord
       # print("This is the coord")
       # print(coord)
       # print(graph[y][x].up_connected, graph[y][x].down_connected)
        if end in graph[y][x].up_connected or end in graph[y][x].down_connected: 
            return count + 1
        else:
            newpoints = set(graph[y][x].up_connected) - set(graph[y][x].down_connected)
            newpoints = list(newpoints) + graph[y][x].down_connected 
            nnext = set(newpoints) - set(next_step)
            next_step = list(nnext) + next_step
   # print("This is next step")
    #print(next_step)
    count = count + 1
    #print(count)
    history = history + start
    return find_route(graph, next_step, end, history, count )

number_of_steps = find_route(graph, [start], end, [], 0 )
print(number_of_steps)

#now we need to find the fastest route as a function of starting point. 

scenic = 400
for y, row in enumerate(grid):
    for x, point in enumerate(row):
        if point == 97:
            n = find_route(graph, [(x,y)], end, [], 0)
            if n < scenic:
                scenic = n
        print(scenic)

print(scenic)
        



