from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()
        self.topEl = None   # remember the most recently pushed element

    def push(self, x: int) -> None:
        self.q.append(x)
        self.topEl = x      # the last thing pushed is always the top

    def pop(self) -> int:
        # rotate everything except the last element to the back
        for i in range(len(self.q) - 1):
            self.topEl = self.q.popleft()   # the last one moved becomes the new top
            self.q.append(self.topEl)
        return self.q.popleft()

    def top(self) -> int:
        return self.topEl

    def empty(self) -> bool:
        return len(self.q) == 0

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()