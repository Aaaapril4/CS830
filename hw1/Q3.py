def find_min(n_S: int, S: list):
    S.sort()
    while n_S != 0:
        min_ = S[0]
        num_min = 0

        for n in S:
            if n == min_:
                num_min += 1
            else:
                break
        
        print(n_S)
        n_S -= num_min
        S = S[num_min:]
        
    return

n_S = int(input())
S = input().split()
S = [int(x) for x in S]

find_min(n_S, S)