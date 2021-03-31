import sys
r = sys.stdin.readline

num = int(r().strip())
list_num = list(str(num))
num_len = len(list_num)

start_num = 10**(num_len-1) - 9 * (num_len-1)
end_num = num
answer = 0
for i in range(start_num, end_num):
    test_num = i + sum(list(map(int,list(str(i)))))
    if test_num == num:
        answer = i
        break

print(answer)