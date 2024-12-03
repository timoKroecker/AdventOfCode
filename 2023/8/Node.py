class Node:

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def get_name(self):
        return self.name

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right
    
    def get_child(self, instruction):
        if(instruction == "L"):
            return self.left
        if(instruction == "R"):
            return self.right
        return None

    def set_left(self, left):
        if self.check_node(left):
            self.left = left
            return True
        return False

    def set_right(self, right):
        if self.check_node(right):
            self.right = right
            return True
        return False

    def check_node(self, element):
        return element.__class__.__name__ == "Node"