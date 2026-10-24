
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            print("Node inserted successfully.")
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = new_node
                break
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                break
            else:
                queue.append(current.right)

        print("Node inserted successfully.")

    def search(self, value):
        if self.root is None:
            return False

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.data == value:
                return True

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return False

    def delete(self, value):
        if self.root is None:
            print("Tree is empty.")
            return

        queue = [(self.root, None, None)]
        target = None
        last = None

        while queue:
            current, parent, side = queue.pop(0)
            last = (current, parent, side)

            if current.data == value and target is None:
                target = current

            if current.left:
                queue.append((current.left, current, "left"))

            if current.right:
                queue.append((current.right, current, "right"))

        if target is None:
            print("Node not found.")
            return

        last_node, parent, side = last
        target.data = last_node.data

        if parent is None:
            self.root = None
        elif side == "left":
            parent.left = None
        else:
            parent.right = None

        print("Node deleted successfully.")

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def display(self):
        if self.root is None:
            print("Tree is empty.")
        else:
            print("Tree elements (level order):", end=" ")
            queue = [self.root]

            while queue:
                current = queue.pop(0)
                print(current.data, end=" ")

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

            print()


bt = BinaryTree()

while True:
    print("\n--- Binary Tree Using Linked List ---")
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
        if bt.search(value):
            print("Node found.")
        else:
            print("Node not found.")

    elif choice == '4':
        print("Inorder:", end=" ")
        bt.inorder(bt.root)
        print()

    elif choice == '5':
        print("Preorder:", end=" ")
        bt.preorder(bt.root)
        print()

    elif choice == '6':
        print("Postorder:", end=" ")
        bt.postorder(bt.root)
        print()

    elif choice == '7':
        bt.display()

    elif choice == '8':
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")
