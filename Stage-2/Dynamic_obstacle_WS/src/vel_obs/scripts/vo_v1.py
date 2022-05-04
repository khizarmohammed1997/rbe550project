#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import random


import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import PoseWithCovarianceStamped,PoseStamped,Twist
from nav_msgs.msg import Path
from nav_msgs.msg import OccupancyGrid
#from vel_obs.srv import G_plan,G_planResponse

class gopher():
    def __init__(self):
        rospy.init_node("vo")
        self.Robot_vel = Twist()
        self.Robot_cmd_vel_pub = rospy.Publisher("/gopher_presence/base_controller/cmd_vel", Twist, queue_size=10)
        self.rate = rospy.Rate(10)

        # Subscriber to Robot Amcl
        r_position_hdle = rospy.Subscriber("/gopher_presence/amcl_pose",PoseWithCovarianceStamped,self.r_position_callback,queue_size=10)

        # Subscriber to Robot Odom

        # Subscriber to Obstacle Amcl
        

        # Subscriber to Obstacle Odom

        # Subscriber to Occupancy Map
        map_hdle = rospy.Subscriber("/map",OccupancyGrid,self.map_callback,queue_size=10) 

        # Subscriber to Get Global Goal

        # Subscriber to get Global Path Plan
        # g_plan_hdle = rospy.Subscriber("/gopher_presence/move_base/TrajectoryPlannerROS/global_plan",Path,self.g_plan_callback,queue_size=10) 
        g_plan_hdle = rospy.Subscriber("/gopher_presence/move_base/AjithPlannerROS/global_plan",Path,self.g_plan_callback,queue_size=10) 
        

        try:
            self.run()
        except rospy.ROSInterruptException:
            rospy.loginfo("Action terminated.")
        
    def run(self):
        # while not rospy.is_shutdown():
        #     self.Robot_vel.linear.x = 0
        #     print("publishing data")
        #     self.Robot_cmd_vel_pub.publish(self.Robot_vel)
        #     rospy.sleep(0.1)
        rospy.loginfo("Run successfully completed")  
        rospy.spin()
        
    def r_position_callback(self,data):
        print("Gopher Pose")
        self.gopher_amcl = data
        print(self.gopher_amcl.pose.pose.position)

    
    def map_callback(self,map_data):
        print("map")
        self.map_array = map_data
        print(len(self.map_array.data))

    def g_plan_callback(self,plan_data):
        print("global plan")
        self.g_plan_array = plan_data
        print(self.g_plan_array.poses[0].pose.position)
        
    def calculateik(self, x,y,z):
        rospy.wait_for_service("global_plan")
        try:
            inverse = rospy.ServiceProxy("global_plan",G_plan)
            out = inverse(x,y,z)
            return out
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)







class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def draw(self, ax, color, marker, size):
        ax.scatter(self.x, self.y, c=color, marker=marker, s=size)

class Circle():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_r(self):
        return self.r
        
    def draw(self, ax, color):
        circle = plt.Circle((self.x, self.y), self.r, color=color, fill=False)
        ax.add_patch(circle)

class Robot(Circle):
    def __init__(self, x, y, r, max_vel):
        super().__init__(x, y, r)
        self.max_vel = max_vel
        self.trajectory = [Point(x,y)]
    
    def update(self, new_point):
        self.x = new_point.x
        self.y = new_point.y
        self.trajectory.append(Point(self.x,self.y))

    def draw_trajectory(self, ax):
        for i in range(len(self.trajectory) - 1):
            x = [self.trajectory[i].x, self.trajectory[i+1].x]
            y = [self.trajectory[i].y, self.trajectory[i+1].y]
            ax.plot(x, y, c='y', marker='o', markersize=5)

        
class Obstacle(Circle):
    def __init__(self, x, y, r, vel, theta):
        super().__init__(x, y, r)
        self.velx = vel * np.cos(theta)
        self.vely = vel * np.sin(theta)
        self.trajectory = [Point(x,y)] 
        
    def update(self, dt):
        self.x = self.x + self.velx * dt
        self.y = self.y + self.vely * dt
        self.trajectory.append(Point(self.x,self.y))
    
    def draw_trajectory(self, ax):
        for i in range(len(self.trajectory) - 1):
            x = [self.trajectory[i].x, self.trajectory[i+1].x]
            y = [self.trajectory[i].y, self.trajectory[i+1].y]
            ax.plot(x, y, c='b', marker='*', markersize=5)




def check_within_vo(obstacle, robot, rvel, theta):
    # compute the relative velocity
    relvx, relvy = rvel * np.cos(theta) - obstacle.velx, \
                   rvel * np.sin(theta) - obstacle.vely
    # compute the relative position
    rx, ry = obstacle.x - robot.x, \
             obstacle.y - robot.y
    
    r2 = rx**2 + ry**2
    rvel2 = relvx**2 + relvy**2
    dot_prod2 = (rx*relvx + ry*relvy)**2
    
    # compute the configuration radius
    cr2 = (obstacle.r + robot.r)**2
    
    # compute the constraint condition 
    condition = (r2 - dot_prod2 / rvel2) >= cr2
    return condition


