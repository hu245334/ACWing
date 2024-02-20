def knapsack(nums, package):
    dp = [0 for _ in range(package + 1)]
    for i in range(len(nums)):
        for j in range(package, nums[i][0] - 1, -1):
            dp[j] = max(dp[j], dp[j - nums[i][0]] + nums[i][1])
    return dp[-1]


if __name__ == '__main__':
    N, W = input().split()
    N, W = int(N), int(W)
    nums = []
    for i in range(N):
        temp = [int(j) for j in input().split()]
        nums.append(temp)
    result = knapsack(nums, W)
    print(result)
