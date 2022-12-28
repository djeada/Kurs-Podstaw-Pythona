def fastFib(n, memo):
    global numCalls
    numCalls += 1
    if not n in memo:
        memo[n] = fastFib(n - 1, memo) + fastFib(n - 2, memo)
    return memo[n]


numCalls = 0
memo = {0: 1, 1: 1}
print(fastFib(5, memo))
print(numCalls)
