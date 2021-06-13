import curses
import random
from curses import textpad
import time
from time import sleep
from drawing import *
import sys




DIRECTIONS_LIST = [curses.KEY_RIGHT, curses.KEY_LEFT]

state = {'time': 0.0,
        'score':0}

    

def main(scr,canvas_height,canvas_width, difficulty_level):

    # Initialization
    scr.refresh()
    scr.nodelay(True)
    curses.curs_set(0)
    sh, sw = scr.getmaxyx()

    # Get the valid canvas width and heights
    canvas_width = int(canvas_width)
    canvas_height = int(canvas_height)
    if canvas_width > sw:
        canvas_width = sw
    if canvas_height > sh:
        canvas_height = sh

    canvas_queue  = []              # A queue to track obstacles' positions
    player_x = canvas_width//2      # Player's initial position

    while True:
        
        
        curses.halfdelay(DELAY)     # Set delay 
        key = scr.getch()           # This blocks (waits) until the time has elapsed,
                                    # or there is input to be handled
        scr.clear()                 # Clears the screen
        direction = None
        #Press q for quit
        scr.addstr(canvas_height + 2, 1, "Press Q for quit.")

        if key == ord("q"):
            break

        #Direction Check                          
        if key in DIRECTIONS_LIST:                
            direction = key

        if direction == curses.KEY_LEFT:            # This block checks 
            if player_x > 0:                        # in which direction 
                player_x -=1                        # the player goes
        elif direction == curses.KEY_RIGHT:         # The player is only allowed go left
            if player_x <= canvas_width - 1:        # or right
                player_x += 1
            
        # Check the last line
        if len(canvas_queue)==canvas_height:
            
            # Check if the game fail
            if  player_x in canvas_queue[-1]:

                # Draw FAIL sign
                scr.addstr(canvas_height-1,player_x, FAIL)
                draw_obstacles(canvas_queue,scr,canvas_width,canvas_height,difficulty_level)
                draw_player(scr, canvas_height, player_x)
                # Update and print score
                score_text = "Score: {}".format(state['score'])
                scr.addstr(canvas_height + 1, 1, score_text)
                scr.refresh()
                sleep(3)
                break

            #Update the score
            else:
                state['score']+=1

        draw_player(scr, canvas_height, player_x)  
        draw_obstacles(canvas_queue,scr,canvas_width,canvas_height,difficulty_level)
        scr.refresh()

        
        

        
        
def run(canvas_height,canvas_width, difficulty_level):                  # Function to run the game
    curses.wrapper(main,canvas_height,canvas_width, difficulty_level)