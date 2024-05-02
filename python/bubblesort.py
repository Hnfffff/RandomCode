def bubble(array):
    arrayLength = len(array)
    for Item in range(arrayLength):
        swap = False
        for number in range(arrayLength - Item - 1):
            if array[number] > array[number+1]:
                templist = array[number]
                array[number] = array[number+1]
                array[number+1] = templist
                print(arr)
                swap = True
        if not swap:
            break

arr = [1,6,4,6,8,9,5,3,3,5,67,8,5,4,23,2,4,56,7,8,54,3,2,2]
bubble(arr)
print(arr)
