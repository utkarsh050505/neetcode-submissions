class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums) - 1  # Since length is n + 1, n is len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            
            # Count how many numbers are <= mid
            count = sum(1 for num in nums if num <= mid)
            
            # Binary search decision based on the Pigeonhole Principle
            if count > mid:
                high = mid  # Duplicate is in the lower half [low, mid]
            else:
                low = mid + 1  # Duplicate is in the upper half [mid + 1, high]
                
        return low
