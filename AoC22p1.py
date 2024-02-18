#!usr/bin/env python 3
#This is my solution to the first Advent of Code 2022 problem. This problem asks participants to 
#find, from a list of lists, the list with the greatest sum of elements where the elements are in 
#the set of real numbers. 


#tinven = []
#einven = []
#c = 0
#while True:
#    if c == 5:
#        break
#    if einven == []:
#        i = input("Input calorie values of your inventory. Submit a null value when complete: ")
#        if i == '':
#            tinven.append(einven)
#            c = c + 1
#            einven = []
#            continue
#        else:
#            i = float(i)
#            einven.append(i)
#    i = input(": ")
#    if i == '':
#        tinven.append(einven)
#        c = c + 1
#        einven = []
#    else: 
#        i = float(i)
#        einven.append(i)
#

f = open("p1input.txt")
l = []
tinven = []
for i in f:
    if i == "\n":
        tinven.append(l)
        l = []
    else:
        i = int(i[:-1])
        l.append(i)

tinven.append(l)
tally = [0,0]
sums = []
for i in tinven:
    isum = 0
    for j in i:
        isum = isum + j
    if isum > tally[0]:
        tally = isum, tinven.index(i) + 1
    sums.append(isum)

print("Elf number " + str(tally[1]) + " has the most calories. And they are carrying " + str(tally[0]) + " calories" )
total_calories = tally[0]
elfnumber = tally[1]

sums.pop(tally[1]-1)
Sums = [tally[0]]
for i in range(0,2):
    s = max(sums)
    Sums.append(s)
    sums.pop(sums.index(s))

print(Sums[0]+Sums[1] + Sums[2], Sums)





