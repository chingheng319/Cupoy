import numpy as np
e_score = np.array([55,89,76,65,48,70])
m_score = np.array([60,85,60,68,55,60])
c_score = np.array([65,90,82,72,66,77])
c1 = np.greater(e_score,m_score)
print(c1)
print(np.sum(c1))
c2 = np.greater(c_score,m_score)
c3 = np.greater(c_score,e_score)
print(np.logical_and(c2,c3))
print(np.logical_and(c2,c3).any())