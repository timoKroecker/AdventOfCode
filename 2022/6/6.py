import os

#reading text file
with open(os.path.dirname(__file__) + '/data.txt') as file:
    lines = file.readlines()

line = lines[0]

#return True if all characters in string are unique
def all_unique(string):
    for i in range(len(string)):
        for j in range(len(string)):
            if(i < j and string[i] == string[j]):
                return False
    return True

#print the position of the first occurance
#of a string with given length and all unique characters
def find_unique_section(length, headline):
    for i in range(len(line) - length + 1):
        if(all_unique(line[i:i + length])):
            print(headline)
            print(i + length)
            print("")
            break

#find first badge
find_unique_section(4, "6.1:")
#find first message
find_unique_section(14, "6.2:")