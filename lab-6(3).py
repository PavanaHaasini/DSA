
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full.")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        print("Element inserted successfully.")

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty.")
            return

        print("Deleted element:", self.queue[self.front])

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def peek(self):
        if self.front == -1:
            print("Queue is empty.")
        else:
            print("Front element:", self.queue[self.front])

    def display(self):
        if self.front == -1:
            print("Queue is empty.")
            return

        print("Queue elements:", end=" ")
        i = self.front

        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

size = int(input("Enter queue size: "))

if size <= 0:
    print("Queue size must be positive.")
else:
    q = CircularQueue(size)

    while True:
        print("\n--- Circular Queue ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = int(input("Enter element to insert: "))
            q.enqueue(item)
        elif choice == '2':
            q.dequeue()
        elif choice == '3':
            q.peek()
        elif choice == '4':
            q.display()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")
