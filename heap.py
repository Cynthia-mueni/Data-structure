
import heapq

h = [2,45,6,78,433,9]
heapq.heapify(h)

print(h)

heapq.heappush(h,5)
print(h)

heapq.heappop(h)
print(h)

heapq.heapreplace(h,12)
print(h)
