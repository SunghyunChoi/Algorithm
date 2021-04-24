def solution(n, arr1, arr2):
    answer = []
    for one, two in zip(arr1, arr2):
        str1 = ''
        str2 = ''
        result = ''
        for i in range(n, 1, -1):
            a = one // 2**(i-1)
            one -= a * 2**(i-1)
            b = two // 2**(i-1)
            two -= b * 2**(i-1)
            str1 += str(a)
            str2 += str(b)
        str1 += str(one % 2)
        str2 += str(two % 2)

        # print(str1, str2)
        for char1, char2 in zip(str1, str2):
            key = ''
            if char1 == '1' or char2 == '1':
                key = '#'
            else:
                key = ' '
            result += key
        answer.append(result)
    return answer

arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
n = 5

print(solution(n, arr1, arr2))