n_tests = int(input())

def all_pairs(x, y, n):
    total = set()
    for i in range(n + 1):
        total.add(x * i + y * (n - i))
    total = [str(x) for x in sorted(list(total))]
    print(' '.join(total))
    return 

for i in range(n_tests):
    [x, y, n] = input().split()
    x, y, n = int(x), int(y), int(n)
    all_pairs(x, y, n)