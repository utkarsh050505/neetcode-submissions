class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        count1 = [0] * 26
        count2 = [0] * 26

        for i in s1:
            count1[ord(i) - ord('a')] += 1
        
        for right in range(len(s2)):
            if right < k:
                count2[ord(s2[right]) - ord('a')] += 1
            else:
                count2[ord(s2[right]) - ord('a')] += 1
                count2[ord(s2[right - k]) - ord('a')] -= 1     
            
            if count1 == count2: return True
        
        return False