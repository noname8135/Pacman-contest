# myTeam.py
# ---------
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

#python capture.py -r myTeam -redOpts first=ShuaiAgent,second=ShuaiAgent

from captureAgents import CaptureAgent
import random, time, util
from game import Directions
import game

#################
# Team creation #
#################

def createTeam(firstIndex, secondIndex, isRed,
               first = 'ShuaiAgent', second = 'ShuaiAgent'):
  """
  This function should return a list of two agents that will form the
  team, initialized using firstIndex and secondIndex as their agent
  index numbers.  isRed is True if the red team is being created, and
  will be False if the blue team is being created.

  As a potentially helpful development aid, this function can take
  additional string-valued keyword arguments ("first" and "second" are
  such arguments in the case of this function), which will come from
  the --redOpts and --blueOpts command-line arguments to capture.py.
  For the nightly contest, however, your team will be created without
  any extra arguments, so you should make sure that the default
  behavior is what you want for the nightly contest.
  """

  # The following line is an example only; feel free to change it.
  return [eval(first)(firstIndex), eval(second)(secondIndex)]

##########
# Agents #
##########

class ShuaiAgent(CaptureAgent):
  """
  A Dummy agent to serve as an example of the necessary agent structure.
  You should look at baselineTeam.py for more details about how to
  create an agent as this is the bare minimum.
  """

  def registerInitialState(self, gameState):
    """
    This method handles the initial setup of the
    agent to populate useful fields (such as what team
    we're on).

    A distanceCalculator instance caches the maze distances
    between each pair of positions, so your agents can use:
    self.distancer.getDistance(p1, p2)

    IMPORTANT: This method may run for at most 15 seconds.
    """
    self.opponents = self.getOpponents(gameState)
    '''
    Make sure you do not delete the following line. If you would like to
    use Manhattan distances instead of maze distances in order to save
    on initialization time, please take a look at
    CaptureAgent.registerInitialState in captureAgents.py.
    '''
    CaptureAgent.registerInitialState(self, gameState)

    #middle_line = # crossing this line will switch your agent

  def chooseAction(self, gameState):
    """
    Picks among actions randomly.
    """
    print gameState.data.timeleft
    actions = gameState.getLegalActions(self.index) #available actions
    #print actions  
    #print self.getFoodYouAreDefending(gameState)
    #print self.getOpponents(gameState), self.getTeam(gameState) #indice!! notice!!
    print self.index #0 2 = red, 1 3 = blue
    #print self.getCurrentObservation()
    print "getAgentDistance",gameState.getAgentDistances()
    print "AgentState self",gameState.getAgentState(self.index)
    print "Maze dis between two coord",self.getMazeDistance((8.0,1.0),(10.0,1.0))
    '''
    You should change this in your own agent.
    '''
    return random.choice(actions)

  def evaluate():
    return None


"""

  def final(self, gameState)

  def observationFunction(self, gameState):
    " Changing this won't affect pacclient.py, but will affect capture.py "
    return gameState.makeObservation(self.index)

  def debugDraw(self, cells, color, clear=False):
  def debugClear(self):

  #######################
  # Convenience Methods #
  #######################

  def getFood(self, gameState):
    Returns the food you're meant to eat. This is in the form of a matrix
    where m[x][y]=true if there is food you can eat in that square.

  def getFoodYouAreDefending(self, gameState):
    Returns the food you're meant to protect (i.e., that your opponent is
    supposed to eat). This is in the form of a matrix where m[x][y]=true if
    there is food at (x,y) that your opponent can eat.

  def getCapsules(self, gameState):

  def getCapsulesYouAreDefending(self, gameState):
    if self.red:
      return gameState.getRedCapsules()
    else:
      return gameState.getBlueCapsules()

  def getOpponents(self, gameState):
    Returns agent indices of your opponents. This is the list of the numbers
    of the agents (e.g., red might be "1,3,5")
    

  def getTeam(self, gameState):
    Returns agent indices of your team. This is the list of the numbers
    of the agents (e.g., red might be the list of 1,3,5)

  def getScore(self, gameState):
    Returns how much you are beating the other team by in the form of a number
    that is the difference between your score and the opponents score.  This number
    is negative if you're losing.

  def getMazeDistance(self, pos1, pos2):
    Returns the distance between two points; These are calculated using the provided distancer object.

  def getPreviousObservation(self):
    Returns the GameState object corresponding to the last state this agent saw
    (the observed state of the game last time this agent moved - this may not include
    all of your opponent's agent locations exactly).

  def getCurrentObservation(self):
    Returns the GameState object corresponding this agent's current observation
    (the observed state of the game - this may not include
    all of your opponent's agent locations exactly).
    
  def displayDistributionsOverPositions(self, distributions):
"""