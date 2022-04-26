import numpy as np 

def pathway(path,horizon):
    for i in range(len(path)):
        x = path[i][0]
        y = path[i][1]
        path[i][0] = x + 0.5
        path[i][1] = y + 0.5
    print(path)
    start   = [path[0]]
    goal    = [path[horizon]]
    for i in range(horizon,len(path),horizon):
        if (i+horizon) < len(path) and i < len(path):
            start.append(path[i])
            goal.append(path[i+horizon])
        else:
            start.append(goal[-1])
            goal.append(path[-1])
    return start, goal


horizon = 3
path = [[0,0],[1,1],[1,2],[1,3],[2,3],[3,3],[4,4],[4,5],[5,5]]
start,goal = pathway(path,horizon)
print("Start :")
print(start)
print("Start length:")
print(len(start))

print("Goal :")
print(goal)
print("Goal length:")
print(len(goal))
    

