import math

vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
dist_to_i =   [8, 6, 6, 3, 10, 2, 5, 5, 0, 2, 15, math.inf, math.inf]
dist_from_i = [20, 22, 23, 28, 29, 26, 28, 16, 0, 2, 6, 7, 9]

print('\t', end = '')
for vert in vertices:
    print(str(vert) + '\t', end = '')
print()
for i in range(len(vertices)):
    print(str(vertices[i]) + '\t', end = '')
    for j in range(len(vertices)):
        print(str(dist_to_i[i] + dist_from_i[j]) + '\t', end = '')
    print()
