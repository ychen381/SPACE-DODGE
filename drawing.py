
import random
from config import *

def draw_obstacles(canvas_array, scr,canvas_width,canvas_height, difficulty_level):

    start_X_list = []   #Random obstacle point list

    #Generate number of obstacles based on difficulty level
    num_obstacle = int(canvas_width * DIFFICULTY_CONST * int(difficulty_level))
    
    #Generate obstacle postion
    for i in range(num_obstacle):
        start_X_list.append(random.randint(1,canvas_width-1))
    canvas_array.insert(0,start_X_list)
    
    #Pop the last line if it is out of canvas
    if len(canvas_array)> canvas_height:
        canvas_array.pop()

    # Draw obstacles on the cancas
    for i in range(len(canvas_array)):
        for j in canvas_array[i]:
            scr.addstr(i,j,OBSTACLE)



def draw_player(scr, canvas_height, player_x):
    scr.addstr(canvas_height,player_x,PLAYER)

