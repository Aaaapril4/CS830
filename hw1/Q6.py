n_tests = int(input())

def sqrt(x):
    '''
    Find the closest upper square number of x
    '''
    if x == 0:
        return 0
    i, j = 0, x
    while i <= j:
        mid = i + (j - i) // 2
        if (mid - 1) ** 2 < x and mid ** 2 >= x:
            return mid
        elif mid ** 2 < x:
            i = mid + 1
        elif mid ** 2 > x:
            j = mid - 1


def get_num(n_min, n_max): 
    min_sqrt = sqrt(n_min)
    d = n_max // 12 - n_min // 12 + int(not(n_min % 12))
    s, b = 0, 0
    while min_sqrt ** 2 <= n_max:
        if min_sqrt ** 2 % 12 == 0:
            b += 1
        s += 1
        min_sqrt += 1
    return d, s, b

# get_num(300, 346)
for i in range(n_tests):
    [n_min, n_max] = input().split()
    n_min, n_max = int(n_min), int(n_max)
    print(' '.join([str(x) for x in get_num(n_min, n_max)]))