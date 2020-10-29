class MyQueue:
    def __init__(self, size):
        self.size = size
        self.arr = [-1] * size
        # head and tail should be 0 as the queue is empty
        self.head = 0
        self.tail = 0

    def enqueue(self, val):
        # if there is no space in the queue
        # if size of array is 10, there are 9 maximum storage p.46
        if (self.tail + 1) % self.size == self.head:
            return None
        # append the val
        self.arr[self.tail] = val
        # update the pointer. if the pointer is at the end, it needs to come at the beginning of the queue
        self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        # if the queue is empty
        if self.head == self.tail:
            return None

        # extract the element
        e = self.arr[self.head]
        self.arr[self.head] = -1

        # update the pointer
        self.head = (self.head + 1) % self.size

        return e


    def to_string(self):
        stringfied_data = "[ "
        index = self.head
        while index != self.tail:
            stringfied_data += str(self.arr[index]) + " "
            if index == self.size - 1:
                index = 0
            else:
                index += 1

        return stringfied_data + "]"


if __name__ == "__main__":
    myqueue = MyQueue(5)
    print(myqueue.to_string())
    myqueue.enqueue(3)
    myqueue.enqueue(1)
    myqueue.enqueue(1)
    myqueue.enqueue(5)
    myqueue.dequeue()
    print(myqueue.to_string())