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
-----
Features
-----
* Takes a 2D workspace with _any number_ of non-overlaping circular or square obstacles
* _Any number_ of dynamic agents with non-zero volume.
* Allow the choice of VO, RVO, HRVO.
* **Direct plug-and-play** and **fully integrate-able  with your control objective**, i.e., the output velocity is a minimal modification of the desired velocity.

```python
from your_module import compute_desired_V, Update_V
from RVO import RVO_update

# your control objective here 
V_desired = compute_desired_V(X, control_objective, V_max)

# plug in the RVO controller from this package
V = RVO_update(X, V_desired, workspace_model)

# let the robot move
X = Update_X(X, V, step)
```

* Scalable and fast, see examples below. 
* See [example.py](https://github.com/MengGuo/RVO_Py_MAS/blob/master/example.py) for test run. [[Video1]](https://vimeo.com/185405407), [[Video2]](https://vimeo.com/185408368)


----
References 
----
* Papers on [RVO](https://www.cs.unc.edu/~geom/RVO/icra2008.pdf), [HRVO](https://www.cs.unc.edu/~geom/RVO/icra2008.pdf)
* There are [Python bindings](https://github.com/sybrenstuvel/Python-RVO2) of the C++ implementation from the algorithm developers. For my purposes, the formality is too _heavy_ to be integrated into my own project, so I have my own try.
* This package does _not_ depend on the [Clearpath geometric package](http://pcl.intel-research.net/publications/clearpath_sca2009.pdf) to compute velocity obstacles.


----
Discussion
----
* For **very** clustered workspace with a large number of robots, you may need to limit the `maximal velocity` and use very `small step size`.
* You may add additional constraints in `RVO_update` such as the change rate of `V`, the lower bound of `V`.
* When applying this module to experimental robot control, you may need to set the **step size** higher due to hardware constraints.
* In most practical experiments, this scheme should still work by limiting the _maximal velocity_.  

