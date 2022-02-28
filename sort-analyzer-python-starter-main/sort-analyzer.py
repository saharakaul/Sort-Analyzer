# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def bubbleSort(anArray):
   for i in range(len(anArray)):
       for y in range(len(anArray) -1):
           if anArray[y] > anArray [y+1]:
               anArray[y], anArray[y+1] = anArray[y+1], anArray[y]


def selectionSort(anArray):
   for i in range(len(anArray) -1):
       min_index = i
       for y in range(i+1, len(anArray) -1):
           if anArray[y] < anArray[min_index]:
               min_index = y
       anArray[i], anArray[min_index] = anArray[min_index], anArray[i]

def insertionSort(anArray):
   for i in range(1, len(anArray)):
       x = anArray[i]
       y = i
       while y > 0 and anArray[y-1] > x:
           anArray[y] = anArray[y-1]
           y = y -1
       anArray[y] = x



def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")
loop = True
while loop:
    print("""\nMain Menu
            1:Sort Random (Bubble)
            2: Sort Reversed (Bubble)
            3: Sort Nearly (Bubble)
            4: Sort Unique (Bubble)
            5:Sort Random (Selection)
            6: Sort Reversed (Selection)
            7: Sort Nearly (Selection)
            8: Sort Unique (Selection)
            9:Sort Random (Insertion)
            10: Sort Reversed (Insertion)
            11: Sort Nearly (Insertion)
            12: Sort Unique (Insertion)
            13:Exit
            """)
    #Get User Instruction
    Number = int(input("Please Enter the command: "))
    if Number == 1:
        start = time.perf_counter()
        bubbleSort(randomData)
        print("It takes " + str(time.perf_counter() - start) + " to run this code")
    elif Number == 2:
        start = time.perf_counter()
        bubbleSort(reversedData)
        print("It takes " + str(time.perf_counter() - start) + " to run this code")
    elif Number == 3:
        start = time.perf_counter()
        bubbleSort(nearlySortedData)
        print("It takes " + str(time.perf_counter() - start) + " to run this code")
    elif Number == 13:
        loop = False

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
print(randomData[0:50])
print(reversedData[0:50])
print(nearlySortedData[0:50])
print(fewUniqueData[0:50])


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")
