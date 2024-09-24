import heapq

class Instruction:
    def __init__(self):
        self.arrival_heap = []
        self.duration_heap = []

    def add(self, t, l):
        heapq.heappush(self.arrival_heap, (t, l))
        return
    
    def get_minimum_arrival(self):
        if self.arrival_heap:
            return self.arrival_heap[0][0]
    
    def move_to_duration_heap(self, current_time):
        while self.arrival_heap and self.arrival_heap[0][0] <= current_time:
            arrival_time, duration = heapq.heappop(self.arrival_heap)
            heapq.heappush(self.duration_heap, (duration, arrival_time))
        return
    
    def get_minimum_duration_task(self):
        if self.duration_heap:
            return heapq.heappop(self.duration_heap)
        else:
            return None, None
    
    def is_empty(self):
        return not self.arrival_heap and not self.duration_heap
    
    def do_earliest_task(self):
        if self.arrival_heap:
            return heapq.heappop(self.arrival_heap)
        else:
            return None, None


N = int(input())
instructions = Instruction()
total_time = 0
current_time = 0
for _ in range(N):
    [t, l] = [int(x) for x in input().split()]
    instructions.add(t, l)

while not instructions.is_empty():
    min_time = instructions.get_minimum_arrival()
    if min_time != None and min_time <= current_time:
        instructions.move_to_duration_heap(current_time)

    l, t = instructions.get_minimum_duration_task()
    if t is None:
        t, l = instructions.do_earliest_task()
        current_time = t + l
        total_time += l
    else:
        current_time += l
        total_time += current_time - t
print(total_time // N)