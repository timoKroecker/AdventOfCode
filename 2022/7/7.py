import os
import numpy as np

#---------------------------------------------------------------
#Classes

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.dirs = []
        self.files = []
        self.parent = parent

    def add_dir(self, dir):
        self.dirs.append(dir)

    def add_file(self, file):
        self.files.append(file)

    def get_name(self):
        return self.name

    def get_size(self):
        size = 0
        for dir in self.dirs:
            size += dir.get_size()
        for file in self.files:
            size += file.get_size()
        return size

    def get_dir_sizes(self):
        array = np.array([], int)
        for dir in self.dirs:
            array = np.concatenate((array, dir.get_dir_sizes()))
        array = np.append(array, self.get_size())
        return array

    def get_parent(self):
        return self.parent

    def get_dir(self, name):
        for dir in self.dirs:
            if(dir.get_name() == name):
                return dir
        return None

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

#---------------------------------------------------------------
#Functions

def is_int(string):
    try:
        int(string)
        return True
    except:
        return False

def get_directory_from_data():
    #reading text file
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()

    root = Directory("/")
    current_directory = root

    for line in lines:
        line_elements = line.replace("\n", "").split(" ")
        #change directory
        if(line_elements[0] == "$" and line_elements[1] == "cd"):
                if(line_elements[2] == ".."):
                    current_directory = current_directory.get_parent()
                elif(line_elements[2] != "/"):
                    directory = current_directory.get_dir(line_elements[2])
                    current_directory = directory
        #add file
        elif(is_int(line_elements[0])):
            current_directory.add_file(File(line_elements[1], int(line_elements[0])))
        #add directory
        elif(line_elements[0] == "dir"):
            directory = Directory(line_elements[1], parent=current_directory)
            current_directory.add_dir(directory)
    return root

#--------------------------------------------------
#Main

root = get_directory_from_data()
dir_sizes = np.sort(root.get_dir_sizes())

print("7.1:")
print(sum(elem for elem in dir_sizes if elem <= 100000))
print("")

missing_space = 30000000 - (70000000 - root.get_size())
for element in dir_sizes:
    if(element >= missing_space):
        print("7.2:")
        print(element)
        break