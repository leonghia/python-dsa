class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def get(self, index):
        if (index < 0 or index >= self.length):
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp  
        

    def append(self, value):
        new_node = Node(value)
        if (self.head is None and self.tail is None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if (self.length == 0):
            return None
        elif(self.length == 1):
            temp = self.head
            self.head = self.tail = None
            self.length == 0
            return temp
        else:
            temp = self.head
            secondLast = self.head
            last = self.tail
            while (temp.next):
                secondLast = temp
                temp = temp.next
            secondLast.next = None
            self.tail = secondLast
            self.length -= 1
            return last

    def pop_first(self):
        if (self.length == 0):
            self.length -= 1
            return None
        if (self.length == 1):
            temp = self.head
            self.head = self.tail = None
            temp.next = None
            self.length -= 1
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if (self.length == 1):
                self.tail = self.head
            return temp

    def prepend(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node  
        self.length += 1
        return True     
    
my_linked_list = LinkedList(4)
