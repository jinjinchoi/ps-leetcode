import heapq
class MedianOfStream:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
    def add_number(self, num: float) -> None:
        if len(self.min_heap) == 0 or num < self.min_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        self._balance()
    def get_median(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return -self.max_heap[0]
    def _balance(self) -> None:
        if len(self.max_heap) < len(self.min_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -val)
#Driver code
inputs = ["6"]
inputs1 = [["1", "2", "3" ,"get","4","get"]]
for i in range(len(inputs)):
    median_of_stream = MedianOfStream()
    n = int(inputs[i])
    actual_output = []
    for j in range(n):
        line = inputs1[i][j].strip()
        if line == 'get':
            median = median_of_stream.get_median()
            actual_output.append(str(median))
        else:
            num = float(line)
            median_of_stream.add_number(num)
    print("Median of stream add :",actual_output)
