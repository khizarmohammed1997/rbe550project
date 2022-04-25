from turtle import up
import numpy as np
import math

def straight_line_creator(start,end,thickness):
    "Generates coordinates to create a straight line given the start and endpoint. Inputs= [startx,starty] , [endx, endy] ,thickness"
    x_start=int(start[0])
    y_start=int(start[1])
    x_end=int(end[0])
    y_end=int(end[1])
    distance=math.sqrt(((x_end-x_start)**2)+((y_end-y_start)**2))
    
    N=int(distance/thickness)+1    
    split_y = np.linspace(y_start,y_end,num=N)
    split_x = np.linspace(x_start,x_end,num=N)
    thicks=[thickness/2 for i in range(len(split_y))]
    obstacles = list(list(x) for x in zip(split_x, split_y,thicks))

    return obstacles

def obstacles_adder(lines,thickness):
    "adds obstacels in the form of lines. Inputs: Lines=[[startx,starty],[endx,endy]] , thickness"
    obstacles=[]
    for a_line in lines:
        new_obstacles=straight_line_creator(a_line[0],a_line[1],thickness)
        # print(new_obstacles)
        obstacles=obstacles+new_obstacles
    return obstacles

def removing_old_dynamic_obs(model,n):
    "removes previosulu added static obstacles"
    return model[:n]

def update_dynamic_obs(old_model,dynamic_obs,time):
    "updates the workpace model to include dynamic obstacles: Inputs= static obstacles, dynamic obstacles, the timestep"
    i=0
    dynamic_plot=[]
    for obs in dynamic_obs:
        cur_x = obs[0][0]
        cur_y = obs[0][1]
        mode=obs[1]
        # end_x=obs[1][0]
        # end_y=obs[1][0]
        speed=obs[2]
        obs_thickness=obs[3]

        # if abs(cur_x-end_x)<0.1 and abs(cur_y-end_y)<0.1: 
        #     pass
        # else:
        if mode==1:
            cur_x= cur_x + speed*time
        elif mode==2:
            cur_y= cur_y - speed*time
        elif mode==3:
            cur_x= cur_x - speed*time
        elif mode==4:
            cur_y= cur_y + speed*time
        
        old_model=old_model+[[cur_x,cur_y,obs_thickness]]
        dynamic_obs[i][0]=[cur_x,cur_y]

        dynamic_plot.append([cur_x,cur_y,obs_thickness])
        i+=1
    return old_model,dynamic_obs,dynamic_plot

# lines=[[[5,7],[5,6]]]
# model=obstacles_adder(lines,0.5)
# d=[   [[0,0],1,0.5,0.5],   [[0,0],4,0.5,0.5]]  

# n=len(model)
# for t in np.arange(0,5,0.25):

#     print(t)
#     model,d,e=update_dynamic_obs(model,d,0.25)
#     print(model)
#     model=removing_old_dynamic_obs(model,n)
#     print(model)
#     print("\n")
# print(model)