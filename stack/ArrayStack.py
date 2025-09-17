class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1
    def isFull(self):
        return self.top == self.capacity - 1
    
    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = item
        else:
            raise IndexError("stack overflow")

    def pop(self):
        if not self.isEmpty():
            item = self.array[self.top]
            self.top -= 1
            return item
        else:
            raise IndexError("stack underflow")
    
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            raise IndexError("stack underflow")
    
    def __str__(self):
        return str(self.array[0:self.top+1])




if __name__ == "__main__":
    s = ArrayStack(10)
    for i in range(1, 6):
        s.push(i)
    print(' push 5회: ', s)

    s.pop()
    print(' pop 1회: ', s)

    print(s.peek())



def checkBrackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        if ch == '{' or ch == '[' or ch == '(':
            stack.push(ch)
        elif ch == '}' or ch == ']' or ch == ')':
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (ch == "}" and left != "{") or (ch == "]" and left != "[") or (ch ==")" and left != "("):
                    return False
                
    return stack.isEmpty()

# Test
s1 = "{ A[(i+1)] = 0;}"
s2 = "if( (i==0) && (j==0)"
s3 = "A[ (i+1]) = 0;"
print(s1, " ---> ", checkBrackets(s1))
print(s2, " ---> ", checkBrackets(s2))
print(s3, " ---> ", checkBrackets(s3))