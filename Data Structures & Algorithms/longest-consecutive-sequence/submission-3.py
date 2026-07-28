class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxCons = 0
        for i in numsSet:
            cons = 1
            if i - 1 not in numsSet:
                j = i
                while j + 1 in numsSet:
                    j += 1
                    cons += 1
            if cons > maxCons: maxCons = cons
        return maxCons