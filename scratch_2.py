import math
import random

import numpy as np
from matplotlib import pyplot as plt

y = np.array([1, 0, 0, 0, 1, 0])
y = np.array([1, 0, 0, 0, 0, 0])

X = np.array([
    [0.51916715, 0.46894559],
    [0.42850038, 0.49204451],
    [0.44844347, 0.44231806],
    [0.49862482, 0.61777354],
    [0.58701822, 0.32693741],
    [0.37040839, 0.48617894],
])


X = np.array([
    [0.51916715, 0.46894559],
    [0.42850038, 0.49204451],
    [0.45844347, 0.44231806],
    [0.49862482, 0.61777354],
    [0.55701822, 0.32693741],
    # [0.37040839, 0.48617894],
])
y = np.array([
    1,
    0,
    0,
    0,
    1,
    # 0
])

oX = np.array(
    [[0.51916715, 0.46894559], [0.42850038, 0.49204451], [0.45844347, 0.44231806], [0.49862482, 0.61777354], [0.55701822, 0.32693741], [0.37040839, 0.48617894]]
)
r= np.array(
    [0.08735121, 0.2139554 ]
)
minority = X[y==1]
# x = minority[0]
#
# points = []
# for i in range(1000):
#     random_translation = np.random.rand(2)*2-1
#     multiplier = random_translation / abs(random_translation).sum()
#     # multiplier = (multiplier-1) * 2
#     new_point = x + multiplier * r[0] * np.random.rand(1)
#     points.append(new_point)
# plt.figure(figsize=(6,6))
# points = np.array(points)
# axes = plt.axes()
# axes.set_xlim(0, 1)
# axes.set_ylim(0, 1)
# circle = plt.Circle(x, r[0], fill=False)
# axes.add_artist(circle)
# axes.scatter(x[0], x[1])
# axes.scatter(points[:, 0], points[:, 1], marker='x')
# plt.show()
# print(minority)
#
plt.figure(figsize=(6, 6))
axes = plt.axes()
axes.scatter(X[:, 0], X[:, 1], c=y)
axes.set_ylim(0, 1)
axes.set_xlim(0, 1)
for i, x in enumerate(minority):
    circle = plt.Circle(x, r[i], fill=False)
    axes.add_artist(circle)

axes.scatter(oX[:, 0], oX[:, 1], marker='x')

plt.show()