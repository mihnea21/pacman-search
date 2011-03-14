"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 74].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.18].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
    
  from game import Directions

  #test the initial state
  if problem.isGoalState(problem.getStartState()):return [Directions.STOP]
  
  #using stack to store the successors 
  successorStack = util.Stack()
  
  #store the path from the initial state to the goal state
  finalDirectionArray = []
  
  #store the node which has already visited
  visitedNodeArray = []
  
  #store each node's previous node
  previousNodeDict = {}
  
  #store the direction of reaching this node
  directionDict = {}
  
  #store the goal State
  goalState = []
  
  #store the node array that from the start to the goal
  finalNodeArray = []
  
  
  #initial some data structure
  visitedNodeArray.append(problem.getStartState())
  
  for item in problem.getSuccessors(problem.getStartState()):
      previousNodeDict[item[0]] = problem.getStartState()
      directionDict[item[0]] = item[1]
      successorStack.push(item)
      

  #begin DFS Search
  while not successorStack.isEmpty():
      
      #get the top element of the stack
      tempSuccessor = successorStack.pop()
      visitedNodeArray.append(tempSuccessor[0])
      
      #decide whether this is a goal or not
      if(problem.isGoalState(tempSuccessor[0])):
          goalState = tempSuccessor[0]
          break

      #put the top node's successors into the stack
      for item in problem.getSuccessors(tempSuccessor[0]):
          if item[0] not in visitedNodeArray and item[0] not in previousNodeDict.keys():
              successorStack.push(item)
              previousNodeDict[item[0]] = tempSuccessor[0]
              directionDict[item[0]] = item[1]
              
  #reconstruct the node array from the start to the goal
  while True:
      finalNodeArray.insert(0, goalState)
      if previousNodeDict[goalState] != problem.getStartState():
          goalState = previousNodeDict[goalState]
      else:       
          break
      
  #reconstruct the direction array from the start to the goal 
  for item in finalNodeArray:
      finalDirectionArray.append(directionDict[item])
      
  return finalDirectionArray




