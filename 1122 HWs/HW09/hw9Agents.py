# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
This file contains all of the agents that can be selected to control Pacman.  To
select an agent, use the '-p' option when running pacman.py.  Arguments can be
passed to your agent using '-a'.  For example, to load a SearchAgent that uses
depth first search (dfs), run the following command:

> python pacman.py -p SearchAgent -a fn=depthFirstSearch

"""

from game import Directions
from game import Agent
from game import Actions
import util
import time
import search
import random

# this is an example Agent
class GoWESTAgent(Agent):
    "An agent that goes WEST until it can't."

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        if Directions.WEST in state.getLegalPacmanActions():
            return Directions.WEST
        else:
            return Directions.STOP

# Part 1
# implement this
class RandomAgent(Agent):
    def __init__(self):
        # This is the constructor. You can initialize data here if you want.
        # You do not need to write anything here if you don't want to.
        pass

    def getAction(self, state):
        return random.choice(state.getLegalPacmanActions())
        #pass

# Part 2
# implement this
class MyAgent(Agent):
    def __init__(self): 
        self.current_direction = Directions.NORTH    
        # This is the constructor. You can initialize data here if you want.	
        # You do not need to write anything here if you don't want to.
	#pass

    def getAction(self, state):
        position = state.getPacmanPosition()
        food = state.getFood()
        cap_pos = state.getCapsules()

        up = (position[0], position[1]+1)
        right = (position[0]+1, position[1])
        down = (position[0], position[1]-1)
        left = (position[0]-1, position[1])
        if up in cap_pos:
            self.current_direction=Directions.NORTH
            return Directions.NORTH
        elif right in cap_pos:
            self.current_direction=Directions.EAST
            return Directions.EAST
        elif down in cap_pos:
            self.current_direction=Directions.SOUTH
            return Directions.SOUTH
        elif left in cap_pos:
            self.current_direction=Directions.WEST
            return Directions.WEST
        if food[up[0]][up[1]] == True:
            self.current_direction=Directions.NORTH
            return Directions.NORTH
        elif food[right[0]][right[1]] == True:
            self.current_direction=Directions.EAST
            return Directions.EAST
        elif food[down[0]][down[1]] == True:
            self.current_direction=Directions.SOUTH
            return Directions.SOUTH
        elif food[left[0]][left[1]] == True:
            self.current_direction=Directions.WEST
            return Directions.WEST
        if self.current_direction in state.getLegalPacmanActions():
            return self.current_direction
        else:
            self.current_direction = random.choice(state.getLegalPacmanActions())
            while(self.current_direction==Directions.STOP):
                self.current_direction = random.choice(state.getLegalPacmanActions())
            return self.current_direction
        #pass

