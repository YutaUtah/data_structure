class MyStack:
    def __init__(self, size):
        self.size = size
        self.arr = [-1] * size
        self.top = -1 # top is the index where the top element is located

    # check if the stack is empty
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            False

    # push
    def push(self, val):
        # if stack has no storage in the array.
        # size-1 is the index of the last array
        # top is the index of the last stack element
        if self.top == self.size-1:
            return None
        else:
            self.top += 1
            self.arr[self.top] = val

    def pop(self):
        # if the stack is empty
        if self.is_empty():
            return None
        # pop the element located at the top
        e = self.arr[self.top]
        self.arr[self.top] = -1
        self.top -= 1

        return e

    def to_string(self):
        stringfied_data = "[ "
        for i in range(0, self.top + 1):
            stringfied_data += str(self.arr[i]) + " "

        return stringfied_data + "]"


if __name__ == "__main__":
    # create the stack with the size of 6
    my_stack = MyStack(6)

    # push elements
    my_stack.push(6)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(7)
    my_stack.push(9)
    print("top = ", my_stack.top)
    print("current stack: ", my_stack.to_string())

    # pop twice
    x = my_stack.pop()
    y = my_stack.pop()
    if x != None and y != None:
        print("elements extracted:", x, y)
    print("top = ", my_stack.top)
    print("current stack: ", my_stack.to_string())

    # push elements
    my_stack.push(5)
    my_stack.push(8)
    print("top = ", my_stack.top)
    print("current stack: ", my_stack.to_string())