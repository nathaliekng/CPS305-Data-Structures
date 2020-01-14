def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
    
    if first<last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)

def mo3_quickSort(alist):
    mo3_quickSortHelper(alist, 0, len(alist)-1)

def mo3_quickSortHelper(alist, first, last):
    pivot = findPivot(alist)
    #new pivot using median
    #switch the first value in alist with alist[pivot]
    temp = alist[0]
    alist[0] = alist[pivot]
    alist[pivot] = temp 

    if first<last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)

def findPivot(alist):
    #function to sort my first, middle and last by least to greatest
    #sort list, then return index of value that ends up in the middle
    first = alist[0]
    middle = alist[len(alist)//2]
    last = alist[len(alist)-1]
    list = [first, middle, last]

    if list[0] == list[1]:
        if list[1] > list[2]:
            temp = list[0]
            list[0] = list[2]
            list[2] = temp
    if list[0] > list[1]:
        temp = list[0] 
        list[0]=list[1]
        list[1] = temp
    if list[1] > list[2]:
        temp = list[1]
        list[1] = list[2]
        list[2] = temp
        if list[1] < list[0]: 
            temp = list[0]
            list[0] = list[1]
            list[1] = temp
    if list[1] == middle:
        return len(alist)//2
    elif list[1] == first:
        return 0
    else:
        return len(alist)-1
def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark

alist = [54,26,93,17,77,31,44,55,20]
#quickSort(alist)
mo3_quickSort(alist)
print(alist)
