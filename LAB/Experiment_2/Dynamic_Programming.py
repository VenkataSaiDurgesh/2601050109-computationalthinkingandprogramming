def knapsack(w, v, c):
    n = len(w)
    dp = [[0] * (c + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(c + 1):
            if w[i - 1] <= j:
                dp[i][j] = max(v[i - 1] + dp[i - 1][j - w[i - 1]],
                               dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][c]


w = [2, 3, 4, 5]
v = [3, 4, 5, 6]
c = 5

print("Maximum value:", knapsack(w, v, c))
