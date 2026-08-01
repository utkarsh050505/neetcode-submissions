import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        print(cleaned_text)
        l = len(cleaned_text) - 1
        r = 0
        while r <= l:
            if cleaned_text[r] != cleaned_text[l]:
                return False
            else:
                r += 1
                l -= 1
        return True