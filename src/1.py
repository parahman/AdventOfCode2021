import sys
import numpy as np

f = open(".//data//1.txt","r")
lines = np.array(f.readlines(),dtype='i')

def assignment_1_1(lines):
    prevValue = sys.maxsize
    count = 0
    for x in lines:
        x_int = int(x)
        if(prevValue < x_int):
            count += 1
        prevValue = x_int
    return count

def assignment_1_2(lines):
    i=0
    window=3
    prevValue = sys.maxsize
    count = 0
    while i <= len(lines)-window:
        # print (str(lines[i:i+window]) + " sum: " + str(sum(lines[i:i+window])))
        if(prevValue < sum(lines[i:i+window])):
            count += 1
        prevValue = sum(lines[i:i+window])
        i += 1
    return count

count = assignment_1_1(lines)
print('assignment_1_1: ' + str(count))
count = assignment_1_2(lines)
print('assignment_1_2: ' + str(count))
f.close()
