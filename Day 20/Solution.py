#!/bin/python3

import sys

n = int(input().strip())
ar = list(map(int, input().strip().split(' '))) 
count = 0
for i in range(n):
    for j in range(n-1):
        if(ar[j] > ar[j+1]):
            count+=1
            ar[j], ar[j+1] = ar[j+1], ar[j]
    if(count is 0):
        break
print("Array is sorted in " + str(count) + " swaps.")
print("First Element: " + str(ar[0]))
print("Last Element: " + str(ar[n-1]))
