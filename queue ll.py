class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(data, "inserted into queue.")


    def dequeue(self):
        if self.front is None:
            print("Queue is empty.")
            return

        data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print(data, "deleted from queue.")


    def peek(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            print("Front element:", self.front.data)


    def display(self):
        if self.front is None:
            print("Queue is empty.")
            return

        temp = self.front
        print("Queue elements:", end=" ")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


queue = Queue()

while True:
    print("\n--- QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter element to enqueue: "))
        queue.enqueue(data)

    elif choice == 2:
        queue.dequeue()

    elif choice == 3:
        queue.peek()

    elif choice == 4:
        queue.display()

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
