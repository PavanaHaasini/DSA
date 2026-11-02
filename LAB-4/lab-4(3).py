class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def create(self):
        n = int(input("Enter number of nodes: "))
        self.head = None
        self.tail = None

        for i in range(n):
            data = int(input("Enter data: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = self.head
            else:
                new_node.next = self.head
                self.tail.next = new_node
                self.tail = new_node

        print("Circular Linked List created successfully.")

    def insert_beginning(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

        print("Node inserted at beginning.")

    def insert_end(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

        print("Node inserted at end.")

    def insert_position(self):
        position = int(input("Enter position: "))
        data = int(input("Enter data: "))

        if position <= 0:
            print("Invalid position.")
            return

        if self.head is None:
            if position == 1:
                new_node = Node(data)
                self.head = new_node
                self.tail = new_node
                new_node.next = self.head
                print("Node inserted.")
            else:
                print("Invalid position.")
            return

        if position == 1:
            self.insert_beginning()
            return

        temp = self.head

        for i in range(1, position - 1):
            temp = temp.next

            if temp == self.head:
                print("Invalid position.")
                return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

        if temp == self.tail:
            self.tail = new_node

        print("Node inserted.")

    def delete_beginning(self):
        if self.head is None:
            print("Circular Linked List is empty.")
            return

        if self.head == self.tail:
            print("Deleted Value =", self.head.data)
            self.head = None
            self.tail = None
        else:
            print("Deleted Value =", self.head.data)
            self.head = self.head.next
            self.tail.next = self.head

    def delete_end(self):
        if self.head is None:
            print("Circular Linked List is empty.")
            return

        if self.head == self.tail:
            print("Deleted Value =", self.tail.data)
            self.head = None
            self.tail = None
            return

        temp = self.head

        while temp.next != self.tail:
            temp = temp.next

        print("Deleted Value =", self.tail.data)

        temp.next = self.head
        self.tail = temp

    def delete_position(self):
        position = int(input("Enter position: "))

        if self.head is None:
            print("Circular Linked List is empty.")
            return
        if position <= 0:
            print("Invalid position.")
            return
        
        if position == 1:
            self.delete_beginning()
            return

        temp = self.head

        for i in range(1, position - 1):
            temp = temp.next

            if temp == self.head:
                print("Invalid position.")
                return

        if temp.next == self.head:
            print("Invalid position.")
            return

        if temp.next == self.tail:
            print("Deleted Value =", self.tail.data)
            self.tail = temp
            self.tail.next = self.head
        else:
            print("Deleted Value =", temp.next.data)
            temp.next = temp.next.next

    def count(self):
        if self.head is None:
            print("No Linked List")
            return

        count = 0
        temp = self.head

        while True:
            count += 1
            temp = temp.next

            if temp == self.head:
                break

        print("Number of nodes:", count)

    def display(self):
        if self.head is None:
            print("Circular Linked List is empty.")
            return

        temp = self.head

        print("Circular Linked List:")

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(Head)")

    def display_head_tail(self):
        if self.head is None:
            print("Circular Linked List is empty.")
        else:
            print("Head =", self.head.data)
            print("Tail =", self.tail.data)


cll = CircularLinkedList()
while True:
    print("\n----- CIRCULAR LINKED LIST -----")
    print("1. Create a Circular LL")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at specific position")
    print("5. Delete at beginning")
    print("6. Delete at end")
    print("7. Delete at specific position")
    print("8. Count no. of nodes")
    print("9. Traverse / Display the elements")
    print("10. Display Head and Tail")
    print("11. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        cll.create()
    elif choice == 2:
        cll.insert_beginning()
    elif choice == 3:
        cll.insert_end()
    elif choice == 4:
        cll.insert_position()
    elif choice == 5:
        cll.delete_beginning()
    elif choice == 6:
        cll.delete_end()
    elif choice == 7:
        cll.delete_position()
    elif choice == 8:
        cll.count()
    elif choice == 9:
        cll.display()
    elif choice == 10:
        cll.display_head_tail()
    elif choice == 11:
        print("Program exited.")
        break

    else:
        print("Invalid choice. Please try again.")
