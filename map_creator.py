import numpy as np
import math

def straight_line_creator(start,end,thickness):
    "Generates coordinates to create a straight line given the start and endpoint"
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
    obstacles=[]
    for a_line in lines:
        new_obstacles=straight_line_creator(a_line[0],a_line[1],thickness)
        # print(new_obstacles)
        obstacles=obstacles+new_obstacles
    return obstacles

# print(straight_line_creator([0,0],[3,3],0.5))

lines=[[[0,0],[0,5]], [[0,0],[5,0]], [[5,0],[5,5]]]
obstacles=obstacles_adder(lines,0.5)

# print(obstacles)