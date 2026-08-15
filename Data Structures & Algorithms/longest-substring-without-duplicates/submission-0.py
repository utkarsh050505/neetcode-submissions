class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0
        left = 0
        ans = 0

        window = set()
        while right <= len(s) - 1:
            if s[right] not in window:
                window.add(s[right])
                right += 1
            else:
                window.remove(s[left])
                left += 1
            ans = max(ans, right - left)
        
        return ans