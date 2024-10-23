
class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" or "operand"
        self.left = left  # Reference to left child
        self.right = right  # Reference to right child
        self.value = value  # Optional value for operand nodes
