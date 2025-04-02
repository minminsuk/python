import numpy as np

a = np.arange(1, 37)
print('a :|n', a)

b = a.reshape(3, 12)
print('b :|n', b)

c= a.reshape(4, 9)
print('c :|n', c)

d= a.reshape(3, 2, 6)
print('d :|n', d)