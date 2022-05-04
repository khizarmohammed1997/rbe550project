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
from math import pi, sqrt, atan2, cos, sin
class gopher():
    def __init__(self):
        rospy.init_node("vo")
        # self.Robot_vel = Twist()
        # self.Robot_cmd_vel_pub = rospy.Publisher("/gopher_presence/base_controller/cmd_vel", Twist, queue_size=10)
        self.rate = rospy.Rate(10)
        # self.gopher_amcl_yaw = 0
        # Subscriber to Robot Amcl
        # r_position_hdle = rospy.Subscriber("/gopher_presence/amcl_pose",PoseWithCovarianceStamped,self.r_position_callback,queue_size=10)
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
        self.maxVel = 1
        self.robotRadius = 3
        self.Time_horizon = 5
        self.start = Point(0, 0)   
        self.goal = Point(0, 0)
        self.g_plan_goal = Point(0, 0)
        # self.gopher_amcl = Point(0, 0)
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
        # i = 0
        # while i<3:
            local_goal = self.g_plan_goal
            # print("found",self.VO_traj.found_path)
            local_goal.x = 0
            local_goal.y = 0
            # print("local goal",local_goal.y)
            flag = self.VO_traj.engine(local_goal)
            if flag == 1:
                break
        # rospy.sleep(1)
        # i=i+1
        rospy.spin()
        


    
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
        self.Robot_vel = Twist()
        self.dt = dt
        self.gen_rand = 100 # velocities sampled at each step
        self.goal_thresh = 0.1 # threshold within which goal is reached
        self.Robot_cmd_vel_pub = rospy.Publisher("/gopher_presence/base_controller/cmd_vel", Twist, queue_size=10)
        r_position_hdle = rospy.Subscriber("/gopher_presence/amcl_pose",PoseWithCovarianceStamped,self.r_position_callback,queue_size=10)
        self.gopher_amcl = Point(0, 0)
        self.gopher_amcl_yaw = 0
        self.found_path = False
        self.way_point = Point(0, 0)

    def r_position_callback(self,data):
        # print("Gopher Pose")
        self.gopher_amcl.x = data.pose.pose.position.x
        self.gopher_amcl.y = data.pose.pose.position.y
        quarternion = [data.pose.pose.orientation.x,data.pose.pose.orientation.y,data.pose.pose.orientation.z, data.pose.pose.orientation.w]
        (roll, pitch, yaw) = tf.transformations.euler_from_quaternion(quarternion)
        print("amcl_x",self.gopher_amcl.x)
        print("amcl_y",self.gopher_amcl.y)
        self.gopher_amcl_yaw = yaw
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
    
    def engine(self,goal):
        self.goal = goal
        self.start = self.gopher_amcl
        self.best_vel = 0
        self.best_theta = 0
        self.found_path = False
        best_cost = self.cost_function(self.start)
        self.new_cost = best_cost
        print("best cost initla",best_cost)
        print("start amcl_x",self.start.x)
        print("start amcl_y",self.start.y)
        while not self.found_path and (not rospy.is_shutdown()):    
            if self.gopher_amcl.x == 0 and self.gopher_amcl.y == 0:
                break
            # check if goal has been reached 
            self.new_cost = self.cost_function(self.gopher_amcl)  
            if self.new_cost < self.goal_thresh:
                print("best_cost",self.new_cost)
                self.found_path = True
                self.Robot_vel.linear.x = 0
                self.Robot_vel.angular.z = 0
                self.Robot_cmd_vel_pub.publish(self.Robot_vel)
                break
            # generate random velocities to be taken as next step
            for _ in range(self.gen_rand):
                collision_free_step = True
                # compute a random next step for the robot to take
                next_vel, next_theta, next_step = self.get_random_vel(self.gopher_amcl)
              
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
                        self.best_vel = next_vel
                        self.best_theta = next_theta
            print("best_cost",best_cost)
  
            self.way_point = next_step
            # self.way_point = Point(0, 0)
            print("way_x",self.way_point.x)
            print("way_y",self.way_point.y)
            angular_set_point = atan2(self.way_point.y-self.gopher_amcl.y, self.way_point.x-self.gopher_amcl.x)
            angular_controller = Controller(P=0.01, D=0.5, set_point=angular_set_point)
            linear_set_point = sqrt((self.way_point.y-self.gopher_amcl.y)**2 + (self.way_point.x-self.gopher_amcl.x)**2)
            linear_controller = Controller(P=0.1, D=1, set_point=linear_set_point)
            #Control loop -orientation
            print("angular_setpoint",angular_set_point)
            print("Linear setpoint",linear_set_point)


            while(min(abs(self.gopher_amcl_yaw - angular_set_point), abs(self.gopher_amcl_yaw -2*pi-angular_set_point))>0.5):
                self.Robot_vel.linear.x = 0
                self.Robot_vel.angular.z = angular_controller.update(self.gopher_amcl_yaw)
                self.Robot_cmd_vel_pub.publish(self.Robot_vel)
                print("angular",abs(self.gopher_amcl_yaw - angular_set_point))
                rospy.sleep(0.1)

            self.Robot_vel.linear.x = 0
            self.Robot_vel.angular.z = 0
            self.Robot_cmd_vel_pub.publish(self.Robot_vel)
            rospy.sleep(0.1)

            # Control loop - Position and Orientation
            while(abs(self.gopher_amcl.x-self.way_point.x)>0.15 or abs(self.gopher_amcl.y-self.way_point.y)>0.15):
                feedback_distance = linear_set_point - sqrt((self.way_point.y-self.gopher_amcl.y)**2 + (self.way_point.x-self.gopher_amcl.x)**2)
                distance = linear_controller.update(feedback_distance)
                self.Robot_vel.linear.x = distance
                theta = angular_controller.update(self.gopher_amcl_yaw)
                #Boundary conditions
                if theta > 2*pi:
                    self.Robot_vel.angular.z = theta - 2*pi
                elif theta < -2*pi:
                    self.Robot_vel.angular.z = theta - 2*pi
                else:
                    self.Robot_vel.angular.z = theta
                self.Robot_cmd_vel_pub.publish(self.Robot_vel)
                rospy.sleep(0.1)
                print("limit",feedback_distance)
                if abs(linear_set_point-feedback_distance) < 0.5 and (feedback_distance !=0):
                    # self.found_path = True
                    break
            
    
            self.Robot_vel.linear.x = 0
            self.Robot_vel.angular.z = 0
            self.Robot_cmd_vel_pub.publish(self.Robot_vel)
            rospy.sleep(0.3)
            # self.found_path = True

            ####################################

            
        return  self.found_path
        

