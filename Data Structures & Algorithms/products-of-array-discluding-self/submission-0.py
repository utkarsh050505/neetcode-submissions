class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        for i in range(len(nums)):
            if i == 0:
                left.append(1)
            else:
                left.append(left[-1] * nums[i-1])
        
        right = []
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right.append(1)
            else:
                right.append(right[-1] * nums[i + 1])
        
        right = right[::-1]
        ans = []
        for i in range(len(left)):
            ans.append(left[i] * right[i])
        return ans