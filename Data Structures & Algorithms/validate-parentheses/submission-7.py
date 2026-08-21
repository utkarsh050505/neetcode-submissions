class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for i in s:
            if i in ["(", "{", "["]:
                stk.append(i)
            else:
                if stk: elem = stk.pop() 
                else: return False
                if (i == ")" and elem != "(") or (i == "}" and elem != "{") or (i == "]" and elem != "["):
                    return False
        if stk: return False
        return True