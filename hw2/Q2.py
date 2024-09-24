N = int(input())
stack = []
length = 0
important = -1

def find_important(stack):
    return sorted(stack, reverse=True)[0]

for i in range(N):
    instructions = [int(x) for x in input().split()]
    if instructions[0] == 1:
        stack.append(instructions[1])
        length += 1
        if important < instructions[1]:
            important = instructions[1]
    elif instructions[0] == 2:
        stack.pop()
        length -= 1
        if length > 0:
            important = find_important(stack)
        else:
            important = -1
        
    elif instructions[0] == 3:
        print(important)
    else:
        break