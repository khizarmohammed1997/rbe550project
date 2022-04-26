import numpy as np
from RRT_project import RRT
# from types import DynamicClassAttribute
import matplotlib
import matplotlib.pyplot as pyplot
from matplotlib.path import Path
import matplotlib.patches as patches
from matplotlib.patches import Polygon
import matplotlib.cm as cmx
import matplotlib.colors as colors
from map_creator import update_dynamic_obs,obstacles_adder
from math import pi as PI
from math import atan2, sin, cos, sqrt
from PIL import Image

def load_map(file_path, resolution_scale):
    ''' Load map from an image and return a 2D binary numpy array
        where 0 represents obstacles and 1 represents free space
    '''
    # Load the image with grayscale
    img = Image.open(file_path).convert('L')
    # Rescale the image
    size_x, size_y = img.size
    print("image size x",size_x)
    print("image size y",size_y)
    new_x, new_y  = int(size_x*resolution_scale), int(size_y*resolution_scale)
    img = img.resize((new_x, new_y), Image.ANTIALIAS)
    map_array = np.asarray(img, dtype='uint8')

    # Get bianry image
    threshold = 127
    map_array = 1 * (map_array > threshold)

    # Result 2D numpy array
    return map_array


def visualize_static_map(ws_model,name):
    figure = pyplot.figure()
    ax = figure.add_subplot(1,1,1)
    
    # plot obstacles
    for hole in ws_model['circular_obstacles']:
        srec = matplotlib.patches.Rectangle(
                (hole[0]-hole[2], hole[1]-hole[2]),
                2*hole[2], 2*hole[2],
                facecolor= 'black',
                fill = True,
                alpha=1)
        ax.add_patch(srec)

    #plot dynamic obstacles
    for hole in ws_model['dynamic_plotting']:
        arec = matplotlib.patches.Rectangle(
                (hole[0]-hole[2], hole[1]-hole[2]),
                2*hole[2], 2*hole[2],
                facecolor= 'black',
                fill = True,
                alpha=1)
        
        ax.add_patch(arec)

    # ---set axes ---
    ax.set_aspect('equal')
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 20)
    
    # ax.axis["left"].set_visible(False)
    # ax.axis["top"].set_visible(False)
    w = ax.get_xaxis()
    w.set_visible(False)
    # ax.axes.get_xaxis().set_visible(False)
    # figure.axes.get_yaxis().set_visible(False)
    # ax.set_xlabel(r'$x (m)$')
    # ax.set_ylabel(r'$y (m)$')
    ax.grid(False)

    pyplot.savefig(name, dpi = 200)
    pyplot.savefig(name,bbox_inches='tight')
    # pyplot.show()

    return figure
#-------------------------------------------------
#Hospital 1
# lines_borders=[  [[0,0],[0,20]], [[0,20],[20,20]],  [[20,20],[20,0]],  [[0,0],[20,0]] ]
# lines_room1=[  [[5,0],[5,8.75]], [[5,8.75],[13.5,8.75]], [[16.5,8.75],[20,8.75]] ]
# lines_room2=[  [[5,20],[5,11.25]],  [[5,11.25],[9.5,11.25]],  [[12.5,11.25],[20,11.25]]  ]
# all_lines=lines_borders+lines_room1+lines_room2

# ws_model = dict()
# ws_model['robot_radius'] = 0.25
# ws_model['circular_obstacles']=obstacles_adder(all_lines,0.5)
# ws_model['dynamic_obs']=[ [[8,4],3,2.5,0.25]]
# ws_model['circular_obstacles'],ws_model['dynamic_obs'],ws_model['dynamic_plotting']=update_dynamic_obs(ws_model['circular_obstacles'],ws_model['dynamic_obs'],0)



def global_path_generator(ws_model,map_resolution,start,goal):
    'generares a global map form the obstacles and dynamic obstacles created INPUTS= model, resolution, start(tuple), goal(tuple)'
    # visualize_static_map(ws_model,"test_map1")
    map_array = load_map("test_map1.png", map_resolution)
    scale_x=20/len(map_array[1])
    scale_y=20/len(map_array[0])
    print(map_array)
    print("x length",len(map_array))
    print("x length",len(map_array[0]))

    # Planning class
    RRT_planner = RRT(map_array, start, goal)
    # path = RRT_planner.RRT(n_pts=2000)
    path,map_size = RRT_planner.RRT_star(n_pts=1000)
    
    return path,scale_x,scale_y

# ws_model = dict()
# lines=[[[5,7],[5,3]]]
# ws_model['circular_obstacles']=obstacles_adder(lines,0.5)
# ws_model['dynamic_obs']=[ [[8,4],3,2.5,0.25]]
# ws_model['circular_obstacles'],ws_model['dynamic_obs'],ws_model['dynamic_plotting']=update_dynamic_obs(ws_model['circular_obstacles'],ws_model['dynamic_obs'],0)



# 'C:\Users\khiza\OneDrive\Documents\GitHub\-Reciprocal-Velocity-Obstacle--RVO-'
# visualize_static_map(ws_model,"test_map")
# map_array = load_map("modified_test_map.jpg", 0.3)
# print(map_array)
# print("x length",len(map_array))
# print("x length",len(map_array[0]))

# start = (50,50)
# goal  = (50,200)



# # Planning class

# RRT_planner = RRT(map_array, start, goal)
# RRT_planner.RRT(n_pts=1000)