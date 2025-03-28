import random

sizeMin = 1
sizeMax = 10
coloursList = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

'''Object class is a bag of marbles. Each marble has 2 values, size and colour.
The bag object simply contains a list of marble objects.'''

class Marble():
    def __init__(self, size, colour):
        self.size = size     # integer
        self.colour = colour # string

    def __getitem__(self, val):
        return val

    def __str__(self):
        return str(self.colour) + ", " + str(self.size)

    def __len__(self):
        return len(self.colour)
    
    def __add__(self, num):
        self.size += num
        return self.size
    
    def __eq__(self, other):
        return self.colour == other.colour and self.size == other.size
    
    def __lt__(self, other):
        return self.size < other.size
    
    

class Bag():
    def __init__(self):
        self.marblesList = []

    def __setitem__(self, index, key):
        obj = self.marblesList[index]
        if str(key) == key:
            obj.data[1] = key
            return obj
        obj.data[0] = key
        return obj

    def generate_bag(self, amount):
        '''The colour and size is randomized for each marble.
        In this case, the colour is any of the 7 in the rainbow
        (red, yellow, orange, green, blue, indigo, violet)
        and the size is a number between 1 and 10.'''

        for i in range (0, amount):

            tempSize = random.randint(sizeMin, sizeMax)
            tempCol = coloursList[random.randint(0, len(coloursList)-1)]
            newMarble = Marble(tempSize, tempCol)

            self.marblesList.append(newMarble)

    def print_marbles(self):
        for i in self.marblesList:
            print (str(i))

    def print_one_marble(self, index):
        print (str(self.marblesList[index]))

    def edit_marble(self, index, col, size):
        self.marblesList[index].colour = col
        self.marblesList[index].size = size

    def add_marble_sizes(self, marble1, marble2):
        self.marblesList[marble1] + self.marblesList[marble2].size

r = Bag()
r.generate_bag(10)

print ("MARBLES:")
r.print_marbles()

print ("")
print ("marbles being added together:")
r.print_one_marble(0)
r.print_one_marble(5)

r.add_marble_sizes(0, 5)

print ("")
print ("resulting marble:")
r.print_one_marble(0)

'''For example purposes, I set the two marbles to have the same
colour and size before comparing.'''

r.edit_marble(1, "red", 3)
r.edit_marble(2, "red", 3)

print ("")
print ("marbles being compared:")
r.print_one_marble(1)
r.print_one_marble(2)

print(r.marblesList[1]==r.marblesList[2])

print ("")
print ("marbles being compared (less than):")
r.print_one_marble(5)
r.print_one_marble(7)

print(r.marblesList[5]<r.marblesList[7])

print ("")
print ("lengths being compared (less than):")
r.print_one_marble(3)
r.print_one_marble(6)

print(len(r.marblesList[3])<len(r.marblesList[6]))