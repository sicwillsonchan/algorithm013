class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {} # 简历字典
        for i in range(len(nums)): # 遍历数组
            temp = target - nums[i] 
            if temp in record: # 如果满足条件，则说明
                return [record.get(temp),i]
            else:
                record[nums[i]] = i
