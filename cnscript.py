import sys

file = open('payload.txt', 'r')
thisFile = file.readlines()
file.close()

dept = sys.argv[1]

def main(thisFile):
    newFile = open(dept, "w")
    for line in thisFile:
        newLine = line[0:1]
        if (newLine != 'p' and newLine != 'a'):
            newFile.write(line)
    
    newFile.close()

main(thisFile)