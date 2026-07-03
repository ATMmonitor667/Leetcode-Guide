class StockPrice(object):

    def __init__(self):
        self.time_to_price = {}
        self.latest_time = 0

        self.max_heap = []  # stores (-price, timestamp)
        self.min_heap = []  # stores (price, timestamp)

    def update(self, timestamp, price):
        self.time_to_price[timestamp] = price
        self.latest_time = max(self.latest_time, timestamp)

        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self):
        return self.time_to_price[self.latest_time]

    def maximum(self):
        while self.max_heap:
            neg_price, timestamp = self.max_heap[0]
            price = -neg_price

            if self.time_to_price[timestamp] == price:
                return price

            heapq.heappop(self.max_heap)

    def minimum(self):
        while self.min_heap:
            price, timestamp = self.min_heap[0]

            if self.time_to_price[timestamp] == price:
                return price

            heapq.heappop(self.min_heap)


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()