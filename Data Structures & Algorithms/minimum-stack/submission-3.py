class MinStack:

    def __init__(self):
        self.p = []
        

    def push(self, val: int) -> None:
        if len(self.p) == 0:
            self.p.append((val, val))
        else:
            m = min(val,self.p[-1][1])
            self.p.append((val, m))

    def pop(self) -> None:
        self.p.pop()

    def top(self) -> int:
        return self.p[-1][0]

    def getMin(self) -> int:
        return self.p[-1][1]
        
