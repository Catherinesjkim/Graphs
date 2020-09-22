"""
Given social graph class, given number users that I need to create and number friends each user should have. Key of the user and the user's friends (1 - 3) average 2 friends per user. 10 users max. If you create a new graph, it will have a different sets of friends per user. If

Output: dictionary of friend of friend. Starting node = 1. 1 to 8. 

Mari: first part

"""

import random
import math

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        # id of the last user I added
        self.last_id = 0
        # users will be mapping 
        self.users = {} # {1: User("1"), 2: User("2"), ...}
        self.friendships = {} # adjacency representation {1: {2, 3, 4}, 2: {1}, 3: {1}, 4: {1}} # bi-directional

    # This creates a bi-directional friendshipo
    # use this method in the populate_graph method
    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        # if this, then that friendship already exist, no need to add to it
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            # friendships are bi-directional
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    # use this method in the populate_graph method
    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user so you know how many users there are in the network
        self.users[self.last_id] = User(name) # {1: User("catherine")}
        # friendship is a adjacency list reprentation to an empty set since you don't have a user yet
        self.friendships[self.last_id] = set()
        
    # implement populate_graph and the users should be randomized
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
        for i in range(num_users):
            self.add_user(f"User {i}")
            
        # Add users
        # randomly distribute friendships between these Users
        for i in range(num_users):
            self.add_user(f"User {i}")

        # Create friendships
        # Generate all the possibler friendships and put them into an array
        # 3 users (0, 1, 2)
        possible_friendships = []
        for user_id in self.users:
            # To prevent duplicate friendships create from user_id + 1
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append(user_id, friend_id) # tuple
        # don't dupe friendship, they are bi-directional already. No need to duplicated it
        # [(0, 1), (0, 2), (1, 2)]
        
        # Shuffle the friendship array
        # [(1, 2), (0, 1), (0, 2)] - use python for it - random libray
        random.shuffle(possible_friendships)
        
        # Take the first num_users * avg_friendships / 2 (friendhips are bi-directional) and that will be the friendships for that graph
        for i in range(math.floor(num_users * avg_friendships / 2)):
            friendship = possible_friendships[i]
            # this method will create an edge from 0 to 1
            self.add_friendship(friendship[0], friendship[1])
        
        
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them (connected component component starting from user_id)

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    # created a graph with 10 users, average friendships of 2
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
