#돌 게임

import sys
r = sys.stdin.readline

rockNum = int(r())

if rockNum%2:
    print("SK")
else:
    print("CY")