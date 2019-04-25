import sys

def preprocess(dataFile,outFile):
    line = dataFile.readline()
    while (len(line)>0):
        if (len(line)!=1 and line[0]!='@'):
            s_line = line.split(',')
            if(s_line[-1][:-1] == 'disease'):
                outFile.write(','.join(s_line[:-1])+',0\n')
            else:
                outFile.write(','.join(s_line[:-1])+',1\n')
        line = dataFile.readline()

def main():
    dataFileName = sys.argv[1]
    outFileName = sys.argv[2]
    
    dataFile = open(dataFileName,'r')
    outFile = open(outFileName,'w')

    preprocess(dataFile,outFile)

    dataFile.close()
    outFile.close()
main()