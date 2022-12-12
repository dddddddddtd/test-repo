import numpy as np


X = np.array([
    [0.51916715, 0.46894559],
    [0.42850038, 0.49204451],
    [0.44844347, 0.44231806],
    [0.49862482, 0.61777354],
    [0.58701822, 0.32693741],
    [0.37040839, 0.48617894],
])

a = np.array([0.5, 0.5])

distances = (abs(a-X)).sum(1)
print(a-X)
print(distances)
s1 = distances < 0.1

s2 = distances < 0.12

print(s1)
print(s2)
print(s2^s1)

print(distances[s2^s1].argmin())

print((s2^s1).nonzero())
for i, x in enumerate(X):
    print(i, x)