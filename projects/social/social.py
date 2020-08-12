class User:
    def __init__(self, name):
        self.name = name

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

        # Create friendships
        # generate all possible friendship combinations, track the list 

        # avoid duplicates by ensuring first num < second num, 
        ## ensures that lowest num is always the first value in tuple

        # shuffle the possible friendships

        # create friendships for the n num of pairs of the list
        # not following why we are doing this formula but it's important
        ## maybe to create an average/range for n?
        # n = num_users * avg_friendships // 2

        # loop through the range of n
            # grab a possible friendship from the list

            # pass the user id and friend_id to add_friendship()

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # key word: SHORTEST => use bfs (bft?)
        # looking for a path output (the shortest this time)
        # look at the simpler logic of earliest ancestor
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # Use what you've already done. Island count most similar?, take a look and pseudocode that?
        # Try an over psuedocode approach
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
