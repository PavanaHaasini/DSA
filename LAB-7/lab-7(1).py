
class BinaryTree:
    def __init__(self):
        self.tree = []

    def insert(self, value):
        self.tree.append(value)
        print("Node inserted successfully.")

    def search(self, value):
        for i in range(len(self.tree)):
            if self.tree[i] == value:
                return i
        return -1

    def delete(self, value):
        index = self.search(value)

        if index == -1:
            print("Node not found.")
        else:
            print("Deleted node:", value)
            self.tree[index] = self.tree[-1]
            self.tree.pop()

    def inorder(self, i=0):
        if i < len(self.tree):
            self.inorder(2 * i + 1)
            print(self.tree[i], end=" ")
            self.inorder(2 * i + 2)

    def preorder(self, i=0):
        if i < len(self.tree):
            print(self.tree[i], end=" ")
            self.preorder(2 * i + 1)
            self.preorder(2 * i + 2)

    def postorder(self, i=0):
        if i < len(self.tree):
            self.postorder(2 * i + 1)
            self.postorder(2 * i + 2)
            print(self.tree[i], end=" ")

    def display(self):
        if not self.tree:
            print("Tree is empty.")
        else:
            print("Array representation:", self.tree)


bt = BinaryTree()

while True:
    print("\n--- Binary Tree Using Array ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Display")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        value = int(input("Enter value: "))
        bt.insert(value)

    elif choice == '2':
        value = int(input("Enter value to delete: "))
        bt.delete(value)

    elif choice == '3':
        value = int(input("Enter value to search: "))
        index = bt.search(value)
        if index != -1:
            print("Node found at index:", index)
        else:
            print("Node not found.")

    elif choice == '4':
        print("Inorder:", end=" ")
        bt.inorder()
        print()

    elif choice == '5':
        print("Preorder:", end=" ")
        bt.preorder()
        print()

    elif choice == '6':
        print("Postorder:", end=" ")
        bt.postorder()
        print()

    elif choice == '7':
        bt.display()

    elif choice == '8':
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")
