def find_start(n_node, health_in, health_out):
    current_health = 0
    start = 0
    for i in range(n_node):
        net_health = health_in[i] - health_out[i]
        current_health += net_health

        if current_health < 0:
            start = i + 1
            current_health = 0
    return start

n_node = int(input())
health_in = []
health_out = []
for i in range(n_node):
    i, o = input().split()
    health_in.append(int(i))
    health_out.append(int(o))
print(find_start(n_node, health_in, health_out))