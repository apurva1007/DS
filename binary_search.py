import random


class BinarySearch:

    array = []

    def __init__(self, n, key):
        self.n = n
        self.key = key
        for i in range(n):
            num = random.randrange(0, n)
            self.array.append(num)
        print('Initial array is', self.array)

    def sort_array(self):
        self.array.sort()
        print('Array after sorting', self.array)

    def binary_search(self):

        self.sort_array()

        low = 0
        high = len(self.array)

        while low <= high:
            mid = int((low+high)/2)
            # print('mid', mid)

            if self.array[mid] < self.key:
                low = mid + 1
            elif self.array[mid] > self.key:
                high = mid - 1
            elif self.array[mid] == self.key:
                return mid
            else:
                return


search = BinarySearch(15, 3)
index = search.binary_search()

print('Index of element is', index)