class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0

        count = [0] * 26
        maxFreq = 0
        ans = 0

        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1
            maxFreq = max(maxFreq, count[ord(s[right]) - ord('A')])

            if (right - left + 1) - maxFreq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans 