from collections import deque

def is_test(item):
    if 'o' in item:
        return True
    return False

def search(name):
    dots = deque()
    dots.extend(G[name])
    check = []
    while dots:
        item = dots.popleft()
        if item not in check:
            if is_test(item):
                print(item)
                return True
            else:
                check.append(item)
                dots.extend(G[item])
    return False

G = dict()
G['you'] = ['alice', 'bob', 'claire']
G['bob'] = ['anuj', 'peggy']
G['alice'] = ['peggy']
G['claire'] = ['thom','jonny']
G['anuj'] = []
G['peggy'] = []
G['thom'] = []
G['jonny'] = []


print(G)
print(search('you'))
# d = deque()
# d.extend(G['A'])
# print(d)