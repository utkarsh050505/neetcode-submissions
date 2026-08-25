class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        rect = 0

        for i in range(len(heights)):
            if not stk:
                stk.append(i)
            else:
                while stk and heights[stk[-1]] > heights[i]:
                    resolve_idx = stk.pop()
                    if stk:
                        width = i - stk[-1] - 1
                        rect = max(rect, heights[resolve_idx] * width)
                    else:
                        width = i
                        rect = max(rect, heights[resolve_idx] * width)
                stk.append(i)

        while stk:
            resolve_idx = stk.pop()
            if stk:
                width = len(heights) - stk[-1] - 1
                rect = max(rect, heights[resolve_idx] * width)
            else:
                width = len(heights)
                rect = max(rect, heights[resolve_idx] * width)

        return rect