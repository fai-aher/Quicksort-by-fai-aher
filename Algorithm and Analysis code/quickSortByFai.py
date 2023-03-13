"""
This is the implementation of the Quicksort algorithm, which uses the divide-and-conquer
strategy for sorting elements of a set as long as they are mutually comparable.

I have prepared a document with the mathematical proof of the average case temporal complexity
which is approximately 1.39nLogn.

This implementation is made with the programming language Python.

This recursive algorithm consists of two functions: Partition and Quicksort.

The sorting process is done from the smaller element to the larger one in the set.

@author @fai-aher (GitHub)
"""

#First fuction: Partition

"""
@param i: initial position (index) of the array that wants to be sorted.
@param f: final position (index) of the array that wants to be sorted.

@return pivotPosition: position of the array where the selected pivot will be finally located.
"""

from random import randint


def Partition(array: list, i: int, f:int) -> int:

    #Generation of the pivot position from a random number between i and f.
    pivotPosition = randint(i, f)
    pivot = array[pivotPosition]

    #Exchange of pivot position element and last element of the array
    array[pivotPosition] = array[f]
    array[f] = pivot

    #Main cycle to exchange first element from the left that is larger than the pivot
    #and first element from the right which is smaller than the pivot.

    fromLeftIndex = i
    fromRightIndex = (f-1)

    while fromLeftIndex <= fromRightIndex:
        leftElement = array[fromLeftIndex]
        rightElement = array[fromRightIndex]

        if (leftElement > pivot) and (rightElement <= pivot):

            #swap
            temp = leftElement
            array[fromLeftIndex] = array[fromRightIndex]
            array[fromRightIndex] = temp

            #Navigator indexes advance 1 position.
            fromLeftIndex += 1
            fromRightIndex -= 1


        elif (leftElement > pivot) and (rightElement > pivot):

            #right navigator index should decrease 1.
            fromRightIndex -= 1    


        elif (leftElement <= pivot) and (rightElement <= pivot):

            #left navigator index should increase 1.
            fromLeftIndex += 1

        else:
            #if no ideal condition is achieved, navigator indices should advance 1 position.
            fromLeftIndex += 1
            fromRightIndex -= 1

    #Finally, pivot and the last element with the left index counter are swapped.
    array[f] = array[fromLeftIndex]
    array[fromLeftIndex] = pivot

    pivotPosition = fromLeftIndex

    return pivotPosition


#Second function: Quicksort

"""
@param i: initial position (index) of the array that wants to be sorted.
@param f: final position (index) of the array that wants to be sorted.

@return array: the array that was given in parameters but sorted with the Quicksort algorithm.

"""


def Quicksort(array: list, i: int, f: int) -> list:

    #This only works if the initial index is smaller than the final index in the array it is sorting.
    if i < f:
        #Partition is made to get the pivot position after sorting the array in some range.
        pivotPosition = Partition(array,i,f)
        #Recursive call to sort elements in a range which does not include the pivot (cause it is already in the final correct position).
        Quicksort(array, i, pivotPosition-1)
        Quicksort(array, pivotPosition + 1, f)

    return array


#----------------------------------------------Testing area-----------------------------------------------------

testingArray = [200,500,3,4,5,6,6,7,4,2,1,24,5,325,678997,1234234234,13,43,122,145,13567,12334,9,0]
i = 0
f = (len(testingArray)-1)

#--------------------------------------------Main application----------------------------------------------------
print("\n-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
print("Welcome to the Quicksort recursive sorting algorithm implementation made by @fai-aher.\n ->If you want to test the implementation, edit the testingArray in the 'Testing Area'.")
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")

print("\n*This is the unsorted array: ", testingArray, "\n")
print("----> Now this is the array sorted with Fai's Quicksort algoritm: ",Quicksort(testingArray, i, f),"\n")
