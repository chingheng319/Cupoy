import numpy as np
np.__version__
c = np.arange(0,21,1)
d = c[::2]
e = c[3::3]
a = np.array([[0,21,1],[4,2,5],[8,2,9]])
print(a)
print(a.flatten())
b = np.array(range(30))
print(b)
f = b.reshape((5,6))
print(f)
g = np.reshape(b,(5,6),order='F')
print(g)
h = np.where((g%6=1))
print(h)