import heapq

class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []
        self.length = 0

    def insert(self, num):
        if len(self.small) == 0 or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
        
        self.length += 1

    def remove(self, num):
        try:
            if num <= -self.small[0]:
                self.small.remove(-num)
                heapq.heapify(self.small)
            else:
                self.large.remove(num)
                heapq.heapify(self.large)
        except (ValueError, IndexError):
            return "Wrong!"

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
        
        self.length -= 1
        if self.length == 0:
            return "Wrong!"
        return None

    def median(self):
        if self.length == 0:
            return "Wrong!"
        elif self.length % 2 == 1:
            res = -self.small[0]
        else:
            res = (-self.small[0] + self.large[0]) / 2
        return int(res) if res == int(res) else res

# Main program
N = int(input())
median_finder = MedianFinder()

for _ in range(N):
    ins, value = input().split()
    value = int(value)
    
    if ins == 'a':
        median_finder.insert(value)
        print(median_finder.median())
    elif ins == 'r':
        result = median_finder.remove(value)
        if result is not None:
            print(result)
        else:
            print(median_finder.median())