# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self,new_data):
        # Create new node
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self,new_data,prev_node):
        if prev_node is Node:
            print("Node must in LinkedList")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self,new_data):
        new_node = Node(new_data)
        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node


if __name__ == '__main__':
    first = LinkedList()
    first.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Linked the nodes
    first.head.next = second
    second.next = third

    # print list data
    print('Created linked list is:')
    first.printList()
    first.push(10)
    print('Created linked list is:')
    first.printList()
    print('Created After list is:')
    first.insertAfter(20,second)
    first.printList()
    print('Created last list is:')
    first.append(30)
    first.printList()

