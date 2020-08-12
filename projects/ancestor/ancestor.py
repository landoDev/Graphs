# import sys
# sys.path.append(".")
# from util import Stack
# Build the graph( wait should this be done in the function?)
# I feel like building a class is overthinking it?
# class Graph:
#     def __init__(self):
#         self.vertices = {}

from util import Stack
# stack imported but is the same as everyone else's
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # intialize the nodes
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # set abstracts some conditionals 
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # if both vertex parameters are present, add v2 to v1's set
        # creates an edge between v1 and v2 if they both are
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        # passing optional error from class
        else:
            raise IndexError("Vertex Does not exist!")

    def get_neighbors(self, ancestor):
        return self.vertices[ancestor]

def earliest_ancestor(ancestors, starting_node):
    # need to find the deepest ancestor
    # find the LONGEST/FARTHEST ancestor
    # utilize dfs to find the ancestors

    # build the graph 
    lineage = Graph()
    # add vertex
    # add the edges
    for parent, child in ancestors:
        lineage.add_vertex(parent)
        lineage.add_vertex(child)
    for parent, child in ancestors:
        lineage.add_edge(child, parent)
    
    # initiate a list of paths?
    list_paths = []

    # create an empty stack and push PATH to the Starting vetex ID
    s = Stack()
    s.push([starting_node])
    # create a set to store visited vertices
    visited = set()
    # while stack is not empty
    while s.size() > 0:
        # take path off the top
        path = s.pop()
        # initialize the last vertex
        v = path[- 1]
        # if vertex hasn't been visited
        if v not in visited:
            # add it
            visited.add(v)
            # for each neighbor, append a copied path and push the copy on the stack
            for neighbor in lineage.get_neighbors(v):
                copy_path = list(path)
                copy_path.append(neighbor)
                s.push(copy_path)
        
        list_paths.append(path)
    # print(list_paths)
    if len(list_paths) <= 1:
        return -1
    else:
        longest = []
        eldest = list_paths[-1][-1]

        for bloodline in list_paths:
            # print("bloodline", bloodline[-1])
            # print("eldest", eldest)
            # find the lenght of the bloodline
            length = len(bloodline)
            # is it the longest one in longest?
            if len(longest) < 1:
                longest.append(bloodline)
            for elder_path in longest:
                if len(elder_path) < length:
                    longest = [bloodline]
                elif len(elder_path) == length:
                    longest = longest + [bloodline]

        # print("longest", longest)
        if len(longest) > 1:
            for elder in longest:
                if elder[-1] < eldest:
                    eldest = elder[-1]
        # print(eldest)
        return eldest


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# earliest_ancestor(test_ancestors, 1)
print(earliest_ancestor(test_ancestors, 3))
# if earliest_ancestor == 10:
#     print(True)
# else:
#     print(False)