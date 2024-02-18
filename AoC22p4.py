#!usr/bin/env python3
#This is my solution to Advent of Code 2022's Day 4 puzzle. 

f = open("p4input.txt")
#f = open("p4sampleinput.txt")

sector_list = []
for entry in f:
    entry = entry.split('\n')[0]
    sector_list.append(entry)

counter = 0
overlap_counter = 0

for area in sector_list:
    area1, area2 = area.split(",")
    lower1, upper1 = area1.split("-")
    lower2, upper2 = area2.split("-")
    r1 = int(upper1) - int(lower1) + 1
    r2 = int(upper2) - int(lower2) + 1
    if ((r1 > r2) or (r1 == r2)) and (int(upper1) >= int(upper2)) and (int(lower1)<= int(lower2)):
        counter = counter + 1
        print(area,counter)
    elif ((r2 > r1) or (r1 == r2)) and (int(upper2) >= int(upper1)) and (int(lower2)<= int(lower1)):
        counter = counter + 1
        print(area,counter)
    if (int(lower1) in range(int(lower2), int(upper2) + 1)) or (int(upper1) in range(int(lower2), int(upper2) + 1)) or (int(lower2) in range(int(lower1), int(upper1) + 1)) or (int(upper2) in range(int(lower1), int(upper1) + 1)):
        overlap_counter = overlap_counter + 1

print(counter,len(sector_list))
print(overlap_counter)
#print(sector_list)
