#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import random

import tf
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
        self.gopher_amcl_yaw = 0
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
        
        ########## VO variables ##############
        # define robot and time parameters
        self.maxVel = 5
        self.robotRadius = 3
        self.Time_horizon = 1
        self.start = Point(0, 0)   
        self.goal = Point(0, 0)
        self.g_plan_goal = Point(0, 0)
        self.gopher_amcl = Point(0, 0)
        # x,y,radius,obstacle velocity,its oreintation
        obstacles = [Obstacle(0, 0, 1, 0, 0)]
        self.robot = Robot(self.start.get_x(), self.start.get_y(), self.robotRadius, self.maxVel)
        # compute the trajectory
        self.VO_traj = VOTrajectory(self.robot, obstacles, self.Time_horizon)
        try:
            self.run()
        except rospy.ROSInterruptException:
            rospy.loginfo("Action terminated.")
        
    def run(self):
        while not rospy.is_shutdown():
            local_goal = self.g_plan_goal
            # print("found",self.VO_traj.found_path)
            local_goal.x = -0.0606698617339
            local_goal.y = 3.46535515785
            print("local goal",local_goal.y)
            print("amcl",self.gopher_amcl.y)
            self.VO_traj.engine(local_goal,self.gopher_amcl)
            self.Robot_vel.linear.x = self.VO_traj.best_vel
            self.Robot_vel.angular.z = self.VO_traj.best_theta - self.gopher_amcl_yaw
            print("VO",self.VO_traj.best_vel)
            self.Robot_cmd_vel_pub.publish(self.Robot_vel)  
            rospy.sleep(1)
  

        # rospy.spin()
        
    def r_position_callback(self,data):
        # print("Gopher Pose")
        self.gopher_amcl.x = data.pose.pose.position.x
        self.gopher_amcl.y = data.pose.pose.position.y
        quarternion = [data.pose.pose.orientation.x,data.pose.pose.orientation.y,data.pose.pose.orientation.z, data.pose.pose.orientation.w]
        (roll, pitch, yaw) = tf.transformations.euler_from_quaternion(quarternion)
        print(self.gopher_amcl.y)
        self.gopher_amcl_yaw = yaw

    
    def map_callback(self,map_data):
        # print("map")
        self.map_array = map_data
        # print(len(self.map_array.data))

    def g_plan_callback(self,plan_data):
        # print("global plan")
        self.g_plan_array = plan_data
        # print(self.g_plan_array.poses[0].pose.position)
        self.g_plan_goal.x = self.g_plan_array.poses[10].pose.position.x
        self.g_plan_goal.y = self.g_plan_array.poses[10].pose.position.y


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    

class Robot():
    def __init__(self, x, y, r, max_vel):
        # super().__init__(x, y, r)
        self.max_vel = max_vel
        self.trajectory = [Point(x,y)]
    
    def update(self, new_point):
        self.x = new_point.x
        self.y = new_point.y
        self.trajectory.append(Point(self.x,self.y))


   
        
class Obstacle():
    def __init__(self, x, y, r, vel, theta):
        # super().__init__(x, y, r)
        self.velx = vel * np.cos(theta)
        self.vely = vel * np.sin(theta)
        self.trajectory = [Point(x,y)] 
        
    def update(self, dt):
        self.x = self.x + self.velx * dt
        self.y = self.y + self.vely * dt
        self.trajectory.append(Point(self.x,self.y))
    
    

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



class VOTrajectory:
    def __init__(self, robot, obstacles, dt):
        
        self.robot = robot
        self.obstacles = obstacles

        # self.traj = [start]
        # self.goal = end
        
        self.dt = dt
        self.gen_rand = 100 # velocities sampled at each step
        self.goal_thresh = 0.1 # threshold within which goal is reached

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
    
    def engine(self,goal,start):
        step = 0
        self.goal = goal
        self.start = start
        self.best_vel = 0
        self.best_theta = 0
        self.traj = [self.start]
        self.found_path = False
        best_cost = self.cost_function(self.traj[-1])
        print("best cost initla",best_cost)
        while not self.found_path:    
            best_step = None
            
            # generate random velocities to be taken as next step
            for _ in range(self.gen_rand):
                collision_free_step = True
              
                # compute a random next step for the robot to take
                next_vel, next_theta, next_step = self.get_random_vel(self.traj[-1])
              
               # check whether the sampled velocity lies within the collision cone of any obstacle
                # for obs in self.obstacles:
                #     # if not check_within_vo(obs, self.robot, next_vel, next_theta):
                #     #     collision_free_step = False
                #     #     break
              
                # Static obstacles check condition neeed to be added

                # if it is a collision free step, compute cost 
                # and check if it is the best step yet      
                if collision_free_step:
                    cost = self.cost_function(next_step)
                    if cost < best_cost:
                        best_cost = cost
                        best_step = next_step
                        self.best_vel = next_vel
                        self.best_theta = next_theta
                        # best_vel_x =  best_vel * np.cos(best_theta)
                        # best_vel_y =  best_vel * np.sin(best_theta)

            if best_step is not None:
                step += 1
                self.traj.append(best_step)
                # best_vel = self.robot.update(best_step)
            # self.Robot_vel.linear.x = self.VO_traj.best_vel
            # self.Robot_vel.angular.z = self.VO_traj.best_theta - self.gopher_amcl_yaw
            # print("VO",self.VO_traj.best_vel)
            # self.Robot_cmd_vel_pub.publish(self.Robot_vel)  
            ####################################
 
            # check if goal has been reached   
            if best_cost < self.goal_thresh:
                print("best_cost",best_cost)
                self.found_path = True
                break
        

            


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
    


















