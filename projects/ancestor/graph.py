from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # intialize the nodes
        self.vertices = {}
        self.path = []

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
        # Flip from queue to stack, enqueue to push and dequeue to pop 👍 
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
        # print the vertex
        print(starting_vertex)
        # base case: what are you???
        for neighbor in self.get_neighbors(starting_vertex):
            # This is it... But I don't fully understand
            if neighbor < starting_vertex:
                return
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
        visited = set()

        # while queue is not empty
        while q.size() > 0:
            # dequeue the first PATH
            path = q.dequeue()
            # grab the last vertex from the path
            last_vertex = path[-1]
            # check if the vertex has not been visited (the ability to break out)
            if last_vertex not in visited:
                # is this vertex the target?
                if last_vertex == destination_vertex:
                    # return the path
                    return path
                # mark it as visited
                visited.add(last_vertex)
                # then add a PATH to its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last_vertex):
                    # make a copy of the path
                    copy_path = list(path)
                    # append the neighbor to the back of the path
                    copy_path.append(neighbor)
                    q.enqueue(copy_path)
                
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
        visited = set()
        while s.size() > 0:
            path = s.pop()
            last_vertex = path[- 1]
            if last_vertex not in visited:
                if last_vertex == destination_vertex:
                    return path
                visited.add(last_vertex)
                for neighbor in self.get_neighbors(last_vertex):
                    copy_path = list(path)
                    copy_path.append(neighbor)
                    s.push(copy_path)
       
        return None
    def dfs_recursive(self, starting_vertex, destination_vertex, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        current_path = path
        if path is None:
            current_path = [starting_vertex]
        else:
            current_path = path + [starting_vertex]
        vertex = starting_vertex
        for neighbor in self.get_neighbors(vertex):
            if vertex == destination_vertex:
                return list(path)
            self.dfs_recursive(neighbor, destination_vertex, current_path)