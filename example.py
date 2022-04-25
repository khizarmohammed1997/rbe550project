import sys

from cv2 import circle


from RVO import RVO_update, reach, compute_V_des, reach
from vis import visualize_traj_dynamic
from map_creator import obstacles_adder,removing_old_dynamic_obs,update_dynamic_obs

#------------------------------
#define workspace model
ws_model = dict()
#robot radius
<<<<<<< Updated upstream
ws_model['robot_radius'] = 0.1
#circular obstacles, format [x,y,rad]
# no obstacles
#ws_model['circular_obstacles'] = []
# with obstacles
# ws_model['circular_obstacles'] = [[-0.3, 2.5, 0.3], [1.5, 2.5, 0.3], [3.3, 2.5, 0.3], [5.1, 2.5, 0.3]]
# ws_model['circular_obstacles'] = [[-0.3, 2, 0.3],[-0.3, 2.5, 0.3],[-0.3, 1.5, 0.3],[-0.3, 3, 0.3],[-0.3, 1, 0.3],[-0.3, 1.75, 0.3]]


lines=[[[0,8],[20,8]],[[0,12],[20,12]]]

ws_model['circular_obstacles']=obstacles_adder(lines,0.4)

# rectangular boundary, format [x,y,width/2,heigth/2]
# ws_model['boundary'] = [[3,3,10]] 
=======
ws_model['robot_radius'] = 0.075

lines=[[[5,7],[5,3]]]
#obstacles format [x,y,thickness/2]
ws_model['circular_obstacles']=[]

#dynamic obstacels format Inputs: [ [startx,starty], mode(right,down,left,up), speed,  thickness  ]
ws_model['dynamic_obs']=[ [[8,4],3,2.5,0.25]]

>>>>>>> Stashed changes
#------------------------------
#initialization for robot 
# position of [x,y]
# X = [[-0.5+1.0*i, 0.0] for i in range(7)] + [[-0.5+1.0*i, 5.0] for i in range(7)]
<<<<<<< Updated upstream
X=[[2.5,9.9],[17.5,10.1]]
=======
X=[[2,4],[2,7]]
>>>>>>> Stashed changes
# velocity of [vx,vy]
V = [[0,0] for i in range(len(X))]
# maximal velocity norm
V_max = [2.5 for i in range(len(X))]
#print("printing v_max",V_max)
# goal of [x,y]
# goal = [[5.5-1.0*i, 5.0] for i in range(7)] + [[5.5-1.0*i, 0.0] for i in range(7)]
<<<<<<< Updated upstream
goal=[[17.5,9.9],[2.5,10.1]]
=======
goal=[[8,4],[2,7]]


>>>>>>> Stashed changes

#------------------------------
#simulation setup
# total simulation time (s)
total_time = 15
# simulation step
step = 0.01

#------------------------------
#simulation starts
t = 0


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
        # print("change")
        visualize_traj_dynamic(ws_model, X, V, goal, time=t*step, name='data/snap%s.jpg'%str(t/10))
        # print("change")
        #visualize_traj_dynamic(ws_model, X, V, goal, time=t*step, name='data/snap%s.png'%str(t/10))
    t += 1
    
