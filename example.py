import sys
import numpy as np

from cv2 import circle


from RVO import RVO_update, reach, compute_V_des, reach
from vis import visualize_traj_dynamic
from map_creator import obstacles_adder,removing_old_dynamic_obs,update_dynamic_obs

#------------------------------
#define workspace model
ws_model = dict()
#robot radius
ws_model['robot_radius'] = 0.075

lines=[[[0,0],[0,20]],[[0,20],[20,20]],[[20,20],[20,0]],[[0,0],[20,0]],[[5,0],[5,10]],[[5,10],[15,10]]]
#obstacles format [x,y,thickness/2]
ws_model['circular_obstacles']=obstacles_adder(lines,0.2)

#dynamic obstacels format Inputs: [ [startx,starty], mode(right,down,left,up), speed,  thickness  ]
ws_model['dynamic_obs']=[ [[8,4],3,2.5,0.25]]

#------------------------------
#initialization for robot 
# position of [x,y]
# X = [[-0.5+1.0*i, 0.0] for i in range(7)] + [[-0.5+1.0*i, 5.0] for i in range(7)]
X = [[2.5,2.5],[18,18]]
# velocity of [vx,vy]
V = [[0,0] for i in range(len(X))]
# maximal velocity norm
V_max = [2.5 for i in range(len(X))]
#print("printing v_max",V_max)
# goal of [x,y]
# goal = [[5.5-1.0*i, 5.0] for i in range(7)] + [[5.5-1.0*i, 0.0] for i in range(7)]
goal = [[15,2.5],[7.5,2.5]]



#------------------------------
#simulation setup
# total simulation time (s)
total_time = 15
# simulation step
step = 0.01

#------------------------------
#simulation starts
t = 0

X_list = np.array(X)
start_step=0 #step for dynamic obstacles
while t*step < total_time:
    
    static_obs_length=len(ws_model['circular_obstacles']) #no of obstacles
    
    # compute desired vel to goal
    V_des = compute_V_des(X, goal, V_max)
    
    #function to update dynamic obstacles
    ws_model['circular_obstacles'],ws_model['dynamic_obs'],ws_model['dynamic_plotting']=update_dynamic_obs(ws_model['circular_obstacles'],ws_model['dynamic_obs'],start_step)
    start_step=step
    #compute the new velocities
    V = RVO_update(X, V_des, V, ws_model)

    # Removing old dynamic obstacles
    ws_model['circular_obstacles']=removing_old_dynamic_obs(ws_model['circular_obstacles'],static_obs_length)


    # updating robot positions
    for i in range(len(X)):
        X[i][0] += V[i][0]*step
        X[i][1] += V[i][1]*step
    #----------------------------------------
    # visualization
    

    if t%10 == 0:
        # saving the list of all the positions of both the robots from the beginning to the current iterations
        X_list = np.dstack((X_list,np.array(X)))

        # print("change")
        visualize_traj_dynamic(ws_model, X, X_list, V, goal, time=t*step, name='data/snap%s.jpg'%str(t/10))
        # print("change")
        #visualize_traj_dynamic(ws_model, X, V, goal, time=t*step, name='data/snap%s.png'%str(t/10))
    t += 1
    
