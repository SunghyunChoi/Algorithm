def fib(n):

    memo = [0, 1, 1]
    memo.extend([0 for _ in range(n)])
    
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]

print(fib(100))