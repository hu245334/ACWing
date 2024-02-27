def hamilton(n, weight):
    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for mask in range(1, 1 << n):
        for i in range(n):
            if ((mask >> i) & 1) == 0:
                continue
            prev_mask = mask ^ (1 << i)
            for j in range(n):
                if ((prev_mask >> j) & 1) == 0:
                    continue
                dp[mask][i] = min(dp[mask][i], dp[prev_mask][j] + weight[j][i])

    return dp[(1 << n) - 1][n - 1]


if __name__ == '__main__':
    n = int(input())
    graph = []
    for i in range(0, n):
        graph.append(list(map(int, input().split())))
    ans = hamilton(n, graph)
    print(ans)
