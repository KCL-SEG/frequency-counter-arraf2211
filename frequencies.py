"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    if items is None:
        print("empty")
    else:
        for i in range(len(items)):
            x = 0
            for j in range(len(items)):
                if items[i] == items[j]:
                    x = x +1
                    frequencies[str(items[i])] = x

    return frequencies
