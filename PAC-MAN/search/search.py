# search.py
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST    
    
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    #return 
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    start = problem.getStartState()
    visited = []
    priorityQueue = util.PriorityQueue()

    priorityQueue.push((start, []), nullHeuristic)

    while not priorityQueue.isEmpty():
        node,path = priorityQueue.pop()

        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return path
            for succesor, direction, cost in problem.getSuccessors(node):
                if not succesor in visited:
                    newPath = path + [direction]
                    priorityQueue.push((succesor, newPath), problem.getCostOfActions(newPath))

    return path

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    visited = []
    queue = util.PriorityQueue()
    initialNode = problem.getStartState()
    queue.push((initialNode, []), heuristic(initialNode, problem))

    while not queue.isEmpty():
        
        currentNode, path = queue.pop()

        if problem.isGoalState(currentNode):
            return path

        visited.append(currentNode)
        
        for succesor, direction, cost in problem.getSuccessors(currentNode):
            if not succesor in visited:
                newPath = path + [direction]
                h = problem.getCostOfActions(newPath) + heuristic(succesor, problem)
                queue.push((succesor, newPath), h)
               
    return path

def hillClimbing(problem, heuristic=nullHeuristic):
    path = []
    currentNode = problem.getStartState()
    currentNode = ( (currentNode, []), heuristic(currentNode,problem))
    
    while True:
        custoEscolhido = currentNode[1]
        
        queue = util.PriorityQueue()
        
        for succesor, direction, cost in problem.getSuccessors(currentNode[0][0]):
           newPath = [direction]
           score = problem.getCostOfActions(newPath) + heuristic(succesor, problem)
           queue.push((succesor, newPath), score)
        
        #analisa primeiro da queue
        analisado = []
        analisado = queue.pop()

        custoAnalisado = problem.getCostOfActions(analisado[1]) + heuristic(analisado[0], problem) - 1
        
        if (custoEscolhido > custoAnalisado):
            path = path + (analisado[1])
            currentNode = ( (analisado[0], analisado[1]), custoAnalisado)
        else:
            break
                   
    return path

def simulatedAnnealing(problem):
    path = []
    # gets the initial node
    currentNode = problem.getStartState()
    actionCurrentNode = []
    Temp = 1.0
    alpha = 1.19

    while True:
        i = 0
        queue = util.Queue()
        for state, direction, cost in problem.getSuccessors(currentNode):
            newPath = [direction]
            queue.push((state, newPath))
            i = i + 1

        randomNext = random.randint(0, i-1)

        if randomNext > 0:
            for j in range(0, randomNext+1):
                nextNode, action = queue.pop()
        else:
            nextNode, action = queue.pop()

        E = problem.getCostOfActions(action) - problem.getCostOfActions(actionCurrentNode)
        if E < 0:
            currentNode = nextNode
            actionCurrentNode = action
            path = path + actionCurrentNode
        else:
            if math.exp(-E/T):
                currentNode = nextNode
                actionCurrentNode = action
                path = path + actionCurrentNode
        
        if problem.isGoalState(currentNode):
            return path

        Temp = Temp*alpha

    return path


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
