import time
from typing import Dict, List, Tuple
from agent import Agent
from planner import Planner
from visualizer import Visualizer
import random
import map_reader

start_time = time.time()
grid_size_x, grid_size_y, static_obstacles, end_points = map_reader.load_file('./map/kvc.map')

# grid_size_x = 21
# grid_size_y = 6
# static_obstacles = []
# end_points = []
# for x in range(grid_size_x):
#     for y in range(grid_size_y):
#         if x%2==1 and 1<=y<=4:
#             static_obstacles.append((x, y))
#         else:
#             end_points.append((x, y))


agent_num = 5
agents = [Agent(i) for i in range(agent_num)]
planner = Planner(agents, grid_size_x, grid_size_y, static_obstacles)
intermediate_time = time.time()
print(f"create planner: {intermediate_time-start_time}")


starts = {}
goals = {}
for agent in agents:
    start_pos = random.choice(end_points)
    starts[agent] = start_pos
    end_points.remove(start_pos)
    #
    goal_pos = random.choice(end_points)
    goals[agent] = goal_pos
    end_points.remove(goal_pos)
    #
print(starts, goals)

solution = planner.plan(starts, goals, True)

end_time = time.time()
print(f"calculate solution: {end_time-intermediate_time}")

visualizer = Visualizer(grid_size_x, grid_size_y, static_obstacles, solution)
visualizer.plot()

