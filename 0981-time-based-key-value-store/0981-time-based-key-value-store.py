from collections import defaultdict

class TimeMap(object):

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key, value, timestamp):
        self.map[key].append((timestamp, value))

    def get(self, key, timestamp):
        arr = self.map[key]

        left = 0
        right = len(arr) - 1
        ans = ""

        while left <= right:
            mid = (left + right) // 2

            stamp, value = arr[mid]

            if stamp <= timestamp:
                ans = value
                left = mid + 1
            else:
                right = mid - 1

        return ans

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)