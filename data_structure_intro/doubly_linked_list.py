# example element
class MyElement:
    def __init__(self, val):
        self.val = val
        self.prev = None  # pointer for the previous element
        self.next = None  # pointer for the next element

    # converting element information to string
    def to_string(self):
        str_prev = "None"
        str_next = "None"
        if self.prev != None:
            str_prev = str(self.prev.val)
        if self.next != None:
            str_next = str(self.next.val)

        return "(" + str(self.val) + ", " + str_prev + ", " + str_next + ")"


# create doubly linked list
class MyDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, element):
        # if the list is empty append at the beginning of the list
        if self.head == None:
            self.head = element
            self.tail = element
        else:
            self.tail.next = element
            element.prev = self.tail
            self.tail = element

    def get(self, index):
        ptr = self.head
        for i in range(0, index):
            ptr = ptr.next

        return ptr

    def insert(self, index, element):
        # get the element where you want to insert
        ptr = self.get(index)

        # insert the element
        if ptr == None:
            # insert at the tail
            self.append(element)
        else:
            element.prev = ptr.prev
            element.next = ptr
            # this means that the element that ptr is indicating is at the beginning of the linked list
            if ptr.prev == None:
                self.head = element
            else:
                ptr.prev.next = element
            ptr.prev = element

    def delete(self, element):
        # if element is the first one
        if element.prev == None:
            self.head = element.next
        else:
            element.prev.next = element.next
        if element.next == None:
            self.tail = element.prev
        else:
            element.next.prev = element.prev


    def to_string(self):
        stringfied_data = "[ "
        ptr = self.head
        while ptr != None:
            stringfied_data += str(ptr.val) + " "
            ptr = ptr.next

        return stringfied_data + "]"




if __name__ == "__main__":
    # create empty doubly linked list
    my_list = MyDoublyLinkedList()

    # append 5 elements in the list
    my_list.append(MyElement(6))
    my_list.append(MyElement(2))
    my_list.append(MyElement(3))
    my_list.append(MyElement(7))
    my_list.append(MyElement(9))
    print("初期値: ", my_list.to_string())
    print("my_list[2] = ", my_list.get(2).val)

