# These Are sorting Algorithms and Search Algorithms
class searching:
    def __init__(self, array, item):
        self.__array = array
        self.__item = item

    def setarray(self, array):
        self.__array = array

    def setitem(self, item):
        self.__item = item

    def linear(self):
        maxIndex = len(self.__array) - 1
        location = 0
        found = False
        FoundItem = ''
        while location <= maxIndex and found is False:
            found = False
            if self.__array[location] == self.__item:
                found = True
                FoundItem = f"Found item '{self.__item}' at index {location}, Using Linear Search!"
            else:
                location += 1
                FoundItem = -1

        return FoundItem

    def binary(self):
        minIndex = 0
        maxIndex = len(self.__array) - 1
        found = False
        Founditem = ''
        while minIndex <= maxIndex and not found:
            location = int((maxIndex + minIndex) / 2)
            found = False
            if self.__array[location] == self.__item:
                found = True
                Founditem = f"Found item '{self.__item}' at index {location}, using Binary Search!"
            else:
                if self.__array.index(self.__item) > location:
                    minIndex = location + 1
                    Founditem = -1
                else:
                    maxIndex = location - 1
                    Founditem = -1

        return Founditem


class sorting:
    def __init__(self, array):
        self.array = array

    def findLowest(self):
        minIndex = 0
        maxIndex = len(self.array) - 1
        passes = 0
        lowest = 0
        while maxIndex >= minIndex:
            x = self.array[minIndex]
            if passes < 1:
                if x < self.array[minIndex+1]:
                    lowest = x
                    passes += 1
            else:
                if lowest > x:
                    lowest = x
                    passes += 1

            minIndex += 1
        return lowest

    def findHighest(self):
        minIndex = 0
        maxIndex = len(self.array) - 1
        passes = 0
        lowest = 0
        while maxIndex >= minIndex:
            x = self.array[minIndex]
            if passes < 1:
                if x > self.array[minIndex+1]:
                    lowest = x
                    passes += 1
            else:
                if lowest < x:
                    lowest = x
                    passes += 1

                minIndex += 1
        return lowest


p = searching(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 'a')
x = sorting([5,2,3,4,11,5,1,7,8,9,10])
# 1,4,7, 10
print(p.linear())
print(p.binary())
print(x.findLowest())
print(x.findHighest())
