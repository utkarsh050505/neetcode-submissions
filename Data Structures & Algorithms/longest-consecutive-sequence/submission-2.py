class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxElem = 0
        for i in numsSet:
            j = i
            cons = 1
            while (j + 1) in numsSet:
                cons += 1
                j += 1
            if cons > maxElem:
                maxElem = cons
        return maxElem