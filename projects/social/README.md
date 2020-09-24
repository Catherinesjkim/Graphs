# Social Graph

You have been assigned the task of building a new friend-based social network. In this network, users are able to view their own friends, friends of their friends, friends of their friends' friends, and so on. People connected to you through any number of friendship connections are considered a part of your extended social network.

The functionality behind creating users and friendships has been completed already. Your job is to implement a function that shows all the friends in a user's extended social network and chain of friendships that link them. The number of connections between one user and another are called the degrees of separation.

Your client is also interested in how the performance will scale as more users join so she has asked you to implement a feature that creates large numbers of users to the network and assigns them a random distribution of friends.

## 1. Generating Users and Friendships

It will be easier to build your extended social network if you have users to test it with. `populate_graph()` takes in a number of users to create and the average number of friends each user should have and creates them.

```
>>> sg = SocialGraph()
>>> sg.populate_graph(10, 2)  # Creates 10 users with an average of 2 friends each
>>> print(sg.friendships)
{1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
>>> sg = SocialGraph()
>>> sg.populate_graph(10, 2)
>>> print(sg.friendships)
{1: {8}, 2: set(), 3: {6}, 4: {9, 5, 7}, 5: {9, 10, 4, 6}, 6: {8, 3, 5}, 7: {4}, 8: {1, 6}, 9: {10, 4, 5}, 10: {9, 5}}
```

Note that in the above example, the average number of friendships is exactly 2 but the actual number of friends per user ranges anywhere from 0 to 4.

* Hint 1: To create N random friendships, you could create a list with all possible friendship combinations, shuffle the list, then grab the first N elements from the list. You will need to `import random` to get shuffle.
* Hint 2: `add_friendship(1, 2)` is the same as `add_friendship(2, 1)`. You should avoid calling one after the other since it will do nothing but print a warning. You can avoid this by only creating friendships where user1 < user2.

## 2. Degrees of Separation

Now that you have a graph full of users and friendships, you can crawl through their social graphs. `get_all_social_paths()` takes a userID and returns a dictionary containing every user in that user's extended network along with the shortest friendship path between each.

```
>>> sg = SocialGraph()
>>> sg.populate_graph(10, 2)
>>> print(sg.friendships)
{1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
>>> connections = sg.get_all_social_paths(1)
>>> print(connections)
{1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}
```
Note that in this sample, Users 3, 4 and 9 are not in User 1's extended social network.

* Hint 1: What kind of graph search guarantees you a shortest path?
* Hint 2: Instead of using a `set` to mark users as visited, you could use a `dictionary`. Similar to sets, checking if something is in a dictionary runs in O(1) time. If the visited user is the key, what would the value be?


## 3. Questions

1. To create 100 users with an average of 10 friends each, how many times would you need to call add_friendship()? Why? 

Call add friendship 100 times --> Answer: 500. Statistical algorithms developed by Kang and others [6-8] to estimate distances with great accuracy, basically finding the approximate number of people within 1, 2, 3 (and so on) hops away from a source. For each number of hops we estimate the number of distinct people you can reach from every source. This estimation can be done efficiently using the Flajolet-Martin algorithm [9]. How does it work? Imagine you have a set of people and you want to count how many are unique. First you assign each person a random integer; let’s call it hash. Approximately 1/2 of the people will have an even hash: the binary representation of the hash will end with 0. Approximately 1/4 of the people will have a hash divisible by 4; that is, the binary representation ends with 00. In general, 1/2n people will have the binary representation of their hash end with n zeros. Now, we can reverse this and try to count how many different people we have by reading their hash values one by one. To do that, we track the biggest number of zeroes we’ve seen. Intuitively, if there were n zeroes, we can expect set to have c*2n unique numbers, where c is some constant. For better accuracy we can do this computation multiple times with different hash values.

2. If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? 50%
What is the average degree of separation between a user and those in his/her extended network? 

Answer: 3.57 average degree. Each person in the world (at least among the 1.59 billion people active on Facebook) is connected to every other person by an average of three and a half other people. The average distance we observe is 4.57, corresponding to 3.57 intermediaries or “degrees of separation.” Within the US, people are connected to each other by an average of 3.46 degrees. 

Reference: https://research.fb.com/blog/2016/02/three-and-a-half-degrees-of-separation/


## 4. Stretch Goal

1. You might have found the results from question #2 above to be surprising. Would you expect results like this in real life? If not, what are some ways you could improve your friendship distribution model for more realistic results?

2. If you followed the hints for part 1, your `populate_graph()` will run in O(n^2) time. Refactor your code to run in O(n) time. Are there any tradeoffs that come with this implementation?

