

#In-order
class Node:
  def __init__(self, key):
#initializing the left and right children
    self.leftChild = None
    self.rightChild = None
#assign data to the node
    self.data = key

#function for the in order traversal
def InorderTraversal(root):
  if root:
#traversing the left subtree
    InorderTraversal(root.leftChild)
#prints the current node's data
    print(root.data)
    InorderTraversal(root.rightChild)

#creating the binary tree's elements
if __name__ == "__main__":
  root = Node(10)
  root.leftChild = Node(4)
  root.rightChild = Node(90)
  root.leftChild.leftChild = Node(25)
  root.leftChild.rightChild = Node(85)
  root.rightChild.leftChild = Node(65)

  #printing the order of the binary tree (left to root to right)
  print("In order traversal of binary tree is:")
  InorderTraversal(root)

#Pre-order
class Node:
    def __init__(self, key):
#initializing the left and right children
        self.leftChild = None
        self.rightChild = None
        self.data = key

#function for the pre-order traversal
def PreorderTraversal(root):
    if root:
#prints the current node's data
        print(root.data)
        PreorderTraversal(root.leftChild)
        PreorderTraversal(root.rightChild)

if __name__ == "__main__":
#create the binary tree's elements
    root = Node(10)
    root.leftChild = Node(18)
    root.rightChild = Node(100)
    root.leftChild.leftChild = Node(45)
    root.leftChild.rightChild = Node(58)
    root.rightChild.leftChild = Node(86)

#print the preorder traversal of the binary tree (root to the left then the right)
    print("Preorder traversal of binary tree is:")
    PreorderTraversal(root)

#Post-order
class Node:
    def __init__(self, key):
#initializing the left and right children
        self.leftChild = None
        self.rightChild = None
        self.data = key

#function for the post-order traversal
def PostorderTraversal(root):
    if root:
        PostorderTraversal(root.leftChild)
        PostorderTraversal(root.rightChild)
        print(root.data)

if __name__ == "__main__":
#create the binary tree
    root = Node(10)
    root.leftChild = Node(25)
    root.rightChild = Node(39)
    root.leftChild.leftChild = Node(54)
    root.leftChild.rightChild = Node(98)
    root.rightChild.leftChild = Node(150)

#print the postorder traversal of the binary tree (left to the right then the root)
    print("Postorder traversal of binary tree is:")
    PostorderTraversal(root)