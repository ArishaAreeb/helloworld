wordCount = {}  # empty dictionary to store the word counts
inFile = open('aesop','r')
for line in inFile:
    line = line.lower()  # make everything lowercase
    # replace punctuation with spaces
    for char in '.,!?':
        line = line.replace(char,'')
inFile.close()
# print out the top 10 words