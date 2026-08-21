class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()

        ans = []

        for right in range(len(nums)):
            while queue and queue[0][1] < right - k + 1:
                queue.popleft()
            while queue and queue[-1][0] <= nums[right]:
                queue.pop()
            queue.append((nums[right], right))

            if right >= k - 1:
                ans.append(queue[0][0])

        return ans 