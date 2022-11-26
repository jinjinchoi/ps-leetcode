from typing import List, Tuple
def k_closest_points(points: List[Tuple[int, int]], k: int) -> List[Tuple[int, int]]:
      import heapq, math
      def dist(point):
          return -(point[0] ** 2 + point[1] ** 2) # "-" for max heap

      max_heap = []
      for i in range(k):
          pt = points[i]
          heapq.heappush(max_heap, (dist(pt), pt))

      for i in range(k, len(points)):
          pt = points[i]
          # max_heap[0] is root of max heap, the point with largest distance
          # max_heap[0][0] is -distance
          if dist(pt) > max_heap[0][0]: 
              heapq.heappop(max_heap)
              heapq.heappush(max_heap, (dist(pt), pt))

      res = []
      for _ in range(k):
          _, pt = heapq.heappop(max_heap)
          res.append(pt)

      return res

#Driver code
inputs = ["3","2"]
inputs1 = [["1 1","2 2","3 3"],["1 3","-2 2"]]
inputs2 = ["1","1"]
for i in range(len(inputs)):
    points = []
    n = int(inputs[i])
    for j in range(n):
        points.append(tuple(int(x) for x in inputs1[i][j].strip().split()))
    k = int(inputs2[i])
    print("K closest points :",str(k_closest_points(points, k)))
