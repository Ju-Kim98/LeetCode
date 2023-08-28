class MyStack:

    def __init__(self):
        self.q = deque()    #create an empty deque(q)

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())    #remove an element from the left end of the deque(popleft) and append it back to the right end
            
    def pop(self) -> int:
        return self.q.popleft()     #remove and return the element from the left end of the q

    def top(self) -> int:
        return self.q[0]        #return element at the left end of q w/o removing it

    def empty(self) -> bool:
        return len(self.q) == 0     #check if the length of the q is equal to 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


"""
#Approch w/ two queues

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        popped_val = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1

        return popped_val
        
    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        top_val = self.q1[0]
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

        return top_val

    def empty(self) -> bool:
        return len(self.q1) == 0
"""






