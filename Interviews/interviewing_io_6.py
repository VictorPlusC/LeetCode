"""
Design a data structure that supports the following three operations. 

1. a constructor that takes a parameter K 
2. add(x) -- inserts the number x 
3. get() -- returns the product of the last K elements inserted 
"""
class LastKProduct():
    def __init__(self, K):
        self.K = K
        self.curr_prod = 1
        self.nums = collections.deque()
        self.zeroes = 0
    
    def __multiply_all(self):
        self.curr_prod = 1
        for val in self.nums:
            self.curr_prod *= val
    
    def add(self, x):
        if x == 0:
            self.zeroes += 1
        self.curr_prod *= x
        self.nums.append(x)
        if len(self.nums) > self.K:
            to_divide = self.nums.popleft()
            if to_divide:
                self.curr_prod /= to_divide
            else:
                self.zeroes -= 1
                if self.zeroes == 0:
                    self.__multiply_all()
    
    def get(self):
        return self.curr_prod