class Controller:
    def __init__(self, P=0.0, D=0.0, set_point=0):
        self.Kp = P
        self.Kd = D
        self.set_point = set_point 
        self.previous_error = 0

    def update(self, current_value):
        error = self.set_point - current_value
        P_term = self.Kp*error
        D_term = self.Kd*(error - self.previous_error)
        self.previous_error = error
        return P_term + D_term
    
    def setPoint(self, set_point):
        self.set_point = set_point
        self.previous_error = 0

    def setPD(self, P=0.0, D=0.0):
        self.Kp = P
        self.Kd = D


  # PID Controller Class 
class Controller:
    def __init__(self, P=0.0,I=0.0,D=0.0, set_point=0,j_t=0):
        self.Kp = P
        self.Ki = I
        self.Kd = D
        self.set_point = set_point 
        self.previous_error = 0
        self.error_sum=0
        self.jt=j_t #Joint type-0 revolute ;1 -Prismatic

    def update(self, current_value):
        error = self.set_point - current_value
        #to avoid Integral wind up problem.Resetting integral amount 
        if self.jt==0:
            if abs(error)>0.15:
                #accumulation of error
                self.error_sum=self.error_sum+error
            else:
                self.error_sum=0
        else:
            
            if abs(error)>0.002:
                self.error_sum=self.error_sum+error
            else:
                self.error_sum=0
        P_term = self.Kp*error
        I_term = self.Ki*self.error_sum
        D_term = self.Kd*(error - self.previous_error)
        self.previous_error = error
        return P_term + I_term + D_term
    
    def setPoint(self, set_point):
        self.set_point = set_point
        self.previous_error = 0

    def setPD(self, P=0.0,I=0.0, D=0.0):
        self.Kp = P
        self.Ki = I
        self.Kd = D      
    
        


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
    


















