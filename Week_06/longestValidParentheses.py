class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        res = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == ')':
                    left = i - dp[i - 1] - 1
                    if left >= 0 and s[left] == '(':
                        dp[i] = dp[i - 1] + 2 + (dp[left - 1] if left > 0
                                                 else 0)
                        res = max(res, dp[i])
                else:
                    if i == 1:
                        dp[i] = 2
                    else:
                        dp[i] = dp[i - 2] + 2
                    res = max(res, dp[i])
        return res
