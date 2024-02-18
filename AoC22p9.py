#!usr/bin/env python 3
#This program is my solution to day 9 of Advent of Code's 2022 puzzles.

f = open('p9input.txt')
#f = open('p9exampleinput.txt')
#f = open("p9exampleinputlarge.txt")
import math

moveset = []
for line in f:
    moveset.append(line.split("\n")[0].split(" "))

class knot:
    def __init__(self, position = (0,0)):
        self.position = position


def movestep(moveset):
    stepbystep = []
    for move in moveset:
        direction, step = move
        step = int(step)
        for i in range(step):
            stepbystep.append((direction, 1))
    return stepbystep

def update(knot, move):
    x, y = knot.position
    direction, steps = move
    steps = int(steps)
    if direction == "L":
        knot.position = (x-steps, y)
    if direction == "R":
        knot.position = (x+steps, y)
    if direction == "U":
        knot.position = (x, y+steps)
    if direction == "D":
        knot.position = (x, y-steps)

def tail_update(head, tail):
    history = []
    xh, yh = head.position
    xt, yt = tail.position
    if math.sqrt((xt-xh)**2 + (yt-yh)**2) <= math.sqrt(2):
        return tail.position, history
    if xh == xt:
        if yh > yt:
            tail.position = (xt, yh-1)
            for i in range(yt+1, yh):
                history.append((xt, i))
        else:
            tail.position = (xt, yh + 1)
            for i in range(yh + 1, yt):
                history.append((xt, i))
        return tail.position, history
    if yh == yt:
        if xh > xt:
            tail.position = (xh - 1, yt)
            for i in range(xt+1, xh):
                history.append((i, yt))
        else:
            tail.position = (xh+1, yt)
            for i in range(xh+1, xt):
                history.append((i, yt))
        return tail.position, history
    if abs(xh - xt) == 1:
        if xh > xt:
            xt = xt + 1
            tail.position = (xt, yt)
        else:
            xt = xt - 1
            tail.position = (xt, yt)
        if yh > yt:
            yt = yt + 1
            history.append((xt, yt))
            tail.position = (xt, yh-1)
            for i in range(yt+1, yh):
                history.append((xt, i))
        else:
            yt = yt - 1
            history.append((xt, yt))
            tail.position = (xt, yh + 1)
            for i in range(yh + 1, yt):
                history.append((xt, i))
        return tail.position, history
    if abs(yh-yt) ==1:
        if yh > yt:
            yt = yt + 1
            tail.position = (xt, yt)
        else:
            yt = yt - 1
            tail.position = (xt, yt)
        if xh > xt:
            xt = xt + 1
            history.append((xt, yt))
            tail.position = (xh - 1, yt)
            for i in range(xt+1, xh):
                history.append((i,yt))
        else:
            xt = xt - 1
            history.append((xt, yt))
            tail.position = (xh+1, yt)
            for i in range(xh+1, xt):
                history.append((i, yt))
        return tail.position, history
    while xh>xt and yh>yt:
        if math.sqrt((xh-xt)**2 + (yh - yt)**2) <= math.sqrt(2):
            return tail.position, history
        xt = xt + 1
        yt = yt + 1
        tail.position = (xt, yt) 
        history.append((xt, yt))
    if xh == xt or yh == yt:
        p, his = tail_update(head, tail)
        history = history + his
        return p, his
    while xh>xt and yh < yt:
        if math.sqrt((xh-xt)**2 + (yh - yt)**2) <= math.sqrt(2):
            return tail.position, history
        xt = xt + 1
        yt = yt - 1
        tail.position = (xt, yt) 
        history.append((xt, yt))
    if xh == xt or yh == yt:
        p, his = tail_update(head, tail)
        history = history + his
        return p, history
    while xh<xt and yh > yt:
        if math.sqrt((xh-xt)**2 + (yh - yt)**2) <= math.sqrt(2):
            return tail.position, history
        xt = xt - 1
        yt = yt + 1
        tail.position = (xt, yt) 
        history.append((xt, yt))
    if xh == xt or yh == yt:
        p, his = tail_update(head, tail)
        history = history + his
        return p, history
    while xh < xt and yh < yt:
        if math.sqrt((xh-xt)**2 + (yh - yt)**2) <= math.sqrt(2):
            return tail.position, history
        xt = xt - 1
        yt = yt - 1
        tail.position = (xt, yt) 
        history.append((xt, yt))
    if xh == xt or yh == yt:
        p, his = tail_update(head, tail)
        history = history + his
        return p, history






def unique_list(input_list):
    output_list = []
    for value in input_list:
        if value not in output_list:
            output_list.append(value)
    return output_list



head = knot()
tail = knot()


history = []
for move in moveset:
    if tail.position not in history:
        history.append(tail.position)
    update(head, move)
    pos, new = tail_update(head, tail)
    history = history + new
 #   print(head.position, tail.position)

#print(head.position, tail.position)
#print(unique_list(history), len(unique_list(history)))

new_head = knot()
new_tail = knot()

knots = []
for i in range(9):
    knots.append(knot())

def update_rope(head, knot_list):
    history = []
    pos, new = tail_update(head, knot_list[0])
    if len(knot_list) == 1:
        history = history + new
        return knot_list[0].position, history
    temp_rope = knot_list.copy()
    del(temp_rope[0])
    print(knot_list, knot_list[0].position)
    pos2, new2 = update_rope(knot_list[0], temp_rope)
    history = new2
    return knot_list[0].position, history

tail_history = []
newmoveset = movestep(moveset)
for move in newmoveset:
    print(move)
    update(new_head, move)
    pos3, temp_tail_history = update_rope(new_head, knots)
    tail_history = tail_history + temp_tail_history


print(unique_list(tail_history), len(unique_list(tail_history)))




