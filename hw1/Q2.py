num_tests = int(input())

def check_value(S):
    if S > 1000000:
        return S % 1000000
    elif S < 0:
        return S % 1000000 + 1000000
    else:
        return S
        
for test_idx in range(num_tests):
    line = input().split()
    S = int(line[0]) # Starting bet
    k = int(line[1]) # Number of rounds

    # Your code goes here!
    for i in range(k):
        if S % 2 == 1:
            S = check_value(2 * check_value(S - 15))
        elif S % 2 == 0:
            S = check_value(3 * check_value(S - 99))
        


    print(S)