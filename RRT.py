# Standard Algorithm Implementation
# Sampling-based Algorithms RRT and RRT*

from stat import S_IRWXO
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
        point1=[node1.row,node1.col]
        point2=[node2.row,node2.col]
        dist=np.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)
        return dist

    
    def check_collision(self, p1, p2):
        '''Check if the path between two nodes collide with obstacles
        arguments:
            node1 - node 1
            node2 - node 2

        return:
            True if the new node is valid to be connected
        '''
        row_points = np.linspace(p1.row, p2.row).astype(int)
        col_points = np.linspace(p1.col, p2.col).astype(int)
        points = zip(row_points, col_points)

        # Checking for collision in the path
        obstacle = False
        for a_point in points:
            if self.map_array[a_point[0], a_point[1]] == 0:
                obstacle = True

        return obstacle



    def get_new_point(self, goal_bias):
        '''Choose the goal or generate a random point
        arguments:
            goal_bias - the possibility of choosing the goal instead of a random point

        return:
            point - the new point
        '''
        choice=np.random.choice(["r","g"], 1, p=[1-goal_bias,goal_bias])
        if choice=="r":
            point=Node(np.random.randint(low=0, high=298,dtype=int),np.random.randint(low=0, high=298,dtype=int))
        else:
            point=Node(self.goal.row,self.goal.col)

        return [point.row,point.col]              

        
    def get_nearest_node(self, point):
        '''Find the nearest node in self.vertices with respect to the new point
        arguments:
            point - the new point

        return:
            the nearest node
        '''
        points = []
        for a_node in self.vertices:
            points.append((a_node.row,a_node.col))  

        tree   = KDTree(points)
        #finidng the nearest node in the tree
        _,index  = tree.query((point[0],point[1]),k=1)
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
        

        vertices_points     = []
        #adding diiferent sample points to get row and col values
        for node in self.vertices:
            vertices_points.append((node.row,node.col))  
        #accessin the tree
        tree      = KDTree(vertices_points)
        near_index       = tree.query_ball_point((new_node.row,new_node.col),neighbor_size)

        for i in near_index:
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
        for a_node in neighbors:
            if self.check_collision(new_node,a_node) == False and (self.dis(new_node,a_node) + new_node.cost) < a_node.cost:
                
                #making new node the parent nide
                # print(a_node)

                a_node.parent = new_node
                a_node.cost   = new_node.cost + self.dis(new_node,a_node)


    def extend(self, nearest_node, sample_point, stepsize):
        #creates a step in the direction of the sampled node
        m = np.arctan2(sample_point[1]-nearest_node.col,sample_point[0]-nearest_node.row)
        row = int(np.round(nearest_node.row + np.cos(m)*stepsize))
        col = int(np.round(nearest_node.col + np.sin(m)*stepsize))
        
        row = np.clip(row,0,self.size_row-1)
        col = np.clip(col,0,self.size_col-1)
        return (row,col)        


    def draw_map(self):
        '''Visualization of the result
        '''
        # Create empty map
        fig, ax = plt.subplots(1)
        img = 255 * np.dstack((self.map_array, self.map_array, self.map_array))
        ax.imshow(img)

        # Draw Trees or Sample points
        for node in self.vertices[1:-1]:
            plt.plot(node.col, node.row, markersize=3, marker='o', color='y')
            plt.plot([node.col, node.parent.col], [node.row, node.parent.row], color='y')
        
        # Draw Final Path if found
        if self.found:
            cur = self.goal
            while cur.col != self.start.col or cur.row != self.start.row:
                plt.plot([cur.col, cur.parent.col], [cur.row, cur.parent.row], color='b')
                cur = cur.parent
                plt.plot(cur.col, cur.row, markersize=3, marker='o', color='b')

        # Draw start and goal
        plt.plot(self.start.col, self.start.row, markersize=5, marker='o', color='g')
        plt.plot(self.goal.col, self.goal.row, markersize=5, marker='o', color='r')

        # show image
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
        goal_radius           = 10

        while i < n_pts:
            
            #sampling a new point and finding nearest node
            sample   = self.get_new_point(goal_bias)
            near_node  = self.get_nearest_node(sample)

            #find a step point
            step     = self.extend(near_node,sample,goal_radius)
            s_row=step[0]
            s_col=step[1]
            
            #chcecking for obstacels
            if self.map_array[s_row,s_col] == 1:
                step_node      = Node(s_row,s_col)

                #checking for collisions                    
                if self.check_collision(step_node,near_node) == False:
                    step_node.parent = near_node
                    step_node.cost   = near_node.cost + self.dis(step_node,near_node)
                    self.vertices.append(step_node)
                    
                    #checinh if goal is  closeby
                    if self.dis(step_node,self.goal) < goal_radius: 
                            self.found = True
                            self.goal.parent = step_node
                            self.goal.cost = self.dis(step_node,self.goal) + step_node.cost
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
        goal_radius       = 6
        while i < n_pts:
            
            #getting new points to sample
            sample   = self.get_new_point(goal_bias)

            #checking if sampled point is an obstacle
            if self.map_array[sample[0],sample[1]] == 1:
                near_node  = self.get_nearest_node(sample)
                
                #finidng an extended step
                # print(step)
                step     = self.extend(near_node,sample,goal_radius)
                # 
                # print(step)
                s_row=step[0]
                s_col=step[1]

                #checing collisons on extended step
                if self.map_array[s_row,s_col] == 1:
                    step_node      = Node(s_row,s_col)

                    #collison checking on path
                    if self.check_collision(step_node,near_node) == False:
                        neighbors   = self.get_neighbors(step_node,neighbor_size)
                        least_cost_node  = near_node
                        min_cost    = self.dis(step_node,near_node) + near_node.cost
                        
                        for idx,node in enumerate(neighbors):
                            if self.dis(step_node,node)+ node.cost < min_cost:
                                least_cost_node  = neighbors[idx]
                                # print(min_cost)
                                min_cost    = self.dis(step_node,node)+ node.cost
                        
                        #cheking collision for rewiring
                        if self.check_collision(step_node,least_cost_node) == False:
                            step_node.parent = least_cost_node
                            step_node.cost   = least_cost_node.cost + self.dis(step_node,least_cost_node)

                            # print(f" rewiring need {step_node}")
                            self.vertices.append(step_node)
                            self.rewire(step_node,neighbors)

                        if self.dis(step_node,self.goal) < goal_radius: 
                                self.found = True
                                self.goal.parent = step_node
                                self.goal.cost = self.dis(step_node,self.goal) + step_node.cost
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



        self.graph.clear()
        i=0
        
        
        while i < n_pts:
            poin1_row = int(np.random.randint(0,(self.size_row-1),1))
            poin1_col = int(np.random.randint(0,(self.size_col-1),1))
            point1_val=self.map_array[poin1_row,poin1_col]       

            if point1_val == 0:
                point2_row = int(np.round(np.random.normal(poin1_row, 15, 1)))
                point2_col = int(np.round(np.random.normal(poin1_col, 15, 1)))

                point2_val=self.map_array[point2_row,point2_col]

                
                if point2_row > self.size_row-1:
                    point2_row = self.size_row-1
                if point2_row < 0:
                    point2_row = 0    
                if point2_col > self.size_col-1:
                    point2_col = self.size_col-1
                if point2_col < 0:
                    point2_col = 0

                if point2_val == 0:                     
                    midpoint_row = int((point2_row+poin1_row)/2)
                    midpoint_col = int((point2_col+poin1_col)/2)
                    
                    midpoint_val=self.map_array[midpoint_row,midpoint_col]


                    if midpoint_val == 1 and (midpoint_row,midpoint_col) not in self.samples:
                        self.samples.append((midpoint_row,midpoint_col))                
                    
            i = i+1
        