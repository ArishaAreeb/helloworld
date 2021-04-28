inFile  = open('scores','r')
outFile = open('score2','w')

for line in inFile:
    average = 0
    sums = 0
    array = line.split()
    outFile.write(array[0]+' ')
    numGrades = len(array[1:])

    for num in array[1:]:
        sums = sums + int(num)
    average =  int(sums / numGrades)
    outFile.write(str(average)+'\n')
    print(array[0]+' '+str(average))




