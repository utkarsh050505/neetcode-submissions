class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minn = float('inf')

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < minn: minn = nums[mid]

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
        return minn