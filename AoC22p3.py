#!usr/bin/env python 3
#This program is my solution to Advent of Code 2022's Day 3 problem. 

from primes import primes as primes
import math
import sympy

#f = open("p3input.txt")
f = open("p3sampleinput.txt")

Primes = primes()
priority = 0
prfactorizations = []
for string in f: 
    string = string[:-1]
    length = len(string)
    left = string[0:int(length/2)]
    right = string[int(length/2):int(length)]
    c = 1 
    d = 1 
    for j in left:
        if math.gcd(c, Primes[ord(j)-65]) == 1:
            c = c*Primes[ord(j)-65]
    for k in right:
        if math.gcd(d, Primes[ord(k)-65]) == 1:
            d = d*Primes[ord(k)-65]
    g = math.gcd(c,d)
    symb = chr(65 + Primes.index(g))
    print(symb)
    if symb.isupper() == True:
        priority = priority + ord(symb)-38
    else:
        priority = priority + ord(symb)-96
    pfstring = 1
    for s in string:
        if math.gcd(pfstring, Primes[ord(s)-65]) == 1:
            pfstring = pfstring*Primes[ord(s)-65]
    prfactorizations.append(pfstring)

counter = 1
priority2 = 0
d = 1
for i in prfactorizations:
    if counter%3 == 0:
        d = math.gcd(d,i)
        symb2 = chr(65+Primes.index(d))
        print(symb2)
        if symb2.isupper() == True:
            priority2 = priority2 + ord(symb2)-38
        else:
            priority2 = priority2 + ord(symb2)-96   
        d = 1
        counter = counter + 1
        continue
    if math.gcd(d, i) == 1:
        d = d*i
    else:
        d = math.gcd(d, i)
    counter = counter + 1

print(priority)
print(priority2)
