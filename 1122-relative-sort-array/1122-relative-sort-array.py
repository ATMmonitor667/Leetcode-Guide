class Solution(object):
    def relativeSortArray(self, arr1, arr2):
            count = Counter(arr1)
            j = 0

            for value in arr2:
                numOccur = count[value]

                arr1[j:j + numOccur] = [value] * numOccur
                j += numOccur

                del count[value]

            for value in sorted(count):
                numOccur = count[value]

                arr1[j:j + numOccur] = [value] * numOccur
                j += numOccur

            return arr1
        