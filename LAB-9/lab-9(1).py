
# AVL Tree Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Right Rotation
    def right_rotate(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))
        x.height = 1 + max(self.height(x.left),
                           self.height(x.right))

        return x

    # Left Rotation
    def left_rotate(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = 1 + max(self.height(x.left),
                           self.height(x.right))
        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))

        return y

    # Insert a node
    def insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.data:
            root.left = self.insert(root.left, value)
        elif value > root.data:
            root.right = self.insert(root.right, value)
        else:
            return root

        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))

        balance = self.balance_factor(root)

        # LL Case
        if balance > 1 and value < root.left.data:
            return self.right_rotate(root)

        # RR Case
        if balance < -1 and value > root.right.data:
            return self.left_rotate(root)

        # LR Case
        if balance > 1 and value > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL Case
        if balance < -1 and value < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Search for a node
    def search(self, root, value):
        if root is None:
            return False

        if root.data == value:
            return True

        if value < root.data:
            return self.search(root.left, value)

        return self.search(root.right, value)

    # Find minimum value
    def min_value(self, node):
        while node.left is not None:
            node = node.left
        return node

    # Delete a node
    def delete(self, root, value):
        if root is None:
            return root

        if value < root.data:
            root.left = self.delete(root.left, value)

        elif value > root.data:
            root.right = self.delete(root.right, value)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.min_value(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        if root is None:
            return root

        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))

        balance = self.balance_factor(root)

        # LL Case
        if balance > 1 and self.balance_factor(root.left) >= 0:
            return self.right_rotate(root)

        # LR Case
        if balance > 1 and self.balance_factor(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RR Case
        if balance < -1 and self.balance_factor(root.right) <= 0:
            return self.left_rotate(root)

        # RL Case
        if balance < -1 and self.balance_factor(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Inorder Traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Preorder Traversal
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder Traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # Display the tree
    def display(self, root, level=0):
        if root:
            self.display(root.right, level + 1)
            print("    " * level + str(root.data))
            self.display(root.left, level + 1)


# Main Program
avl = AVLTree()
root = None

while True:
    print("\n--- AVL Tree Operations ---")
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

        if avl.search(root, value):
            print("Duplicate values are not allowed.")
        else:
            root = avl.insert(root, value)
            print("Node inserted.")

    elif choice == '2':
        value = int(input("Enter value to delete: "))

        if avl.search(root, value):
            root = avl.delete(root, value)
            print("Node deleted.")
        else:
            print("Node not found.")

    elif choice == '3':
        value = int(input("Enter value to search: "))

        if avl.search(root, value):
            print("Node found.")
        else:
            print("Node not found.")

    elif choice == '4':
        print("Inorder traversal:", end=" ")
        avl.inorder(root)
        print()

    elif choice == '5':
        print("Preorder traversal:", end=" ")
        avl.preorder(root)
        print()

    elif choice == '6':
        print("Postorder traversal:", end=" ")
        avl.postorder(root)
        print()

    elif choice == '7':
        if root is None:
            print("Tree is empty.")
        else:
            print("AVL Tree:")
            avl.display(root)

    elif choice == '8':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 8.")
