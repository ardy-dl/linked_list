class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail= None
        self.count = 0

    def append(self, data):
        if not isinstance(data, (int, str)):
            raise ValueError("Data should be of type int or str")

        if self.count >= 50:
            raise ValueError("Cannot add more than 50 nodes to the list")

        if not -100 <= data <= 100:
            raise ValueError("Node value should be in the range [-100,100]")

        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.count += 1

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
    
    def merge(self, other):
        merged = LinkedList()

        current1 = self.head
        current2 = other.head

        while current1 and current2:
            if current1.data < current2.data:
                merged.append(current1.data)
                current1 = current1.next
            else:
                merged.append(current2.data)
                current2 = current2.next

        while current1:
            merged.append(current1.data)
            current1 = current1.next

        while current2:
            merged.append(current2.data)
            current2 = current2.next

        return merged

    def printLinkedList(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("X")

#example usage
list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(4)

list2 = LinkedList()
list2.append(1)
list2.append(3)
list2.append(4)

merged = list1.merge(list2)
merged.printLinkedList()