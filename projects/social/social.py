import random

class User:
    def __init__(self, name):
        self.name = name

# if this gets too deep, pull this into it's own file and import it
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # loop through the range from 0 to the num of users
        for i in range(0, num_users):
            self.add_user(f"User{i}")

        # Create friendships
        # generate all possible friendship combinations, track the list 
        possible_friends = []

        # avoid duplicates by ensuring first num < second num, 
        # loop through users and 
        for user_id in self.users:
            #  for each user id
            ## ensures that lowest num is always the first value in tuple
            for friend_id in range(user_id + 1, self.last_id + 1):
                # append the next user to the possible friends
                possible_friends.append((user_id, friend_id))
        
        # shuffle the possible friendships
        random.shuffle(possible_friends)

        # create friendships for the n num of pairs of the list
        # not following why we are doing this formula but it's important
        ## maybe to create an average/range for n?
        n = num_users * avg_friendships // 2
        # loop through the range of n
        for i in range(n):
            # grab a possible friendship from the list
            friendship = possible_friends[i]
            user_id, friend_id = friendship
            # pass the user id and friend_id to add_friendship()
            self.add_friendship(user_id, friend_id)
    

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
       
        # key word: SHORTEST => use bfs (bft?)
        # looking for a path output (the shortest this time)
        # create an empty queue and enqueue PATH to the Starting vetex ID
        q = Queue()
        # q.enqueue([]) # making it into a list
        q.enqueue([user_id])

        # create a set to store visited vertices
        # key probably needs to be each of the users friends with the value being the list of paths
        ## or value needs to be the shortest path
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
   
        # while queue is not empty
        while q.size() > 0:
            # dequeue the first PATH (value)
            value = q.dequeue()
            # grab the last key from the path
            key = value[-1]
            # check if the key has not been visited (the ability to break out)
            if key not in visited:
                # mark it as visited
                print(self.friendships[key])
                visited[key] = list(self.friendships[key])
                # then add a PATH (value) to its neighbors to the back of the queue
                # print("friendships", self.friendships)
                # print("value", value)
                # print("visited", visited)
                # need to add the value of the key's neighbors
                for friend in visited[key]:
                #     # make a copy of the path
                    value_copy = list(value)
                    # append the neighbor to the back of the path
                    value_copy.append(friend)
                    q.enqueue(value_copy)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
