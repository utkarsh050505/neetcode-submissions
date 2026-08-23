class MinStack:

    def __init__(self):
        self.stk = []
        self.minn = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.minn or val <= self.minn[-1]:
            self.minn.append(val)

    def pop(self) -> None:
        if self.stk[-1] == self.minn[-1]:
            self.minn.pop()
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minn[-1]