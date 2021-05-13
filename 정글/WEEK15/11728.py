import sys
r = sys.stdin.readline

num = r();
list_a = list(map(int, r().split(' ')))
list_b = list(map(int, r().split(' ')))

a_idx = 0
b_idx = 0

while(a_idx < len(list_a) or b_idx < len(list_b)):
    if b_idx == len(list_b):
        print(list_a[a_idx], end=' ')
        a_idx += 1
    elif a_idx == len(list_a):
        print(list_b[b_idx], end=' ')
        b_idx += 1
    elif list_a[a_idx] <= list_b[b_idx]:
        print(list_a[a_idx], end=' ')
        a_idx += 1
    else:
        print(list_b[b_idx], end=' ')
        b_idx += 1

