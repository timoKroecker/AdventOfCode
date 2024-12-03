class Network:

    def __init__(self):
        self.nodes = []
        self.dictionary = {}

    def get_root(self):
        if len(self.nodes) == 0:
            return None
        for node in self.nodes:
            if(node.get_name() == "AAA"):
                return node

    def get_roots(self):
        roots = []
        for node in self.nodes:
            if(node.get_name()[-1] == "A"):
                roots.append(node)
        return roots

    def get_all_nodes(self):
        return self.nodes
    
    def get_node_by_name(self, name):
        try:
            index = self.dictionary[name]
            return self.nodes[index]
        except:
            return None
    
    def add_node(self, node):
        if(self.check_nodes(node)):
            self.nodes.append(node)
            self.dictionary[node.get_name()] = len(self.nodes) - 1
            return True
        return False
    
    def check_nodes(self, element):
        if(not self.check_node(element)):
            return False
        for node in self.nodes:
            if(node.get_name() == element.get_name()):
                return False
        return True
    
    def check_node(self, element):
        return element.__class__.__name__ == "Node"
    
    def check_root(self, element):
        return self.check_node(element) and element in self.nodes
    
    def get_size(self):
        return len(self.nodes)