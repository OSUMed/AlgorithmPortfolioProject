


def getTesla(M):
    path = M
    # first set up our grid and make our grid based on input lengths:
    m = len(path)       # m is i aka columns
    n = len(path[0])    # n is j aka columns

    # They need at minimum 1 life point to get to the end:
    if m == 1 and n == 1:
        return max(1 - path[0][0], 1)


    dp = [[0] * n for _ in range(m)]    # m is rows made and n is the columns per row

    # Here we will start from the end and work backwards. For each iteration, we will ask the question: "what is the
    # minimum life Tesla can have and still go that direction:
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):

            # base case: starting point:
            if (i == m -1) and (j == n - 1):
                dp[i][j] = 1 - path[i][j]

            # here we are considering for all situations where we can only go right and still have 1 life minimum:
            elif i == m - 1 and j < n - 1:
                dp[i][j] = max(dp[i][j + 1] - path[i][j], 1)

            # here we are considering for all situations where we can only go down and still have 1 life minimum:
            elif j == n - 1 and i < m - 1:
                dp[i][j] = max(dp[i+1][j] - path[i][j], 1)

            # Here we first find the easiest path to take for Tesla-- which way can be get away with the least life:
            else:
                minimum = min(dp[i + 1][j], dp[i][j + 1])

                # After we know what direction is safer for Tesla, we can go that direction and still have 1 life min:
                dp[i][j] = max(minimum - path[i][j], 1)

    return dp[0][0]

M = [[-1, -2, 2], [10, -8, 1], [-5, -2, -3]]
answer = getTesla(M)
print(answer)




