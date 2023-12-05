import itertools

class Network:

    def __init__(self):
        self.start_node = None
        self.nodes = []

    def get_start_node(self):
        return self.start_node

    def get_node_by_name(self, name):
        for node in self.nodes:
            if(node.get_name() == name):
                return node
        return None
    
    def set_start_node(self):
        for node in self.nodes:
            if(node.get_name() == "AA"):
                self.start_node = node
                return True
        return False
    
    def add_node(self, node):
        if(self.check_node(node)):
            self.nodes.append(node)
            return True
        return False
    
    def check_node(self, node):
        for legit_node in self.nodes:
            if(legit_node.get_name() == node.get_name()):
                return False
        return True
    
    def print_network(self):
        for node in self.nodes:
            print("")
            print(node.get_name())
            print(node.get_flow())
            for successor in node.get_successors():
                print("\t" + successor.get_name())
            print("")

    def get_relevant_nodes(self):
        relevant_nodes = []
        for node in self.nodes:
            if(node.is_relevant()):
                relevant_nodes.append(node)
        return relevant_nodes

    def get_max_released_pressure(self, total_time):
        relevant_nodes = self.get_relevant_nodes()
        print("BEFORE")
        permutations = list(itertools.permutations(relevant_nodes))
        print("NUM PERMUTATIONS", len(permutations))
        max_released_pressure = 0
        for permutation in permutations:
            shortest_times = self.get_shortest_times(permutation)
            released_pressure = self.calculate_released_pressure(permutation, shortest_times, total_time)
            if(max_released_pressure < released_pressure):
                max_released_pressure = released_pressure
        return max_released_pressure

    def get_shortest_times(self, permutation):
        shortest_times = []
        start_node = self.get_start_node()
        for node in permutation:
            shortest_times.append(start_node.shortest_time(node))
            start_node = node
        return shortest_times
    
    def calculate_released_pressure(self, permutation, shortest_times, total_time):
        released_pressure = 0
        for i in range(len(permutation)):
            released_pressure += (total_time - sum(shortest_times[0:i+1])) * permutation[i].get_flow()
        return released_pressure

class Node:

    def __init__(self, name, flow):
        self.name = name
        self.flow = flow
        self.successors = []

    def add_successor(self, successor):
        if(successor.__class__.__name__ == "Node"):
            self.successors.append(successor)
            return True
        return False
    
    def get_successors(self):
        return self.successors
    
    def get_flow(self):
        return self.flow
    
    def get_name(self):
        return self.name
    
    def is_relevant(self):
        return self.flow > 0
    
    def shortest_time(self, goal_node):
        length = 0
        visited_nodes = []
        next_nodes = [self]

        while(True):
            length += 1
            new_next_nodes = []
            for node in next_nodes:
                for successor in node.get_successors():
                    if(not successor in visited_nodes and not successor in next_nodes):
                        new_next_nodes.append(successor)
            visited_nodes = visited_nodes + next_nodes
            next_nodes = new_next_nodes
            if(goal_node in visited_nodes):
                return length
            
    def is_reachable(self, goal_node):
        if(goal_node == self):
            return True
        
        visited_nodes = []
        next_nodes = [self]

        while(len(next_nodes) > 0):
            current_node = next_nodes[0]
            if(current_node == goal_node):
                return True
            visited_nodes.append(current_node)
            next_nodes = next_nodes[1:]
            for successor in current_node.get_successors():
                if(not successor in visited_nodes and not successor in next_nodes):
                    next_nodes.append(successor)
        return False