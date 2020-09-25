"""
Given social graph class, given number users that I need to create and number friends each user should have. Key of the user and the user's friends (1 - 3) average 2 friends per user. 10 users max. If you create a new graph, it will have a different sets of friends per user

Output: dictionary of friend of friend. Starting node = 1 (1 to 8) 

"""

import random

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
    

class User:
    # we can add users into the graph
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        # id of the last user I added
        self.last_id = 0
        # users will be mapping - 2 empthy dictionaries
        # maps IDs to User objects (lookup table for User Objects given IDs)
        self.users = {} # {1: User("1"), 2: User("2"), ...}
        # Adjacency list - the way to represent my graph
        # Maps user_ids to a list of other users (who are their friends)
        self.friendships = {} # adjacency representation {1: {2, 3, 4}, 2: {1}, 3: {1}, 4: {1}} # bi-directional


    # This creates a bi-directional friendshipo
    # use this method in the populate_graph method
    # not suer if add_friendship fn succeeded --> add_friendship_linear()
    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        # error checking
        if user_id == friend_id:
            # you can't be friends with yourself
            print("WARNING: You cannot be friends with yourself")
        # if this, then that friendship already exists, no need to add to it
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            
        # otherwise, add 
        else:
            # friendships are bi-directional connections
            self.friendships[user_id].add(friend_id) # the direction one way
            self.friendships[friend_id].add(user_id) # the corresponding ID to the friend adjacency list


    # use this method in the populate_graph method
    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        # every time there's a new user, we give the next sequential ID
        self.last_id += 1  # automatically increment the ID to assign the new user so you know how many users there are in the network
        self.users[self.last_id] = User(name) # {1: User("catherine")}
        # friendship is a adjacency list reprentation to an empty set since you don't have a user yet
        # Most important part because we are going to add the vertex into the adjacency list
        self.friendships[self.last_id] = set() # instantiate an empty set because we just added a new individua/vertex and there are no edges yet. Any new individual/user will be a vertex, edges are friendships

   
    """
    Takes a number of users and an average/mean number of friendships
    as arguments

    Creates that number of users and a randomly distributed friendships
    between those users

    The number of users must be greater than the average number of friendships
    
    Runtime: n is num_users or avg_friendships or both
    
    """
    # implement populate_graph and the users should be randomized
    # Runtime: O(n^2) == O(users^2) because there are double for loops
    #                        n          m
    def populate_graph(self, num_users, avg_friendships):
        # Reset graph - set everything back to normal multiple times
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!! IMPLEMENT ME - #1 Generating Users and Friendships & Populate the Graph - Done
        # Add users before creating a friendship
        # randomly distribute friendships between these Users
        for i in range(0, num_users): # runtime: O(n) - O(num_users)
            self.add_user(f"User {i+1}") # you will not care about the name in this case
            
        # Create friendships - random distribution of friendship but not too many either (average 2)
        # Generate ALL possible friendships - and put them into an array - pick out the average friendship per user
        # Avoid duplicate friendships - using double for loops - only consider the ones that are further away from you
        possible_friendships = []
        # first loop: starts at first value and goes all the way
        for user_id in self.users: # First loop runtime: O(n)
            # second loop: start at the next value after the first loop + 1
            # how many times do we have to go until the last user? len(self.users.keys()) + 1
            # Second loop runtime: O(n-1), O(n-2), O(n-3), ... --> 0(1) = O(n) ---> Total: O(n^2)
            for friend_id in range(user_id + 1, len(self.users.keys()) + 1):
                # user_id == user_id_2 cannot happen - optimization
                # if friendship between user_id and user_id_2 already exists
                # don't add friendship between user_id_2 and user_id
                possible_friendships.append((user_id, friend_id)) # tuple
        
        # Randomly selected X friendships
        # the formulat for X is num_users * avg_friendships // 2
        # shuffle the entire array of possible friendships and pick X elements from it
        random.shuffle(possible_friendships)
        # Take the first num_users * avg_friendships // 2 (friendhips are bi-directional) and that will be the friendships for that graph
        num_friendships = num_users * avg_friendships // 2
        
        # Select the first num_users * avg_friendships
        # We / 2 because a friendship is a bi-directional edge (we're essentially adding 2 edges)
        for i in range(0, num_friendships): # Runtime: O(n * m / 2) - if m = m --> O(n^2 / 2); m = friendships
            friendship = possible_friendships[i]
            # this method will create an edge from 0 to 1
            self.add_friendship(friendship[0], friendship[1])
            
    # Runtime: O(n) - n is target_friendships - optimazing 
    def populate_graph_linear(self, num_users, avg_friendships):
        # Keep randomly making friendships until we've made the right amount
        # randomly select 2 vertices to become friends
        # if it's a success, then increment number of friendships made
        # else try again
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        
        for i in range(0, num_users):
            self.add_user(f'User {i}')
            
        target_friendships = num_users * avg_friendships
        total_friendships = 0
        collisions = 0
        while total_friendships < target_friendships:
            # 2 vertices - last_id (how many users I have)
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if self.add_friendship_linear(user_id, friend_id):
                # if succeeded, increment by 2
                total_friendships += 2
            # if that increment of friendship does not succeed due to collisions,
            else:
                collisions += 1
        print(f"collisions: {collisions}")
        
            
    # returns true if making friendship was a success
    def add_friendship_linear(self, user_id, friend_id):
        # if you are friends with yourself, don't add that friendship
        if user_id == friend_id:
            return False
        # if any of the below is true, we don't wanna make a friendship if it already exists,
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # then return false
            return False
        else:
            self.friendships[user_id].add(friend_id) # add friendships to the adjacency list
            self.friendships[friend_id].add(user_id)
            return True
        
        
    """
    Takes a user's user_id as an argument - how broad is my social network?

    Returns a dictionary containing every user in that user's
    extended network with the shortest friendship path between them (connected component component starting from user_id)
    
    Hint 1: what graph search guarantees the shortest friendship path? Breadth First Traversal - to get through every single node, until we can't do it any more vs. BFSearch - with a target in mind
    
    Hint 2: Instead of using a set to mark users as visited, you could use a dictionary. Similar to sets, checking if something is in a dictionary runs in O(1) time. If the visited user is the key, what would the value be? 

    The key is the friend's ID and the value is the path.
    """
    # hit every connected user ID and the path to it using BFT - shortest path
    # instead of saying I visited 2, add more info into it (key:value pair)
    def get_all_social_paths(self, user_id):    
        # !!!! IMPLEMENT ME - #2 Degrees of Separation - Done
        # Create a Queue
        # Create a set of visited (previously seen) Vertices
        queue = Queue()
        # Create a Dictionary of visited (previously seen) Vertices
        visited = {
            # Key: Value
            # 3: {1, 3}
            # 2: {1, 2}
            # 4: {1, 2, 4}
            # 5: {1, 3, 5}
        }  # Note that this is a dictionary (key value store), not a set
        # Add first user_id to the Queue as a path
        queue.enqueue([user_id])
        
        # While the Queue is not empty:
        while queue.size() > 0:
            # Dequeue a current path --> will show us to that path vertex - let's hold on to it
            current_path = queue.dequeue()
            # Get the current vertex from end of path
            current_vertex = current_path[-1]
            # is the current vertex a key in the dictionary? Then, we've already seen it, we don't need to do any work in it again
            if current_vertex not in visited:
                # add vertex to visited_set
                # ALSO add the PATH that brought us to this vertex
                # visited at the current vertex is now equal to the path, now we are storing the vertex in the set
                # i.e. add a key and value to the visited Dictionary
                    # the key is the current vertex, and the value is the path
                visited[current_vertex] = current_path
                
                # queue up all neighbors as paths - use the adjacency list
                for neighbor in self.friendships[current_vertex]:
                    # make a new copy of the current path - you might modify the original array if you don't copy
                    new_path = current_path.copy()
                    new_path.append(neighbor)
                    queue.enqueue(new_path)
                    
        return visited
        

if __name__ == '__main__':
    
    sg = SocialGraph()
    
    # created a graph with 10 users, average friendships of 2 - adjacency list
    sg.populate_graph(5, 2)
    print(f'friendships: {sg.friendships}')
    
    # People connected to you through any number of friendship connections are considered a part of your extended social network. The number of connections between one user and another are called the degrees of separation
    # starting from node 1, it takes only 1 path to itself, to get to node 3, I need the path of node 1 & 3, etc. 
    # Output - connections: {1: [1], 3: [1, 3], 4: [1, 4], 5: [1, 5], 2: [1, 4, 2]}
    connections = sg.get_all_social_paths(1)
    print(f'connections: {connections}')
