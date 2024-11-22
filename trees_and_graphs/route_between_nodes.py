import unittest

# Route Between Nodes: 
# Given a directed graph, design an algorithm to find out whether 
# there is a route between two nodes.

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, from_node, to_node):
        if from_node not in self.adjacency_list:
            self.adjacency_list[from_node] = []
        self.adjacency_list[from_node].append(to_node)

    def has_path(self, start, end):
        visited = set()
        return self._dfs(start, end, visited)

    def _dfs(self, current, end, visited):
        if current == end:
            return True
        if current in visited:
            return False
        
        visited.add(current)

        for neighbor in self.adjacency_list.get(current, []):
            if self._dfs(neighbor, end, visited):
                return True
        
        return False


# Unit Tests
import unittest

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        # Creating a sample directed graph
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 2)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(2, 3)
        self.graph.add_edge(3, 4)

    def test_path_exists(self):
        # Test path from 0 to 4
        self.assertTrue(self.graph.has_path(0, 4))

    def test_path_does_not_exist(self):
        # Test path from 4 to 0 (which should not exist)
        self.assertFalse(self.graph.has_path(4, 0))

    def test_direct_connection(self):
        # Test direct connection from 0 to 1
        self.assertTrue(self.graph.has_path(0, 1))

    def test_no_edges(self):
        empty_graph = Graph()
        # Test path in an empty graph
        self.assertFalse(empty_graph.has_path(0, 1))

if __name__ == '__main__':
    unittest.main()