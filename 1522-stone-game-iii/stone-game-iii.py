class Solution(object):
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [0] * (n + 3)

        for i in range(n - 1, -1, -1):
            total = 0
            best = float('-inf')

            for take in range(3):
                if i + take < n:
                    total += stoneValue[i + take]
                    best = max(best, total - dp[i + take + 1])

            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"