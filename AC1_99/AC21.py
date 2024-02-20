class Solution(object):
    def Fibonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        dp = [0, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n]
