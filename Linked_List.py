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
        
    def set_value(self, index, value):
        temp = self.get(index)
        if (temp):
            temp.value = value
            return True
        return False

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
    
    def insert(self, index, value):
        if (index < 0 or index > self.length):
            return False
        if (index == 0):
            return self.prepend(value)
        if (index == self.length):
            return self.append(value)
        new_node = Node(value)
        prev = self.get(index - 1)
        next = prev.next
        prev.next = new_node
        new_node.next = next
        self.length += 1
        return True

    def remove(self, index):
        if (index < 0 or index >= self.length):
            return None
        if (index == 0):
            return self.pop_first()
        if (index == self.length - 1):
            return self.pop()
        prev = self.get(index - 1)
        item_to_be_deleted = prev.next
        prev.next = item_to_be_deleted.next
        item_to_be_deleted.next = None
        self.length -= 1
        return item_to_be_deleted

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.reverse()

my_linked_list.print_list()