[n_robot, index] = [int(x) for x in input().split()]
all_color = input().split()
saw = input().split()
color_dict = {}
for i in range(n_robot):
    color_dict[all_color[i]] = i

color_sum = 0
for c in saw:
    color_sum += color_dict[c]

res = index - color_sum % n_robot
print(all_color[res] if res >= 0 else all_color[n_robot + res])