class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head is None:
            newnode = Node(data)
            self.head = newnode
        else:
            curr = self.head
            newnode = Node(data)
            while curr.next:
                curr = curr.next
            newnode.prev = curr
            curr.next = newnode
            
    
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            curr = self.head
            while curr:
                print(curr.data, end = '<-->')
                curr = curr.next
            print(None)

    def reverse(self):
        if self.head is None:
            print("List is empty")
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            while curr:
                print(curr.data,end='<-->')
                curr = curr.prev
            print(None)

    def insert_at_beginning(self,data):
        if self.head is None:
            print("List is empty")
        else:
            newnode = Node(data)
            curr = self.head
            curr.prev = newnode
            newnode.next = curr
            self.head = newnode

    def insert_at_position(self,index,data):
        if self.head is None:
            print("List is empty")
        else:
            if index == 0:
                self.insert_at_beginning(data)
            else:
                newnode = Node(data)
                curr = self.head
                counter = 0
                while counter!=index:
                    curr = curr.next
                    counter+=1
                newnode.next = curr
                newnode.prev = curr.prev
                curr.prev.next = newnode
                curr.prev = newnode
                


n = DoubleLinkedList()
n.append(12)
n.append(13)
n.append(14)
n.display()
n.insert_at_beginning(10)
n.display()
n.insert_at_position(2,120)
n.display()
