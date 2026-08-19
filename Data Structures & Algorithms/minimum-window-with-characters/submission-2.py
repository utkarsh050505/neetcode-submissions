class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        elif len(s) == len(t):
            if sorted(s) == sorted(t):
                return s
            else:
                return ""
        
        need = {}
        for i in t:
            if i in need: need[i] += 1
            else: need[i] = 1
        
        left = 0
        min_len = float('inf')
        res = ""
        window = {}

        satisfied = 0
        require = len(need)
        
        for right in range(len(s)):
            char = s[right]
            if char in window: window[char] += 1
            else: window[char] = 1

            if char in need and window[char] == need[char]:
                satisfied += 1
            
            while satisfied == require:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left : right + 1]
                
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    satisfied -= 1
                left += 1

        return res