
def enqueue(queue, item):
    queue.append(item)
    print("Element inserted successfully.")

def dequeue(queue):
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Deleted element:", queue.pop(0))

def peek(queue):
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Front element:", queue[0])

def display(queue):
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Queue elements:", queue)

queue = []

while True:
    print("\n--- Queue Using Array ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = int(input("Enter element to insert: "))
        enqueue(queue, item)
    elif choice == '2':
        dequeue(queue)
    elif choice == '3':
        peek(queue)
    elif choice == '4':
        display(queue)
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