class Env:
    def __init__(self, xmin, xmax, ymin, ymax, start, goal):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        
        self.start = start
        self.goal = goal
        
        self.fig, self.ax = plt.subplots(1, 1, figsize=(15,15))
        
    def draw_env(self, robot, obstacles, step):
        self.refresh_plot()
        
        self.add_title('Velocity Obstacle: Test Case - 1')
        
        self.goal.draw(self.ax, 'g', '*', 100)
        self.start.draw(self.ax,'r', '*', 100)
        
        for obstacle in obstacles:
            obstacle.draw(env.ax, 'r')
            obstacle.draw_trajectory(self.ax)
       
        robot.draw_trajectory(self.ax)
        robot.draw(env.ax, 'b')

        env.fig.savefig('./{}.png'.format(str(step)), dpi=100)
        
        plt.show()
        plt.close()
        
    def refresh_plot(self):
        self.fig, self.ax = plt.subplots(1, 1, figsize=(15,15))
            
    def draw_path(self, pathx, pathy):
        self.ax.plot(pathx,pathy)
            
    def add_title(self, title):
        self.ax.set_title(title, loc='center', fontweight ="bold")




class VOTrajectory:
    def __init__(self,env, start, end, robot, obstacles, dt):
        
        self.env = env
        self.robot = robot
        self.obstacles = obstacles

        self.traj = [start]
        self.goal = end
        
        self.dt = dt
        self.gen_rand = 100 # velocities sampled at each step
        self.goal_thresh = 1 # threshold within which goal is reached

        self.found_path = False
    
    def get_random_vel(self, cur_step):
        """ 
        Returns a random velocity vector for the robot
        from a uniform probability distribution (0, max velocity)
        Also returns the next step that this velocity would make
        the robot reach.
        """
        theta = np.random.uniform(0, 2*np.pi)
        vel = np.random.uniform(0, self.robot.max_vel)

        x = cur_step.x + vel * self.dt * np.cos(theta)
        y = cur_step.y + vel * self.dt * np.sin(theta)
        
        return vel, theta, Point(x,y)
        
    def cost_function(self, next_step):
        """ 
        Computes the L2 distance between a given step and the goal node
        """
        goalX, goalY = self.goal.get_x(), self.goal.get_y() 
        nextX, nextY = next_step.get_x(), next_step.get_y()

        cost = np.sqrt((nextX - goalX)**2 + (nextY - goalY)**2)
        
        return cost
    
    def engine(self):
        best_cost = self.cost_function(self.traj[-1])
        step = 0
        while not self.found_path:    
            best_step = None
            
            # generate random velocities to be taken as next step
            for _ in range(self.gen_rand):
                collision_free_step = True
              
                # compute a random next step for the robot to take
                next_vel, next_theta, next_step = self.get_random_vel(self.traj[-1])
              
               # check whether the sampled velocity lies within the collision cone of any obstacle
                for obs in self.obstacles:
                    if not check_within_vo(obs, robot, next_vel, next_theta):
                        collision_free_step = False
                        break
              
                # Static obstacles check condition neeed to be added



                # if it is a collision free step, compute cost 
                # and check if it is the best step yet      
                if collision_free_step:
#                     idx += 1
                    cost = self.cost_function(next_step)
                    if cost < best_cost:
                        best_cost = cost
                        best_step = next_step
            
            if best_step is not None:
                step += 1
                self.traj.append(best_step)
                for obs in self.obstacles:
                    obs.update(self.dt)
                self.robot.update(best_step)
                
            # check if goal has been reached   
            if best_cost < self.goal_thresh:
                self.found_path = True
                break
            
            # self.env.draw_env(self.robot, self.obstacles, step) 


# # define the grid dimensions
# #Cost map dimensions
# gridStartX = 0 
# gridStartY = 0
# gridEndX = 150
# gridEndY = 150

# # define robot and time parameters
# maxVel = 5
# robotRadius = 3
# dt = 1

# # set the start and goal nodes
# #get this data amcl 
# start = Point(10, 60)   
# #get this data rviz
# goal = Point(80, 0)

# # define the robot and obstacles
# robot = Robot(start.get_x(), start.get_y(), robotRadius, maxVel)

# # x,y,radius,obstacle velocity,its oreintation
# obstacles = [   Obstacle(35, 75, 7, 0.5, np.pi/6),
#                 Obstacle(30, 40, 10, 0.5, np.pi/3),
#                 Obstacle(10, 30, 5 , 0.5, 0),
#                 Obstacle(50, 0, 6 , 0.5, np.pi/2) ]

# # define the environment
# env = Env(gridStartX, gridEndX, gridStartY, gridEndY, start, goal)
# env.add_title('Velocity Obstacle: Test Case - 1')

# # compute the trajectory
# VO_traj = VOTrajectory(env, start, goal, robot, obstacles, dt)
# VO_traj.engine()



if __name__ == "__main__":
    gopher_robot = gopher()
    # gopher_robot.run()
    


















