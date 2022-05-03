import sys
import numpy as np

from cv2 import circle


from RVO import RVO_update, reach, compute_V_des, reach
from vis import visualize_traj_dynamic
from map_creator import obstacles_adder,removing_old_dynamic_obs,update_dynamic_obs,pathway,updated_goals,start_goal_dis
from map_generator import global_path_generator
#--------------------------------------------------------
#Hospital map 1
lines_borders=[  [[0,0],[0,20]], [[0,20],[20,20]],  [[20,20],[20,0]],  [[0,0],[20,0]] ]
lines_room1=[  [[5,0],[5,8.75]], [[5,8.75],[13.5,8.75]], [[16.5,8.75],[20,8.75]] ]
lines_room2=[  [[5,20],[5,11.25]],  [[5,11.25],[13.5,11.25]],  [[16.5,11.25],[20,11.25]]  ]
all_lines=lines_borders+lines_room1+lines_room2

ws_model = dict()
ws_model['robot_radius'] = 0.25
ws_model['circular_obstacles']=obstacles_adder(all_lines,0.5)
ws_model['dynamic_obs']=[ [[1.866,10],2,2.5,0.25],[[17,10],3,2.5,0.25] ]
ws_model['circular_obstacles'],ws_model['dynamic_obs'],ws_model['dynamic_plotting']=update_dynamic_obs(ws_model['circular_obstacles'],ws_model['dynamic_obs'],0)


#------------------------------
#initialization for robot 

X = [[1.75,1.75],[1.75,18]]
# velocity of [vx,vy]
V = [[0,0] for i in range(len(X))]
# maximal velocity norm
V_max = [4 for i in range(len(X))]
goal = [[15,18],[15,1.75]]

reduced_paths=[]

# for i in range(len(X)):

#     start_i=X[i]
#     goal_i=goal[i]

#     path,scale_x,scale_y=global_path_generator(ws_model,0.5,start_i,goal_i)
#     print("len of unmodified path",len(path))
#     start,goals=pathway(path,5)
#     print("len of modified path",len(start))
#     print("path successful")
#     reduced_paths.append(goals)
# reduced_paths=(np.array(reduced_paths)*scale_x)
# print("reducecd_path",reduced_paths)

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
i_local=0

reduced_paths=[[[2.66,5.3],[3.75,9.33],[8.5,10.66],[14.4,12],[15,14.56],[15,18]], \
    [[2.66,14.56],[3.75,12],[8.5,10.66],[14.4,9.33],[15,5.6],[15,1.75]]]
# print("entering while loop")
path_i=0
path_j=0
goal_1=[reduced_paths[0][0]]
goal_2=[reduced_paths[1][0]]
while t*step < total_time:
    distances=start_goal_dis(list(X),list(goal))


    if distances[0]<0.1:
        if path_i<=len(reduced_paths[0]):
            path_i+=1
        goal_1=updated_goals(reduced_paths,path_i,0)
    if distances[0]<0.1:
        if path_j<=len(reduced_paths[1]):
            path_j+=1
        goal_2=updated_goals(reduced_paths,path_j,1)
    goal=goal_1+goal_2
    
    static_obs_length=len(ws_model['circular_obstacles']) #no of obstacles
    # print("goals",goal)
    
    # compute desired vel to goal
    V_des = compute_V_des(X, goal, V_max)
    # print("crossed_computed_v_des")
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