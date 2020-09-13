class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backTrack(S, nLeft: int, nRight: int) -> None:
            if 2 * n == len(S):
                ans.append("".join(S))
                return
            if nLeft < n:
                S.append("(")
                backTrack(S, nLeft+1, nRight)
                S.pop()
            if nLeft > nRight:
                S.append(")")
                backTrack(S, nLeft, nRight+1)
                S.pop()
        backTrack([], 0, 0)
        return ans
