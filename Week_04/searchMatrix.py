class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        if matrix[0][0]>target or matrix[-1][-1]<target: return False
        if matrix[0][0]==target or matrix[-1][-1]==target: return True
        signal=0
        row=len(matrix)
        for i in range(1,row):
            if matrix[i][0]==target:
                return True
            elif matrix[i][0]<target:
                signal=i
            else:
                break
        for i in matrix[signal]:
            if i==target:
                return True
        return False
