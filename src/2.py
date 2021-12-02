import sys
import numpy as np
import os

def assignment_2_1(lines):
    cmdDict = dict({'forward':0,'down':0,'up':0});
    for x in lines:
        command=x.split()
        cmdDict[command[0]] = cmdDict[command[0]] + int(command[1])
    return cmdDict['forward'] * (cmdDict['down'] - cmdDict['up'])

def assignment_2_2(lines):
    cmdDict = dict({'forward':0,'aim':0,'depth':0});
    for x in lines:
        command=x.split()
        if command[0] == 'forward':
            cmdDict['forward'] += int(command[1])
            cmdDict['depth'] = cmdDict['depth'] + int(command[1]) * cmdDict['aim']
        if command[0] == 'up':
            cmdDict['aim'] -= int(command[1])
        if command[0] == 'down':
            cmdDict['aim'] += int(command[1])
    return cmdDict['forward'] * cmdDict['depth']

def run(filename):
    f = open(filename,"r")
    lines = np.array(f.readlines())
    return [assignment_2_1(lines), assignment_2_2(lines)]
    f.close()    
    
day = os.path.basename(__file__).split(".")[0]
filename = ".//data//{fname}.txt".format(fname = day)
testfilename = ".//data//{fname}_test.txt".format(fname = day)

result = run(testfilename)
assert result[0] == 150    
assert result[1]== 900

result = run(filename)
print('assignment_2_1: ' + str(result[0]))
print('assignment_2_2: ' + str(result[1]))
