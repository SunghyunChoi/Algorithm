import sys
r = sys.stdin.readline

num = r()
a = set(map(int, r().split(' ')))
b = set(map(int, r().split(' ')))

intsec = a.intersection(b)
print(len(a) + len(b) - 2 * len(intsec))