class MinStack:

    def __init__(self):
        self.st=[]
        self.mini=float("inf")
        

    def push(self, val: int) -> None:
        if not self.st:
            self.mini=val
            self.st.append(val)
        else:
            if val<self.mini:
                self.st.append(2*val-self.mini)
                self.mini=val
            else:
                self.st.append(val)

        

    def pop(self) -> None:
        if not self.st:
            return 
        top=self.st.pop()
        if top<self.mini:
            self.mini=2*self.mini-top


        

    def top(self) -> int:
        if not self.st:
            return None 
        top=self.st[-1]
        if top<self.mini:
            return self.mini
        return top 

        

    def getMin(self) -> int:
        return self.mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()