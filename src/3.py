import sys
import numpy as np
import os
import math

def binToStr(arr):
    return int(''.join(str(s) for s in arr),2)

def roundOldFashion(val):
    x = 0
    if (float(val) % 1) >= 0.5:
        x = math.ceil(val)
    else:
        x = round(val)
    return x

def findCommon(npArr, lookingFor, index, findMostCommon):
    if len(npArr) == 1:
        return npArr[0]
    filteredArray = np.array([item for item in npArr if item[index] == lookingFor])
    sum = filteredArray.sum(axis=0)
    length = len(filteredArray)
    resArray=[roundOldFashion(float(s)/len(filteredArray)) for s in sum]
    lookingFor = resArray[min(index+1,len(resArray)-1)]
    if findMostCommon == False:
        lookingFor = 1 if lookingFor == 0 else 0
    resArray = findCommon(filteredArray,lookingFor,index+1, findMostCommon)
    return resArray

def assignment_1(lines):
    length = len(lines)
    sum = lines.sum(axis=0)
    resArray=[str(roundOldFashion(float(s)/length)) for s in sum]
    res = int(''.join(resArray),2)
    resInv = int(''.join(['1' if i == '0' else '0' for i in resArray]),2)
    return res*resInv

def assignment_2(lines):
    return binToStr(findCommon(lines, 1, 0, True)) * binToStr(findCommon(lines, 0, 0, False))

def run(filename):
    f = open(filename,"r")
    lines = np.array([[int(char) for char in line.strip()] for line in f.readlines()])
    f.close()
    return [assignment_1(lines), assignment_2(lines)]
    
day = os.path.basename(__file__).split(".")[0]
filename = ".//data//{fname}.txt".format(fname = day)
testfilename = ".//data//{fname}_test.txt".format(fname = day)

result = run(testfilename)
assert result[0] == 198
assert result[1] == 230

result = run(filename)
print('assignment_1: ' + str(result[0]))
print('assignment_2: ' + str(result[1]))
