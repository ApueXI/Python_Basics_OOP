"""
from tkinter import*

application = Tk()

application.mainloop()
"""

def mergedArrays(arrayA, arrayB):
    # set() makes it a set can also be done in list() or tupple()
    return sorted(set(arrayA + arrayB))

a = [1, 2, 3, 3, 4, 5, 6]
b = [4, 4, 5, 6, 7, 8, 9,]
c = mergedArrays(a, b)

print(c)