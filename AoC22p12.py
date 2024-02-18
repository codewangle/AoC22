#!usr/bin/env python 3
#This program is my solution to day 12 of Advent of Code's 2022 puzzles.

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

class connected_set:
    def __init__(self, point, height = 0, border = []):
        self.height = height
        self.border = border
        self.point = point


class_grid = []
for y, row in enumerate(grid):
    for x, value in enumerate(grid):
        connected = []
        if y + 1 < len(grid):
            class_grid.append(connected_set((x,y), value ))
            if grid[y + 1][x] - grid[y][x] > 0 and (x,y):
                connected.append((x,y))
        if yo - 1 >= 0: 
            if (grid[yo-1][xo] - grid[yo][xo] <= 1 or grid[yo][xo] - grid[yo - 1][xo] > 0) and (xo, yo - 1) not in history:
        if xo + 1 < len(grid[0]):
            if (grid[yo][xo + 1] - grid[yo][xo] <=1 or grid[yo][xo] - grid[yo][xo + 1] > 0) and (xo + 1, yo) not in history:
        if xo - 1 >= 0:
            if (grid[yo][xo - 1] - grid[yo][xo] <=1 or grid[yo][xo] - grid[yo][xo - 1] > 0) and (xo - 1, yo) not in history:
    




def find_route(grid, start, end, routes):
    if len(routes) == 0:
        routes.append([start])
    for route in routes:
        if route[-1] == end:
            return route
    temp_routes = []
    for route in routes:
        print(route)
        print(find_next(grid, route[-1], end, route))
        temp_routes = temp_routes + find_next(grid, route[-1], end, route)
    final = find_route(grid, start, end, temp_routes)
    return final

def find_next(grid, start, end, history):
    route = history
    xo, yo = start
    xf, yf = end
    routes = []
    if yo + 1 < len(grid):
        if (grid[yo+1][xo] - grid[yo][xo] <= 1 or grid[yo][xo] - grid[yo + 1][xo] > 0) and (xo, yo + 1) not in history:
            droute = route.copy()
            droute.append((xo, yo + 1))
            routes.append(droute)
    if yo - 1 >= 0: 
        if (grid[yo-1][xo] - grid[yo][xo] <= 1 or grid[yo][xo] - grid[yo - 1][xo] > 0) and (xo, yo - 1) not in history:
            uroute = route.copy()
            uroute.append((xo, yo - 1))
            routes.append(uroute)
    if xo + 1 < len(grid[0]):
        if (grid[yo][xo + 1] - grid[yo][xo] <=1 or grid[yo][xo] - grid[yo][xo + 1] > 0) and (xo + 1, yo) not in history:
            rroute = route.copy()
            rroute.append((xo + 1, yo))
            routes.append(rroute)
    if xo - 1 >= 0:
        if (grid[yo][xo - 1] - grid[yo][xo] <=1 or grid[yo][xo] - grid[yo][xo - 1] > 0) and (xo - 1, yo) not in history:
            lroute = route.copy()
            lroute.append((xo - 1, yo))
            routes.append(lroute)
    return routes
    


print(grid, end, start, len(grid[0]))
m = find_route(grid, start, (8, 17), [])
print(len(m) - 1, m)
n = find_route(grid, (8, 17), (12,14), [m])
print(n, len(n)-1)
o = find_route(grid, (12,14), (20,12), [n])
print(o, len(o)-1)
p = find_route(grid, (20,12), (30, 11), [o])
print(p, len(p)-1)
