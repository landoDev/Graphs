# import sys
# sys.path.append(".")
# from util import Stack
# Build the graph( wait should this be done in the function?)
# I feel like building a class is overthinking it?
# class Graph:
#     def __init__(self):
#         self.vertices = {}

def earliest_ancestor(ancestors, starting_node):
    pass
    # need to find the deepest ancestor
    # find the LONGEST/FARTHEST ancestor
    # utilize dfs to find the ancestor

    # copy and pasted from graph
    # s = Stack()
    # s.push([starting_node])
    # visited = set()
    # while s.size() > 0:
    #     path = s.pop()
    #     last_vertex = path[- 1]
    #     if last_vertex not in visited:
    #         if last_vertex == destination_vertex:
    #             return path
    #         visited.add(last_vertex)
    #         for neighbor in self.get_neighbors(last_vertex):
    #             copy_path = list(path)
    #             copy_path.append(neighbor)
    #             s.push(copy_path)
    
    # return None    

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(test_ancestors, 1)