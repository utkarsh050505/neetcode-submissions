class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                idx = stk.pop()
                ans[idx] = i - idx
            else:
                stk.append(i)
        
        return ans