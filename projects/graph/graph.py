"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # intialize the nodes
        self.vertices = {}
        self.stack = Stack()
        self.visited = set()

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

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0: 
            vertex = q.dequeue()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex) 
                for neighbor in self.get_neighbors(vertex):
                    q.enqueue(neighbor)
       

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Flip from queue to stack, enqueue to push and dequeue ot pop 👍 
        s = Stack()
        s.push(starting_vertex)
        
        visited = set()
        while s.size() > 0:
            vertex = s.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex) 
                for neighbor in self.get_neighbors(vertex):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        self.stack.push(starting_vertex)
        if self.stack.size() < 1:
            return
        else:
            vertex = self.stack.pop()
            print(vertex)
            if vertex not in self.visited:
                self.visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    self.dft_recursive(neighbor)
        
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # ALMOST the same, difference is that if you find the target id STOP traversing
        # Another big difference is that you will store the path 
        # create an empty queue and enqueue PATH to the Starting vetex ID
        q = Queue()
        # q.enqueue([starting_vertex_id]) # making it into a list
        q.enqueue([starting_vertex])
        # create a set to store visited vertices
        vistied = set()
        # while queue is not empty
        while q.size() > 0:
            # dequeue the first PATH
            path = q.dequeue()
            # grab the last vertex from the path
            last_vertex = path[-1]
            # check if the vertex has not been visited (the ability to break out)
            print(last_vertex)
            if last_vertex not in vistied:
                # is this vertex the target?
                if last_vertex == destination_vertex:
                    # return the path
                    return path
                # mark it as visited
                vistied.add(last_vertex)
                # then add a PATH to its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last_vertex):
                    # make a copy of the path
                    copy_path = path
                    # append the neighbor to the back of the path
                    copy_path.append(neighbor)
        # return None
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
    
        s.push([starting_vertex])

        vistied = set()
  
        while s.size() > 0:
     
            path = s.pop()
     
            last_vertex = path[- 1]
            print(last_vertex)

            if last_vertex not in vistied:
         
                if last_vertex == destination_vertex:
                  
                    return path
            
                vistied.add(last_vertex)
   
                for neighbor in self.get_neighbors(path):
                   
                    copy_path = path
                    
                    copy_path.append(neighbor)
       
        return None
    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
