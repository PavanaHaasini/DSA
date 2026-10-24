# Binary Search Tree (BST) Using Array

class ArrayBST:
    def __init__(self):
        self.tree = []

    # Insert a node
    def insert(self, value, i=0):
        if i >= len(self.tree):
            self.tree.extend([None] * (i + 1 - len(self.tree)))

        if self.tree[i] is None:
            self.tree[i] = value
            return True

        elif value < self.tree[i]:
            return self.insert(value, 2 * i + 1)

        elif value > self.tree[i]:
            return self.insert(value, 2 * i + 2)

        else:
            return False

    # Search for a node
    def search(self, value, i=0):
        if i >= len(self.tree) or self.tree[i] is None:
            return False

        if self.tree[i] == value:
            return True

        if value < self.tree[i]:
            return self.search(value, 2 * i + 1)

        return self.search(value, 2 * i + 2)

    # Inorder traversal
    def inorder(self, i=0):
        if i < len(self.tree) and self.tree[i] is not None:
            self.inorder(2 * i + 1)
            print(self.tree[i], end=" ")
            self.inorder(2 * i + 2)

    # Preorder traversal
    def preorder(self, i=0):
        if i < len(self.tree) and self.tree[i] is not None:
            print(self.tree[i], end=" ")
            self.preorder(2 * i + 1)
            self.preorder(2 * i + 2)

    # Postorder traversal
    def postorder(self, i=0):
        if i < len(self.tree) and self.tree[i] is not None:
            self.postorder(2 * i + 1)
            self.postorder(2 * i + 2)
            print(self.tree[i], end=" ")

    # Delete a subtree and shift its nodes
    def delete_subtree(self, i):
        if i >= len(self.tree) or self.tree[i] is None:
            return

        self.delete_subtree(2 * i + 1)
        self.delete_subtree(2 * i + 2)
        self.tree[i] = None

    # Delete a node
    def delete(self, value, i=0):
        if i >= len(self.tree) or self.tree[i] is None:
            return False

        if value < self.tree[i]:
            return self.delete(value, 2 * i + 1)

        elif value > self.tree[i]:
            return self.delete(value, 2 * i + 2)

        left = 2 * i + 1
        right = 2 * i + 2

        # Node has no children
        if ((left >= len(self.tree) or self.tree[left] is None)
                and (right >= len(self.tree)
                     or self.tree[right] is None)):
            self.tree[i] = None

        # Node has only a right child
        elif left >= len(self.tree) or self.tree[left] is None:
            self.tree[i] = self.tree[right]
            self.delete_subtree(right)

        # Node has only a left child
        elif right >= len(self.tree) or self.tree[right] is None:
            self.tree[i] = self.tree[left]
            self.delete_subtree(left)

        # Node has two children
        else:
            successor = right

            while (2 * successor + 1 < len(self.tree)
                   and self.tree[2 * successor + 1] is not None):
                successor = 2 * successor + 1

            successor_value = self.tree[successor]
            self.delete(successor_value, i)
            self.tree[i] = successor_value

        return True

    # Display the array and tree structure
    def display(self):
        if not self.tree or all(x is None for x in self.tree):
            print("Tree is empty.")
            return

        last = len(self.tree)

        while last > 0 and self.tree[last - 1] is None:
            last -= 1

        print("Array representation:", self.tree[:last])
        print("\nBinary Search Tree:")
        self.display_tree(0)

    # Display the tree sideways
    def display_tree(self, i, level=0):
        if i >= len(self.tree) or self.tree[i] is None:
            return

        self.display_tree(2 * i + 2, level + 1)
        print("    " * level + str(self.tree[i]))
        self.display_tree(2 * i + 1, level + 1)


# Main program
bst = ArrayBST()

while True:
    print("\n--- BST Using Array ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder")
    print("5. Preorder")
    print("6. Postorder")
    print("7. Display")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        value = int(input("Enter value: "))

        if bst.insert(value):
            print("Node inserted.")
        else:
            print("Duplicate values are not allowed.")

    elif choice == '2':
        value = int(input("Enter value to delete: "))

        if bst.delete(value):
            print("Node deleted.")
        else:
            print("Node not found.")

    elif choice == '3':
        value = int(input("Enter value to search: "))

        if bst.search(value):
            print("Node found.")
        else:
            print("Node not found.")

    elif choice == '4':
        print("Inorder traversal:", end=" ")
        bst.inorder()
        print()

    elif choice == '5':
        print("Preorder traversal:", end=" ")
        bst.preorder()
        print()

    elif choice == '6':
        print("Postorder traversal:", end=" ")
        bst.postorder()
        print()

    elif choice == '7':
        bst.display()

    elif choice == '8':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 8,.")
