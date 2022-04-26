# Standard Algorithm Implementation
# Sampling-based Algorithms RRT and RRT*

import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import KDTree

# Class for each tree node
class Node:
    def __init__(self, row, col):
        self.row    = row       # coordinate
        self.col    = col       # coordinate
        self.parent = None      # parent node
        self.cost   = 0.0       # cost


# Class for RRT
class RRT:
    # Constructor
    def __init__(self, map_array, start, goal):
        self.map_array  = map_array                 # map array, 1->free, 0->obstacle
        self.size_row   = map_array.shape[0]        # map size
        self.size_col   = map_array.shape[1]        # map size

        self.start      = Node(start[0], start[1])  # start node
        self.goal       = Node(goal[0], goal[1])    # goal node
        self.vertices   = []                        # list of nodes
        self.found      = False                     # found flag
        

    def init_map(self):
        '''Intialize the map before each search
        '''
        self.found      = False
        self.vertices   = []
        self.vertices.append(self.start)

    
    def dis(self, node1, node2):
        '''Calculate the euclidean distance between two nodes
        arguments:
            node1 - node 1
            node2 - node 2

        return:
            euclidean distance between two nodes
        '''
        dist = np.sqrt((node1.row - node2.row) ** 2 + (node1.col - node2.col) ** 2)
        return dist

    
    def check_collision(self, node1, node2):
        '''Check if the path between two nodes collide with obstacles
        arguments:
            node1 - node 1
            node2 - node 2

        return:
            True if the new node is valid to be connected
        '''
        flag = False
        if abs(node1.row-node2.row) > abs(node1.col-node2.col):
            x = np.linspace(node1.row,node2.row,abs(node2.row-node1.row)+1).astype(int)
            y = np.round(np.linspace(node1.col,node2.col,abs(node2.row-node1.row)+1)).astype(int)
        else:
            x = np.round(np.linspace(node1.row,node2.row,abs(node2.col-node1.col)+1)).astype(int)
            y = np.linspace(node1.col,node2.col,abs(node2.col-node1.col)+1).astype(int)            
            
        for i,j in zip(x,y):
            if self.map_array[i,j] == 0:
                flag = True
        return flag


    def get_new_point(self, goal_bias):
        '''Choose the goal or generate a random point
        arguments:
            goal_bias - the possibility of choosing the goal instead of a random point

        return:
            point - the new point
        '''
        x   = int(np.random.randint(0,self.size_row-1,1))
        y   = int(np.random.randint(0,self.size_col-1,1))
        point = [(x,y),(self.goal.row,self.goal.col)][int(np.random.choice([0,1],size = 1, p = [1-goal_bias,goal_bias]))]
        return point               

        
    def get_nearest_node(self, point):
        '''Find the nearest node in self.vertices with respect to the new point
        arguments:
            point - the new point

        return:
            the nearest node
        '''
        samples = []
        for node in self.vertices:
            samples.append((node.row,node.col))  

        kdtree   = KDTree(samples)
        _,index  = kdtree.query((point[0],point[1]),k=1)
        return self.vertices[index]


    def get_neighbors(self, new_node, neighbor_size):
        '''Get the neighbors that are within the neighbor distance from the node
        arguments:
            new_node - a new node
            neighbor_size - the neighbor distance

        return:
            neighbors - a list of neighbors that are within the neighbor distance 
        '''
        neighbors   = []
        samples     = []
        for node in self.vertices:
            samples.append((node.row,node.col))  

        kdtree      = KDTree(samples)
        index       = kdtree.query_ball_point((new_node.row,new_node.col),neighbor_size)

        for i in index:
            neighbors.append(self.vertices[i])

        return neighbors


    def rewire(self, new_node, neighbors):
        '''Rewire the new node and all its neighbors
        arguments:
            new_node - the new node
            neighbors - a list of neighbors that are within the neighbor distance from the node

        Rewire the new node if connecting to a new neighbor node will give least cost.
        Rewire all the other neighbor nodes.
        '''
        for node in neighbors:
            if self.check_collision(new_node,node) == False and (self.dis(new_node,node) + new_node.cost) < node.cost:
                #self.vertices.remove(node)
                node.parent = new_node
                node.cost   = new_node.cost + self.dis(new_node,node)
                #self.vertices.append(node)


    def new_config(self, nearest_node, point, delta):
        '''Get the new node in the direction of the random sample point at a distance delta:
                node  - the nearest node
                point - the sample point
                delta - distance to move from nearest node

            return:
                new_node - a new node at a distance delta from the nearest node 
        '''
        slope = np.arctan2(point[1]-nearest_node.col,point[0]-nearest_node.row)
        x = int(np.round(nearest_node.row + np.cos(slope)*delta))
        y = int(np.round(nearest_node.col + np.sin(slope)*delta))
        x = np.clip(x,0,self.size_row-1)
        y = np.clip(y,0,self.size_col-1)
        return (x,y)        

    def return_path(self):
        path=[]
    
        if self.found:
            cur = self.goal
            while cur.col != self.start.col and cur.row != self.start.row:
                path.append([cur.col,cur.row])
                cur=cur.parent
        return path

    def draw_map(self):
        '''Visualization of the result
        '''
        # Create empty map
        fig, ax = plt.subplots(1)
        img = 255 * np.dstack((self.map_array, self.map_array, self.map_array))
        ax.imshow(img)
        print("reached checkpoint 1")
        # plt.show()
        # Draw Trees or Sample points
        for node in self.vertices[1:-1]:
            plt.plot(node.col, node.row, markersize=3, marker='o', color='y')
            plt.plot([node.col, node.parent.col], [node.row, node.parent.row], color='y')
        
        print("reached checkpoint 2")
        # plt.show()

        # Draw Final Path if found
        if self.found:
            cur = self.goal
            print("inside the plotting fuction")
            while cur.col != self.start.col or cur.row != self.start.row:
                plt.plot([cur.col, cur.parent.col], [cur.row, cur.parent.row], color='b')
                cur = cur.parent
                plt.plot(cur.col, cur.row, markersize=3, marker='o', color='b')
        
        print("reached checkpoint 3")
        # Draw start and goal
        plt.plot(self.start.col, self.start.row, markersize=5, marker='o', color='g')
        plt.plot(self.goal.col, self.goal.row, markersize=5, marker='o', color='r')

        # show image
        print('just before plt.show in draw map')
        plt.show()

    def RRT(self, n_pts=1000):
        '''RRT main search function
        arguments:
            n_pts - number of points try to sample, 
                    not the number of final sampled points

        In each step, extend a new node if possible, and check if reached the goal
        '''
        ### YOUR CODE HERE ###

        # In each step,
        # get a new point, 
        # get its nearest node, 
        # extend the node and check collision to decide whether to add or drop,
        # if added, check if reach the neighbor region of the goal.

       # Remove previous result
        self.init_map()
        i = 0
        goal_bias       = 0.05
        delta           = 4

        while i < n_pts:
            point   = self.get_new_point(goal_bias)
            #if self.map_array[point[0],point[1]] == 1:
            nearest_node  = self.get_nearest_node(point)
            new_point     = self.new_config(nearest_node,point,delta)
            if self.map_array[new_point[0],new_point[1]] == 1:
                #nearest_node  = self.get_nearest_node((new_point[0],new_point[1]))
                new_node      = Node(new_point[0],new_point[1])                    
                if self.check_collision(new_node,nearest_node) == False:
                    new_node.parent = nearest_node
                    new_node.cost   = nearest_node.cost + self.dis(new_node,nearest_node)
                    self.vertices.append(new_node)
                    if self.dis(new_node,self.goal) < delta: 
                            self.found = True
                            self.goal.parent = new_node
                            self.goal.cost = self.dis(new_node,self.goal) + new_node.cost
                            self.vertices.append(self.goal)
                            break                
            i = i+1                                  

        # Output
        if self.found:
            steps = len(self.vertices) - 2
            length = self.goal.cost
            print("It took %d nodes to find the current path" %steps)
            print("The path length is %.2f" %length)
        else:
            print("No path found")
        
        # Draw result
        self.draw_map()
        return self.return_path()


    def RRT_star(self, n_pts=1000, neighbor_size=20):
        '''RRT* search function
        arguments:
            n_pts - number of points try to sample, 
                    not the number of final sampled points
            neighbor_size - the neighbor distance
        
        In each step, extend a new node if possible, and rewire the node and its neighbors
        '''
        # Remove previous result
        self.init_map()
        # In each step,
        # get a new point, 
        # get its nearest node, 
        # extend the node and check collision to decide whether to add or drop,
        # if added, rewire the node and its neighbors,
        # and check if reach the neighbor region of the goal if the path is not found.
        i = 0
        goal_bias   = 0.05
        delta       = 10
        while i < n_pts:
            point       = self.get_new_point(goal_bias)
            if self.map_array[point[0],point[1]] == 1:
                nearest_node  = self.get_nearest_node(point)
                new_point     = self.new_config(nearest_node,point,delta)
                if self.map_array[new_point[0],new_point[1]] == 1:
                    new_node      = Node(new_point[0],new_point[1])                    
                    if self.check_collision(new_node,nearest_node) == False:
                        neighbors   = self.get_neighbors(new_node,neighbor_size)
                        cheap_node  = nearest_node
                        min_cost    = self.dis(new_node,nearest_node) + nearest_node.cost
                        
                        for idx,node in enumerate(neighbors):
                            if self.dis(new_node,node)+ node.cost < min_cost:
                                cheap_node  = neighbors[idx]
                                min_cost    = self.dis(new_node,node)+ node.cost
                        
                        if self.check_collision(new_node,cheap_node) == False:
                            new_node.parent = cheap_node
                            new_node.cost   = cheap_node.cost + self.dis(new_node,cheap_node)
                            self.vertices.append(new_node)
                            self.rewire(new_node,neighbors)

                        if self.dis(new_node,self.goal) < delta: 
                                self.found = True
                                self.goal.parent = new_node
                                self.goal.cost = self.dis(new_node,self.goal) + new_node.cost
                                self.vertices.append(self.goal)
                                #break                
            i = i+1    

        # Output
        if self.found:
            steps = len(self.vertices) - 2
            length = self.goal.cost
            print("It took %d nodes to find the current path" %steps)
            print("The path length is %.2f" %length)
        else:
            print("No path found")

        # Draw result
        self.draw_map()
        return self.return_path()
