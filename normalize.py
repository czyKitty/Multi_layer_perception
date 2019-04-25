import sys
import math
import numpy as np

def normalize(dataFile,outFile):
    line = dataFile.readline().split(',')
    dataList = []
    
    for i in range(len(line)):
        dataList.append([])
    
    while(len(line)>1):
        for i in range(len(line)):
            dataList[i].append(float(line[i]))
        line = dataFile.readline().split(',')

    for i in range(len(dataList)-1):
        mean = np.mean(dataList[i])
        std = np.std(dataList[i])
        minVal = mean-2*std
        maxVal = mean+2*std
        for j in range(len(dataList[i])):
            if dataList[i][j] < minVal:
                dataList[i][j] = -1
            elif dataList[i][j] > maxVal:
                dataList[i][j] = 1
            else:
                dataList[i][j] = (dataList[i][j]-minVal)/(maxVal-minVal)

    for i in range(len(dataList[0])):
        for j in range(len(dataList)-1):
            outFile.write(str(dataList[j][i])+',')
        outFile.write(str(dataList[len(dataList)-1][i])+'\n')

def main():
    dataFileName = sys.argv[1]
    outFileName = sys.argv[2]
    
    dataFile = open(dataFileName,'r')
    outFile = open(outFileName,'w')
    
    normalize(dataFile,outFile)

    dataFile.close()
    outFile.close()
main()
