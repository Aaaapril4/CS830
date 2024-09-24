from collections import defaultdict
N = int(input())
mention_dict = defaultdict(int)

for i in range(N):
    id = int(input())
    mention_dict[id] += 1

ids = sorted(mention_dict.keys(), key = lambda x: mention_dict[x], reverse=True)
parallel_list = [ids[0]]
for i in range(1, len(ids)):
    if mention_dict[ids[i]] == mention_dict[ids[i-1]]:
        parallel_list.append(ids[i])
    else:
        break
parallel_list.sort()
print(parallel_list[0])