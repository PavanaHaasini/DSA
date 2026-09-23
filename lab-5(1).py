# Stack Implementation using Array

class Stack:
    def __init__(self):
        self.stack = []

    # Push operation
    def push(self, data):
        self.stack.append(data)
        print(data, "pushed into stack.")

    # Pop operation
    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow.")
        else:
            data = self.stack.pop()
            print(data, "popped from stack.")

    # Peek operation
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
        else:
            print("Top element:", self.stack[-1])

    # Display stack
    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
        else:
            print("Stack elements:")
            for i in range(len(self.stack) - 1, -1, -1):
                print(self.stack[i])


# Main Program
s = Stack()

while True:
    print("\n========== STACK USING ARRAY ==========")
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
