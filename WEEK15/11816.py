string = input()
answer = 0
power = 1
if (string[0] == '0'):
    if (string[1] == 'x'):
        answer = int(string, 16)
    else:
        answer = int(string, 8)
else:
    answer = int(string)
    
print(answer)