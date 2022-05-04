# Collision Avoidance in Dynamic Environment
## RBE550 - Motion Planning Project

-----
## Description

The following project is the implementation of collision avoidance in Dynamic environment using the global-local planner integration. The project consist of two stages of implementation.
1. Stage - I
2. Stage - II

## Stage - I
In stage -I, the python implementation of global and local planner has been done. For global planner the RRT* algorithm has been implemented. The output of the implementation are as follows:

This is the implementation of RRT* for the first scenario:
<p align="center" width="100%">
    <img width="33%" src=./results/RRT-star1.png> 
</p>

This is the implementation of RRT* for the second scenario:
<p align="center" width="100%">
    <img width="33%" src=./results/RRT-star2.png> 
</p>

In case of the local planner, three variants of velocity obstacle has been implemented. They are as follows:
1. Standard Velocity Obstacle
2. Reciprocal Velocity Obstacle
3. Hybrid Reciprocal Velocity Obstacle

#### 1. Standard Velocity Obstacle
In the below scenario, a simple velocity obstacle is implemented for four robots. The circle around the robot represents the horizon for the local planner. Within this region, the local planner alters the path of the robot with respect to the trajectory of the obstacle.

<p align="center" width="100%">
    <img width="33%" src=./results/VO_dance.gif> 
</p>

#### 2. Reciprocal Velocity Obstacle 
In this implementation, the major issue of the reciprocal velcoity obstacle algorithm has been shown. The four robot converge into an oscillatory motion resulting in the "Reciprocal Dance".
<p align="center" width="100%">
    <img width="33%" src=./results/RVO_Dance.gif> 
</p>

#### 3. Hybrid Reciprocal Velocity Obstacle 
In the below scenario the HRVO implementation has been shown. The issue of Reciprocal dance has been resolved and it has been demosntrated in the below video.
<p align="center" width="100%">
    <img width="33%" src=./results/HVO.gif> 
</p>

### Integration
The complete integration of the global and local planner implementation has been show below:
<p align="center" width="100%">
    <img width="33%" src=./results/stage1.gif> 
</p>
The two robots follows the path from the global planner. When encountered by the dynamic obstacles the local planner reacts in response, thus avoiding the collision with the obstacles. 


## How to run the code

#### STAGE 1
Github reference for Stage 1:https://github.com/MengGuo/RVO_Py_MAS 
We have referenced our work on this github link. We have added dynamic obstacles along with a combination of a local and global planner. Our work can be generalized for different maps and different global algorithms as well, just based on a black and white picture of the static map. In order to do so, modifications are required to functions we have written on map_generator.py  and map_creator.py


#### To run the combined local and global planner:
Run hospital_1.py file
This file directly runs the combined local + global planne on test_map1
The program saves each frame in the resulting simulation as a picture in the Data folder.
In order to view the video you can run video creator file, which will compile all the images into a video


#### To make customized maps:
In hospital_1.py, refer to the MAP DEFINER code block. Here  you can manually define lines based on start and end points  to make a static map.


#### To run only the global algorithm to get a path:
Currently we have manually input  a reduced path from the global planner into the local planner. In order to run the global planner and to integrate with local planner uncomment the “Globalpath converter” to run the global path '''