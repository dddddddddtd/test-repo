import math
import random

import matplotlib.patches
import numpy as np
from matplotlib import pyplot as plt

X = np.array([
    [0.51916715, 0.46894559],
    [0.42850038, 0.49204451],
    [0.45844347, 0.44231806],
    [0.49862482, 0.61777354],
    # [0.55701822, 0.32693741],
    [0.37040839, 0.48617894],
])
y = np.array([
    1,
    0,
    0,
    0,
    # 1,
    0
])

oX = np.array(
    [[0.51916715, 0.46894559], [0.3464042256627114, 0.5129599181627115], [0.36847075424212555, 0.4028647332578744], [0.49287499380029176, 0.6594306863002918], [0.3248957760286293, 0.4914514685286293]]
)
r = np.array(
    [0.21677725]
)

ccr2X= np.array([[0.3464042256627114, 0.5129599181627115], [0.36847075424212555, 0.4028647332578744], [0.49287499380029176, 0.6594306863002918], [0.3248957760286293, 0.4914514685286293], [0.51916715, 0.46894559]])
ccr2y = np.array([0, 0, 0, 0, 1])
minority = X[y == 1]

plt.figure(figsize=(6, 6))
axes = plt.axes()

axes.set_xlim(0, 1)
axes.set_ylim(0, 1)
axes.scatter(X[:, 0], X[:, 1], c=y)

axes.scatter(ccr2X[:, 0], ccr2X[:, 1], c=ccr2y, marker='v')

for i, x in enumerate(minority):
    polygon = matplotlib.patches.RegularPolygon(x, 4, radius=r[i], orientation=math.pi / 2, fill=0)
    axes.add_patch(polygon)
axes.scatter(oX[:, 0], oX[:, 1], marker='x')
plt.show()
