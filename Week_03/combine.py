class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []

        def dfs(level, start, pre):
            if level == k:
                res.append(pre)
                return
            for i in range(start, n - (k - level) + 2):
                dfs(level + 1, i + 1, pre + [i])

        dfs(0, 1, [])
        return res
