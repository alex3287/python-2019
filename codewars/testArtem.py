from collections import deque

D = dict()
for i in range(5):
    D.setdefault('H', 0)
    D['H'] += 1
print(D)

t = deque()
t.append(6)
print(len(t))
t.append(7)
print(len(t))