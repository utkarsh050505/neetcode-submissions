class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1

        leftMax = 0
        rightMax = 0

        while left < right:
            if height[left] <= height[right]:
                cap = min(leftMax, height[right])
                ans += max(cap - height[left], 0)
                leftMax = max(height[left], leftMax)
                left += 1
            else:
                cap = min(rightMax, height[left])
                ans += max(cap - height[right], 0)
                rightMax = max(height[right], rightMax)
                right -= 1
        
        return ans