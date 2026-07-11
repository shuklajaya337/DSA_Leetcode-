class MinStack:

    def __init__(self):
        self.st=[]
        self.minval=[]
        

    def push(self, value: int) -> None:
        if not self.st:
            self.st.append(value)
            self.minVal = value

        elif value >= self.minVal:
            self.st.append(value)

        else:
            self.st.append(2 * value - self.minVal)
            self.minVal = value

    def pop(self) -> None:
        if not self.st:
            return
        x = self.st[-1]
        self.st.pop()        

        if x < self.minVal:
            self.minVal = 2 * self.minVal - x
        

    def top(self) -> int:
        if not self.st:
            return

        x = self.st[-1]

        if x >= self.minVal:
            return x
        else:
            return self.minVal
              

    def getMin(self) -> int:
        return self.minVal
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()