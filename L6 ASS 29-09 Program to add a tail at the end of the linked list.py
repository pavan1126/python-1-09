#A.pavan kumar 121910313047
# Program to add a tail at the end of the linked list


# Defining the Node class
class Node:
    def __init__(self,data): # Constructor for Node class
        self.data = data
        self.next = None

# Defining the Linked List class
class LinkedList:
    def __init__(self): # Constrctor for LinkedList class
        self.head = None

    # Method to append data
    def append(self,data):
        new_node = Node(data)
        # If head is empty
        if self.head is None:
            self.head = new_node
            return
        # If head is not empty
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
    
    # Method to print linked list
    def print_list(self):
        cur = self.head
        while cur:
            # Traversing through each element and printing it
            print(cur.data)
            cur = cur.next

    # Method to add node at the end of the linked list
    def add_last(self,data):
        new_node = Node(data)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

ll = LinkedList() # Creating a linked list
# Appending data to it
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

# Prninting the current linked list
print("The Current Linked List is : ")
ll.print_list()

# Adding new element at the end
n = input("Enter the tail of the Linked List : ")
ll.add_last(n)

# Prninting the updated linked list
print("The Updated Linked List is : ")
ll.print_list()
