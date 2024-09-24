import os
class Chest:
    def __init__(self, maximum_cache = 100) -> None:
        self.cache = {}
        self.maximum_cache = maximum_cache
        self.length = 0
        self.cache_length = 0
    
    def add(self, id) -> None:
        key = 0
        for l in id:
            key += ord(l)
        key %= 10
        if key not in self.cache:
            self.cache[key] = []
        if self.cache_length >= self.maximum_cache:
            with open(str(key), 'a') as f:
                f.writelines([id + '\n'])
            self.length += 1
        else:
            self.cache[key].append(id)
            self.length += 1
            self.cache_length += 1
        return
    
    def search(self, id):
        key = 0
        for l in id:
            key += ord(l)
        key %= 10
        if key not in self.cache:
            return 0
        else:
            res = 0
            for i in self.cache[key]:
                if i == id:
                    res += 1
            if os.path.exists(str(key)):
                with open(str(key), 'r') as f:
                    for line in f:
                        if line.strip() == id:
                            res += 1
            return res

c = Chest(3)
M = int(input())
res = 0
for _ in range(M):
    c.add(input())

N = int(input())
res = 0
for _ in range(N):
    res += c.search(input())
print(res)

for k in c.cache.keys():
    if os.path.exists(str(k)):
        os.remove(str(k))