"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    templist = []
    if items is None:
        print("empty")
    else:
        for y in range(len(items)):
            templist.append(str(items[y]))
        for i in range(len(templist)):
            x = 0
            for j in range(len(templist)):
                if templist[i] == templist[j]:
                    x = x +1
                    frequencies[str(templist[i])] = x
                    
    return frequencies
