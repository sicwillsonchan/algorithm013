class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def  backTrack(conbination,nums,n):
            if n == 0:
                if conbination not in conbination:
                    res.append(conbination)
            else:
                for j in range(len(nums)):
                    element = nums[j]
                    nums.remove(element)
                    backTrack(conbination + [element],nums,n-1)
                    nums.insert(j,element)
        res = []
        backTrack([],nums,n)
        return res

