class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if len(self.stack2) == 0:
            self.stack1.append(x)
        elif len(self.stack1) == 0 and len(self.stack2) != 0:
            self.stack2.append(x)
        else:
            return -1

        

    def pop(self) -> int:
        if len(self.stack1) != 0 and len(self.stack2) == 0:
            for atom in self.stack1[1:]:
                self.stack2.append(atom)
            temp = self.stack1[0]
            self.stack1.clear()
            return temp
        elif len(self.stack1) == 0 and len(self.stack2) != 0:
            for atom in self.stack2[1:]:
                self.stack1.append(atom)
            temp = self.stack2[0]
            self.stack2.clear()
            return temp
        else:
            return -1
        
    def peek(self) -> int:
        if len(self.stack1) != 0 and len(self.stack2) == 0:
            return self.stack1[0]
        elif len(self.stack1) == 0 and len(self.stack2) != 0:
            return self.stack2[0]
        else:
            return -1

    def empty(self) -> bool:
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# 스택 두개로 큐를 구현해야함
# 따라서 스택 둘을  쓰되 하나는 늘 비워둠
# push시 모든 정보를 넣어두는 용도로 하나
# pop시 모든 정보를 하나 빼고 옮기는 용도로 하나
# pop을 실행한 경우 이전 스택은 전부 비움
