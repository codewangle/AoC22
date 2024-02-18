#!usr/bin/env python 3
#This program is my solution to Advent of Code 2022's day 5 puzzle. 

import re

f = open("p5input.txt")
#f = open("p5sampleinput.txt")

data_list = []

def move(quantity, stack1, stack2 ):
    for i in range(0, quantity):
        stack2.append(stack1[-1])
        stack1.pop()

def move2(quantity, stack1, stack2):
    stack2 = stack2 + stack1[-quantity:]
    stack1 = stack1[0:-quantity]
    return stack1, stack2


for i in f:
    i = i.split("\n")[0]
    data_list.append(i)

stack_list = []
move_list = []
for data in data_list:
    index = 0
    for char in data:
        if char == "[":
            stack_list.append([data[index + 1], int(index/4)])
        index = index + 1
    try:
        quantity, fr, to, = re.findall("[0-9]*[0-9]", data)
        move_list.append([int(quantity), int(fr)-1, int(to)-1])
    except:
        continue

stack_number = 0
bin_list = []
while stack_number < 9:
    new = True
    for stack in stack_list:
        if stack_number == stack[1] and new == True:
            bin_list.append([stack[0]])
            new = False
        elif stack_number == stack[1]:
            bin_list[stack_number].insert(0, stack[0])
    stack_number = stack_number + 1
    
#del move_list[0]
print(move_list[0])#, move_list[20])
for Move in move_list:
    #bin_list[Move[1]], bin_list[Move[2]] = move2(Move[0], bin_list[Move[1]], bin_list[Move[2]])
    move(Move[0], bin_list[Move[1]], bin_list[Move[2]])

#print(stack_list)
print(bin_list)

            





