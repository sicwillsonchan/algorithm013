class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits or [0]
        last = digits.pop()
        
        if last == 9:
            return self.plusOne(digits) + [0]
        else:
            return digits + [last + 1]
