# Binary Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Inorder Traversal
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Preorder Traversal
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder Traversal
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Function to calculate height of the tree
def height(root):
    if root is None:
        return -1
    return max(height(root.left), height(root.right)) + 1


# Creating the binary tree using the given numbers
root = Node(23)

root.left = Node(5)
root.right = Node(18)

root.left.left = Node(70)
root.left.right = Node(10)

root.left.right.left = Node(8)

root.right.left = Node(15)
root.right.left.right = Node(12)


# Display results
print("Inorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)

print("\nHeight of the tree:", height(root))
