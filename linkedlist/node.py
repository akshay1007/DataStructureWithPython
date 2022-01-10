# Node of Singly Linked List
class Node:
    # constructor
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class LinkedList:
    def __init__(self):
        self.head = None

    # method for setting the data for the node
    def setData(self, data):
        self.data = data

    # method for getting data from the node
    def getData(self):
        return self.data

    # method for setting the next field for the node
    def setNext(self, next):
        self.next = next

    # method for getting the next field for the node
    def getNext(self):
        return self.next

    # return true if node points to next node
    def hasNext(self):
        return self.next is not None

    # get the length of the list
    def listLength(self):
        current = self.head
        count = 0

        while(current):
            count = count + 1
            current = current.getNext()

        return count
    # This function prints contents of linked list

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    # method for inserting the new node at the beginning of the linked list (at the head)
    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.setData(data)
        if self.length == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
        self.length += 1

# Code exution starts here
if __name__ == '__main__':
    # Start with the empty list
    list = LinkedList()
    list.head = Node(1)
    second = Node(2)
    third = Node(3)
    list.head.next = second  # Link first node with second
    second.next = third  # Link second node with the third node
    print(list.listLength())

