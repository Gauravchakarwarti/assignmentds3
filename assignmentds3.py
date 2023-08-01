# 1. Implement Binary tree
# solution:

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)

    def search(self, val):
        return self._search_recursive(self.root, val)

    def _search_recursive(self, node, val):
        if node is None or node.val == val:
            return node
        if val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, node, result):
        if node:
            self._inorder_traversal_recursive(node.left, result)
            result.append(node.val)
            self._inorder_traversal_recursive(node.right, result)

# Example usage:
if __name__ == "__main__":
    binary_tree = BinaryTree()
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(7)
    binary_tree.insert(2)
    binary_tree.insert(4)

    print("Inorder Traversal:", binary_tree.inorder_traversal())

    search_result = binary_tree.search(3)
    if search_result:
        print("Found:", search_result.val)
    else:
        print("Value not found.")


        
#2 Find height of a given tree.
# Solution:

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def tree_height(root):
    if root is None:
        return -1

    left_height = tree_height(root.left)
    right_height = tree_height(root.right)

    return max(left_height, right_height) + 1

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)

    height = tree_height(root)
    print("Height of the binary tree:", height)


# 3 Perform Pre-order, Post-order, In-order traversal.

# Solution:

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def pre_order_traversal(node):
    if node:
        print(node.val, end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.val, end=" ")
        in_order_traversal(node.right)

def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.val, end=" ")
    
if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)

    print("Pre-order Traversal :", end=" ")
    pre_order_traversal(root)
    print()

    print("In-order Traversal :", end=" ")
    in_order_traversal(root)
    print()

    print("Post-order Traversal :", end=" ")
    post_order_traversal(root)
    print()

# 4 Function to print all the leaves in a given binary tree.
# solution:

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_leaves(node):
    if node is None:
        return

    if node.left is None and node.right is None:
        print(node.val, end=" ")
    
    print_leaves(node.left)
    print_leaves(node.right)

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)

    print("Leaf nodes:")
    print_leaves(root)



# 5 Implement BFS (Breath First Search) and DFS (Depth First Search).
# Solution:
    
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def breadth_first_search(root):
    if root is None:
        return[]

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append(node.val)


        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

def depth_first_search_preorder(root):
    if root is None:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result

def depth_first_search_inorder(root):
    if root is None:
        return []

    result = []
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    
    return result

def depth_first_search_postorder(root):
    if root is None:
        return []

    result = []
    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        result.append(stack2.pop().val)

    return result

if __name__ == "__main__":

    root = TreeNode(10)

    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)



    print("BFS:", breadth_first_search(root))

    print("DFS Pre-order:", depth_first_search_preorder(root))

    print("DFS In-order:", depth_first_search_inorder(root))

    print("DFS Post-order:", depth_first_search_postorder(root))

#6 Find sum of all left leaves in a given Binary Tree.

# Solution:


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sum_of_left_leaves(root):
    if root is None:
        return 0

    left_sum = 0

    if root.left and root.left.left is None and root.left.right is None:
        left_sum += root.left.val

    left_sum += sum_of_left_leaves(root.left)
    left_sum += sum_of_left_leaves(root.right)

    return left_sum


if __name__ == "__main__":
  
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)

    
    left_leaves_sum = sum_of_left_leaves(root)
    print("Sum of left leaves:", left_leaves_sum)

        
# 7 Find sum of all nodes of the given perfect binary tree.

# Solution:

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sum_of_all_nodes(root):
    if root is None:
        return 0

    return root.val + sum_of_all_nodes(root.left) + sum_of_all_nodes(root.right)


if __name__ == "__main__":
    
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)

  
    total_sum = sum_of_all_nodes(root)
    print("Sum of all nodes:", total_sum)



# 8 Count subtress that sum up to a given value x in a binary tree.

# Solution:

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_subtrees_with_sum(root, target_sum):
    def dfs(node):
        nonlocal count
        if node is None:
            return 0

        left_sum = dfs(node.left)
        right_sum = dfs(node.right)
        subtree_sum = node.val + left_sum + right_sum

        if subtree_sum == target_sum:
            count += 1

        return subtree_sum
    count = 0
    dfs(root)
    return count

if __name__ == "__main__":

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)

    target_sum = 22
    result = count_subtrees_with_sum(root, target_sum)
    
    if result > 0:
        print("Number of subtrees with sum equal to", target_sum, ":", result)
    else:
        print("No subtrees with sum equal to", target_sum, "found.")


# 9 Find maximum level sum in Binary Tree.

# Solution:
    
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_level_sum(root):
    if root is None:
        return 0

    max_sum = root.val
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_sum = 0

        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        max_sum = max(max_sum, level_sum)

    return max_sum


if __name__ == "__main__":
   
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)

    
    result = max_level_sum(root)
    print("Maximum level sum:", result)



# 10 Print the nodes at odd levels of a tree.

# Solution:

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_nodes_at_odd_levels(root):
    def dfs(node, level):
        if node is None:
            return

        if level % 2 == 1:
            print(node.val, end=" ")

        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 1)


if __name__ == "__main__":
    
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)

    
    print("Nodes at odd levels:")
    print_nodes_at_odd_levels(root)
