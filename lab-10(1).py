# Hashing using Separate Chaining

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Insert an element
    def insert(self, key):
        index = key % self.size

        if key not in self.table[index]:
            self.table[index].append(key)
            print("Element inserted.")
        else:
            print("Duplicate element.")

    # Search an element
    def search(self, key):
        index = key % self.size
        return key in self.table[index]

    # Delete an element
    def delete(self, key):
        index = key % self.size

        if key in self.table[index]:
            self.table[index].remove(key)
            print("Element deleted.")
        else:
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
