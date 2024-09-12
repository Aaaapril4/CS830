n_tests = int(input())

def get_miles(n_frag, c): 
    n_wings, n_frag = n_frag // c, n_frag % c
    if n_wings == 0:
        return 0
    else:
        return n_wings + get_miles(n_wings + n_frag, c)



for i in range(n_tests):
    [n, m, c] = input().split()
    n, m, c = int(n), int(m), int(c)
    print(n//m + get_miles(n//m, c))