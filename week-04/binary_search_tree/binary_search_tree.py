class Node:
    def __init__(self,val):
        self.right =None
        self.left = None
        self.val = val
        
        
def insert(root,key):
    if root is None:
        return Node(key)
    if root.val == key:
        return root
    if root.val < key:
        root.right = insert(root.right,key)
    else:
        root.left = insert(root.left,key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=' ')
        inorder(root.right)
        

# Test Case 1: Insert in order
print("Test 1: Insert [15, 12, 13, 11, -1, 0, 101]")
print("Expected: -1 0 11 12 13 15 101")
print("Result: ", end='')
r = Node(15)
r = insert(r, 12)
r = insert(r, 13)
r = insert(r, 11)
r = insert(r, -1)
r = insert(r, 0)
r = insert(r, 101)
inorder(r)
print()

# Test Case 2: Insert reverse order
print("\nTest 2: Insert [7, 6, 5, 4, 3, 2, 1]")
print("Expected: 1 2 3 4 5 6 7")
print("Result: ", end='')
r2 = Node(7)
for val in [6, 5, 4, 3, 2, 1]:
    r2 = insert(r2, val)
inorder(r2)
print()

# Test Case 3: Insert with duplicates
print("\nTest 3: Insert [5, 3, 7, 3, 5]")
print("Expected: 3 5 7")
print("Result: ", end='')
r3 = Node(5)
for val in [3, 7, 3, 5]:
    r3 = insert(r3, val)
inorder(r3)
print()

# Test Case 4: Single node
print("\nTest 4: Insert [42]")
print("Expected: 42")
print("Result: ", end='')
r4 = Node(42)
inorder(r4)
print()

# Test Case 5: Balanced tree
print("\nTest 5: Insert [50, 30, 70, 20, 40, 60, 80]")
print("Expected: 20 30 40 50 60 70 80")
print("Result: ", end='')
r5 = Node(50)
for val in [30, 70, 20, 40, 60, 80]:
    r5 = insert(r5, val)
inorder(r5)
print()
    
        