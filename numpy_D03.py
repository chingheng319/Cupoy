import numpy as np
v1 = 20000
v0 = 20
v2 = 20*np.log10(v1/v0)
print(v2)

v130 = 10**(30/20)*v0
v150 = 10**(50/20)*v0
print(v130/v150)
