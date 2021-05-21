#캠핑

import sys
r = sys.stdin.readline

def solution():
    idx = 1
    while True:
        available, term, total = map(int, r().rstrip().split())
        if term==0:
            break
        remainder = total%term
        if remainder > available:
            remainder = available

        print(f"Case {idx}: {(total//term)*available + remainder}")
        idx += 1

if __name__=='__main__':
    solution()