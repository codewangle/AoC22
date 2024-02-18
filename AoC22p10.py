#!usr/bin/env python3
#This my solution to day 10 of Advent of Code's 2022 puzzles. 

f = open("p10input.txt")
#f = open("p10exampleinput.txt")

commands = []
X = 1
cycle = 0
signalsum = 0
screen = "" 
for instruction in f:
    command = instruction.split("\n")[0]
    try:
        command = command.split(" ")
        X = X + int(command[1])
        cycle = cycle + 1
        if (cycle-1)%40 in range(X-int(command[1])-1, X-int(command[1])+2):
            screen = screen + "#"
        else:
            screen = screen + "."
        if cycle in range(20,240,40):
            signalsum = signalsum + (X-int(command[1]))*cycle
            print(signalsum, X - int(command[1]), cycle)
        cycle = cycle + 1
        if (cycle-1)%40 in range(X-int(command[1])-1, X-int(command[1])+2):
            screen = screen + "#"
        else:
            screen = screen + "."
        if cycle in range(20, 240, 40):
            signalsum = signalsum + (X - int(command[1]))*cycle
            print(signalsum, X - int(command[1]), cycle)
        command.append(X)
        command.append(cycle)
        commands.append(command)
    except:
        cycle = cycle + 1
        if (cycle-1)%40 in range(X-1, X+2):
            screen = screen + "#"
        else:
            screen = screen + "."
        if cycle in range(20, 240, 40):
            signalsum = signalsum + X*cycle
            print(signalsum, X, cycle)
        commands.append([command[0], "p", X, cycle])
crt = ""
for i, pixel in enumerate(screen):
    if i%40 == 0 and i != 0:
        print(i, pixel)
        crt = crt  + "\n" + pixel
    else:
        print(i, pixel)
        crt = crt + pixel


print(commands)


print(signalsum)
print(crt)

print(len(screen))
