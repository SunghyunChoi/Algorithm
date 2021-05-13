_ = input()
string = input()
hiddenNumber = ''
answer = 0

for char in string:
    try:
        newChar = int(char)
        hiddenNumber += char
    except:
        if(hiddenNumber):
            answer += int(hiddenNumber)
            hiddenNumber = ''
if (hiddenNumber):
    answer += int(hiddenNumber)
print(answer)