def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 74]"
  "*** YOUR CODE HERE ***"
  
  from game import Directions

  #test the initial state
  if problem.isGoalState(problem.getStartState()):return [Directions.STOP]
  
  #using Queue to store the successors 
  successorQueue = util.Queue()
  
  #store the path from the initial state to the goal state
  finalDirectionArray = []
  
  #store the node which has already visited
  visitedNodeArray = []
  
  #store each node's previous node
  previousNodeDict = {}
  
  #store the direction of reaching this node
  directionDict = {}
  
  #store the goal State
  goalState = []
  
  #store the node array that from the start to the goal
  finalNodeArray = []
  
  
  #initial some data structure
  visitedNodeArray.append(problem.getStartState())
  
  for item in problem.getSuccessors(problem.getStartState()):
      previousNodeDict[item[0]] = problem.getStartState()
      directionDict[item[0]] = item[1]
      successorQueue.push(item)
      

  #begin BFS Search
  while not successorQueue.isEmpty():
      
      #get the top element of the Queue
      tempSuccessor = successorQueue.pop()
      visitedNodeArray.append(tempSuccessor[0])
      
      #decide whether this is a goal or not
      if(problem.isGoalState(tempSuccessor[0])):
          goalState = tempSuccessor[0]
          break
      

      #put the first node's successors into the queue
      for item in problem.getSuccessors(tempSuccessor[0]):
          if item[0] not in visitedNodeArray and item[0] not in previousNodeDict.keys():
              successorQueue.push(item)
              previousNodeDict[item[0]] = tempSuccessor[0]
              directionDict[item[0]] = item[1]
              
  #reconstruct the node array from the start to the goal
  while True:
      finalNodeArray.insert(0, goalState)
      if previousNodeDict[goalState] != problem.getStartState():
          goalState = previousNodeDict[goalState]
      else:       
          break
      
  #reconstruct the direction array from the start to the goal 
  for item in finalNodeArray:
      finalDirectionArray.append(directionDict[item])
      
  return finalDirectionArray
          
        
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  
  from game import Directions

  #test the initial state
  if problem.isGoalState(problem.getStartState()):return [Directions.STOP]
  
  #using PriorityQueue to store the successors 
  successorPriorityQueue = util.PriorityQueue()
  
  #store the path from the initial state to the goal state
  finalDirectionArray = []
  
  #store the node which has already visited
  visitedNodeArray = []
  
  #store each node's previous node
  previousNodeDict = {}
  
  #store the direction of reaching this node
  directionDict = {}
  
  #store the goal State
  goalState = []
  
  #store the node array that from the start to the goal
  finalNodeArray = []
  
  
  #initial some data structure
  visitedNodeArray.append(problem.getStartState())
  
  for item in problem.getSuccessors(problem.getStartState()):
      previousNodeDict[item[0]] = problem.getStartState()
      directionDict[item[0]] = item[1]
      successorPriorityQueue.push(item,problem.getCostOfActions([item[1]]))
      

  #begin UCS Search
  while not successorPriorityQueue.isEmpty():
      
      #get the top element of the PriorityQueue
      tempSuccessor = successorPriorityQueue.pop()
      visitedNodeArray.append(tempSuccessor[0])
      
      #decide whether this is a goal or not
      if(problem.isGoalState(tempSuccessor[0])):
          goalState = tempSuccessor[0]
          break

      #put the first node's successors into the queue
      for item in problem.getSuccessors(tempSuccessor[0]):
          if item[0] not in visitedNodeArray and item[0] not in previousNodeDict.keys():
              previousNodeDict[item[0]] = tempSuccessor[0]
              directionDict[item[0]] = item[1]
              #get the direction array from the start to the node item
              nodeToStartArray = []
              directionToStartArray = []
              iter = item[0]
              while True:
                  nodeToStartArray.insert(0,iter)
                  if previousNodeDict[iter] != problem.getStartState():
                      iter = previousNodeDict[iter]
                  else:
                      break
              for eachNode in nodeToStartArray:
                  directionToStartArray.append(directionDict[eachNode])
              #put the node and its cost into the PriorityQueue
              successorPriorityQueue.push(item,problem.getCostOfActions(directionToStartArray))
              
  #reconstruct the node array from the start to the goal
  while True:
      finalNodeArray.insert(0, goalState)
      if previousNodeDict[goalState] != problem.getStartState():
          goalState = previousNodeDict[goalState]
      else:       
          break
      
  #reconstruct the direction array from the start to the goal 
  for item in finalNodeArray:
      finalDirectionArray.append(directionDict[item])
      
  return finalDirectionArray
  

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  
  from game import Directions

  #test the initial state
  if problem.isGoalState(problem.getStartState()):return [Directions.STOP]
  
  #using PriorityQueue to store the successors 
  successorPriorityQueue = util.PriorityQueue()
  
  #store the path from the initial state to the goal state
  finalDirectionArray = []
  
  #store the node which has already visited
  visitedNodeArray = []
  
  #store each node's previous node
  previousNodeDict = {}
  
  #store the direction of reaching this node
  directionDict = {}
  
  #store the goal State
  goalState = []
  
  #store the node array that from the start to the goal
  finalNodeArray = []
  
  
  #initial some data structure
  visitedNodeArray.append(problem.getStartState())
  
  for item in problem.getSuccessors(problem.getStartState()):
      previousNodeDict[item[0]] = problem.getStartState()
      directionDict[item[0]] = item[1]
      successorPriorityQueue.push(item,problem.getCostOfActions([item[1]])+heuristic(item[0],problem))
      

  #begin A-STAR Search
  while not successorPriorityQueue.isEmpty():
      
      #get the top element of the PriorityQueue
      tempSuccessor = successorPriorityQueue.pop()
      visitedNodeArray.append(tempSuccessor[0])

      #decide whether this is a goal or not
      if(problem.isGoalState(tempSuccessor[0])):
          goalState = tempSuccessor[0]
          break

      #put the first node's successors into the queue
      for item in problem.getSuccessors(tempSuccessor[0]):
          if item[0] not in visitedNodeArray and item[0] not in previousNodeDict.keys():
              previousNodeDict[item[0]] = tempSuccessor[0]
              directionDict[item[0]] = item[1]
              #get the direction array from the start to the node item
              nodeToStartArray = []
              directionToStartArray = []
              iter = item[0]
              while True:
                  nodeToStartArray.insert(0,iter)
                  if previousNodeDict[iter] != problem.getStartState():
                      iter = previousNodeDict[iter]
                  else:
                      break
              for eachNode in nodeToStartArray:
                  directionToStartArray.append(directionDict[eachNode])
              #put the node and its cost into the PriorityQueue
              successorPriorityQueue.push(item,problem.getCostOfActions(directionToStartArray)+heuristic(item[0],problem))
              
  #reconstruct the node array from the start to the goal
  while True:
      finalNodeArray.insert(0, goalState)
      if previousNodeDict[goalState] != problem.getStartState():
          goalState = previousNodeDict[goalState]
      else:       
          break
      
  #reconstruct the direction array from the start to the goal 
  for item in finalNodeArray:
      finalDirectionArray.append(directionDict[item])
      
  return finalDirectionArray
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch