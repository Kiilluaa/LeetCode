# from collections import deque

# queue = deque([10, 5, 15])

# queue.append(2)

# node = queue.popleft()
# # popleft() removes first item from queue, returns that item so it can be stored in a variable
# # node = 10
# # queue = [5, 15, 2]

from collections import deque # import python's queue-friendly data structure 

class Solution(object):
    def levelOrder(self, root):
        if root is None: # handles an empty tree
            return []

        queue = deque([root]) # places first tree node into the queue
        result = [] # creates the list that will hold the completed levels

        # We need to continue processing nodes until the queue is empty
        while queue: # while loop condition that continues as long as queue contains nodes
            level_size = len(queue) # get the size of the level to iterate through each node
            level = [] # create a list for just the current level

            for _ in range(level_size): # for the length of the level keep iterating
                node = queue.popleft() # remove the first node from queue and store it in node
                level.append(node.val) # add node to the current level list

                if node.left: # if a left node exists
                    queue.append(node.left) # add it to queue
                
                if node.right: # is a right node exists
                    queue.append(node.right) # add it to queue
            
            result.append(level) # add the level list to the first element of the result list

        return result # return the completed result list