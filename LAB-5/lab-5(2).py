# Stack Implementation using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "pushed into stack.")

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow.")
        else:
            data = self.top.data
            self.top = self.top.next
            print(data, "popped from stack.")

    # Peek operation
    def peek(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            print("Top element:", self.top.data)

    # Display stack
    def display(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            temp = self.top
            print("Stack elements:")

            while temp is not None:
                print(temp.data)
                temp = temp.next


# Main Program
s = Stack()

while True:
    print("\n======= STACK USING LINKED LIST =======")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    print("=======================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        s.push(data)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")
