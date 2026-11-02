# Hashing using Quadratic Probing

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Insert an element
    def insert(self, key):
        index = key % self.size

        for i in range(self.size):
            pos = (index + i * i) % self.size

            if self.table[pos] is None:
                self.table[pos] = key
                print("Element inserted.")
                return

            if self.table[pos] == key:
                print("Duplicate element.")
                return

        print("No empty position found.")

    # Search an element
    def search(self, key):
        index = key % self.size

        for i in range(self.size):
            pos = (index + i * i) % self.size

            if self.table[pos] is None:
                return False

            if self.table[pos] == key:
                return True

        return False

    # Delete an element
    def delete(self, key):
        index = key % self.size

        for i in range(self.size):
            pos = (index + i * i) % self.size

            if self.table[pos] is None:
                print("Element not found.")
                return

            if self.table[pos] == key:
                self.table[pos] = "DELETED"
                print("Element deleted.")
                return

        print("Element not found.")

    # Display the hash table
    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


# Main Program
size = int(input("Enter hash table size: "))
ht = HashTable(size)

while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        key = int(input("Enter element: "))
        ht.insert(key)

    elif choice == '2':
        key = int(input("Enter element to search: "))
        print("Element found." if ht.search(key)
              else "Element not found.")

    elif choice == '3':
        key = int(input("Enter element to delete: "))
        ht.delete(key)

    elif choice == '4':
        ht.display()

    elif choice == '5':
        break

    else:
        print("Invalid choice.")
