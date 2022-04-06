import numpy as np

z = np.zeros(6).reshape(2, 3)
o = np.ones(6).reshape(2, 3)

print(z)
print(o)

print(np.vstack((z, o)))