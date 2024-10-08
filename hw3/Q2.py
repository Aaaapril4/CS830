[n_tower, n_room] = [int(x) for x in input().split()]
animals = []
for i in range(n_tower):
    animals.append(int(input()))

animals = sorted(animals, reverse=True)
for i in range(n_room):
    print(animals[i])
