import sys


from RVO import RVO_update, reach, compute_V_des, reach
from vis import visualize_traj_dynamic
from map_creator import straight_line_creator,obstacles_adder

#------------------------------
#define workspace model
ws_model = dict()
#robot radius
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
#------------------------------
#initialization for robot 
# position of [x,y]
# X = [[-0.5+1.0*i, 0.0] for i in range(7)] + [[-0.5+1.0*i, 5.0] for i in range(7)]
X=[[2.5,9.9],[17.5,10.1]]
# velocity of [vx,vy]
V = [[0,0] for i in range(len(X))]
# maximal velocity norm
V_max = [2.5 for i in range(len(X))]
#print("printing v_max",V_max)
# goal of [x,y]
# goal = [[5.5-1.0*i, 5.0] for i in range(7)] + [[5.5-1.0*i, 0.0] for i in range(7)]
goal=[[17.5,9.9],[2.5,10.1]]

# print(type(X),X)
# print(type(V),V)
# print(type(V_max),V_max)
# print(type(goal),goal)
#------------------------------
# # Hospital workspace model
# ws_model = dict()
# ws_model['robot_radius'] = 0.1
# ws_model['circular_obstacles'] = [[-0.3, 2, 0.3],[-0.3, 2.5, 0.3],[-0.3, 1.5, 0.3],[-0.3, 3, 0.3],[-0.3, 1, 0.3],[-0.3, 1.75, 0.3]]

# # Robot initialization
# X = [[0.5,0.5]]
# V = [[0,0] for i in range(len(X))]
# V_max = [1.0 for i in range(len(X))]
# goal=[[1,1]]
#------------------------------
#simulation setup
# total simulation time (s)
total_time = 15
# simulation step
step = 0.01

#------------------------------
#simulation starts
t = 0
while t*step < total_time:
    # compute desired vel to goal
    V_des = compute_V_des(X, goal, V_max)
    # compute the optimal vel to avoid collision
    V = RVO_update(X, V_des, V, ws_model)
    # update position
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
    
