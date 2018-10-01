from heapq import heappush, heappop # for priority queue
import math
import time
import random

class node:
    xPos = 0 # x position
    yPos = 0 # y position
    distance = 0 # total distance already travelled to reach the node
    priority = 0 # priority = distance + remaining distance estimate
    def __init__(self, xPos, yPos, distance, priority):
        self.xPos = xPos
        self.yPos = yPos
        self.distance = distance
        self.priority = priority
    def __lt__(self, other): # comparison method for priority queue
        return self.priority < other.priority
    def updatePriority(self, xDest, yDest):
        self.priority = self.distance + self.estimate(xDest, yDest) * 10 # A*
    # give higher priority to going straight instead of diagonally
    def nextMove(self, dirs, d): # d: direction to move
        if dirs == 8 and d % 2 != 0:
            self.distance += 14
        else:
            self.distance += 10
    # Estimation function for the remaining distance to the goal.
    def estimate(self, xDest, yDest):
        xd = xDest - self.xPos
        yd = yDest - self.yPos
        # Manhattan distance
        d = abs(xd) + abs(yd)      
        return(d)

# A-star algorithm.
# The path returned will be a string of digits of directions.
def pathFind(the_map, n, m, dirs, dx, dy, xA, yA, xB, yB):
    closed_nodes_map = [] # map of closed (tried-out) nodes
    open_nodes_map = [] # map of open (not-yet-tried) nodes
    dir_map = [] # map of dirs
    row = [0] * n
    for i in range(m): # create 2d arrays
        closed_nodes_map.append(list(row))
        open_nodes_map.append(list(row))
        dir_map.append(list(row))

    pq = [[], []] # priority queues of open (not-yet-tried) nodes
    pqi = 0 # priority queue index
    # create the start node and push into list of open nodes
    n0 = node(xA, yA, 0, 0)
    n0.updatePriority(xB, yB)
    heappush(pq[pqi], n0)
    open_nodes_map[yA][xA] = n0.priority # mark it on the open nodes map

    # A* search
    while len(pq[pqi]) > 0:
        # get the current node w/ the highest priority
        # from the list of open nodes
        n1 = pq[pqi][0] # top node
        n0 = node(n1.xPos, n1.yPos, n1.distance, n1.priority)
        x = n0.xPos
        y = n0.yPos
        heappop(pq[pqi]) # remove the node from the open list
        open_nodes_map[y][x] = 0
        closed_nodes_map[y][x] = 1 # mark it on the closed nodes map

        # quit searching when the goal is reached
        # if n0.estimate(xB, yB) == 0:
        if x == xB and y == yB:
            # generate the path from finish to start
            # by following the dirs
            path = ''
            while not (x == xA and y == yA):
                j = dir_map[y][x]
                c = str((j + dirs // 2) % dirs)
                path = c + path
                x += dx[j]
                y += dy[j]
            return path

        # generate moves (child nodes) in all possible dirs
        for i in range(dirs):
            xdx = x + dx[i]
            ydy = y + dy[i]
            if not (xdx < 0 or xdx > n-1 or ydy < 0 or ydy > m - 1
                    or the_map[ydy][xdx] == 1 or closed_nodes_map[ydy][xdx] == 1):
                # generate a child node
                m0 = node(xdx, ydy, n0.distance, n0.priority)
                m0.nextMove(dirs, i)
                m0.updatePriority(xB, yB)
                # if it is not in the open list then add into that
                if open_nodes_map[ydy][xdx] == 0:
                    open_nodes_map[ydy][xdx] = m0.priority
                    heappush(pq[pqi], m0)
                    # mark its parent node direction
                    dir_map[ydy][xdx] = (i + dirs // 2) % dirs
                elif open_nodes_map[ydy][xdx] > m0.priority:
                    # update the priority
                    open_nodes_map[ydy][xdx] = m0.priority
                    # update the parent direction
                    dir_map[ydy][xdx] = (i + dirs // 2) % dirs
                    # replace the node
                    # by emptying one pq to the other one
                    # except the node to be replaced will be ignored
                    # and the new node will be pushed in instead
                    while not (pq[pqi][0].xPos == xdx and pq[pqi][0].yPos == ydy):
                        heappush(pq[1 - pqi], pq[pqi][0])
                        heappop(pq[pqi])
                    heappop(pq[pqi]) # remove the target node
                    # empty the larger size priority queue to the smaller one
                    if len(pq[pqi]) > len(pq[1 - pqi]):
                        pqi = 1 - pqi
                    while len(pq[pqi]) > 0:
                        heappush(pq[1-pqi], pq[pqi][0])
                        heappop(pq[pqi])       
                    pqi = 1 - pqi
                    heappush(pq[pqi], m0) # add the better node instead
    return 'No route found' # if no route found

# MAIN
def searchBestRoute(mLarge,nHigh,maze,conDiagonal,start, end):
    n=mLarge # horizontal size of the map
    m=nHigh  # vertical size of the map
    objPoints=start+end  
    the_map=maze.copy()
    
    if conDiagonal:
        dirs = 8 # number of possible directions to move on the map
    else:
        dirs=4

    if dirs == 4:  #With NO Diagonals
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
    elif dirs == 8: #With Diagonales
        dx = [1, 1, 0, -1, -1, -1, 0, 1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]

    # fillout the map with a '+' pattern
    ##for x in range(n // 8, n * 7 // 8):
    ##    the_map[m // 2][x] = 1
    ##for y in range(m//8, m * 7 // 8):
    ##    the_map[y][n // 2] = 1

    # randomly select start and finish locations from a list
    ##sf = []
    ##sf.append((0, 0, n - 1, m - 1))
    ##sf.append((0, m - 1, n - 1, 0))
    ##sf.append((n // 2 - 1, m // 2 - 1, n // 2 + 1, m // 2 + 1))
    ##sf.append((n // 2 - 1, m // 2 + 1, n // 2 + 1, m // 2 - 1))
    ##sf.append((n // 2 - 1, 0, n // 2 + 1, m - 1))
    ##sf.append((n // 2 + 1, m - 1, n // 2 - 1, 0))
    ##sf.append((0, m / 2 - 1, n - 1, m // 2 + 1))
    ##sf.append((n - 1, m // 2 + 1, 0, m // 2 - 1))
    ##(xA, yA, xB, yB) = random.choice(sf)

    (xA, yA, xB, yB) = objPoints #This post cant be in the map as Obstacle


    print ('Map size (X,Y): ', n, m)
    print ('Start: ', xA, yA)
    print ('Finish: ', xB, yB)
    t = time.time()
    route = pathFind(the_map, n, m, dirs, dx, dy, yA, xA, yB, xB)
    print ('Time to generate the route (seconds): ', time.time() - t)
    print ('Route:')
    print (route)

    # mark the route on the map
    if len(route) > 0:
        x = xA
        y = yA
        the_map[y][x] = 2
        # print("Ruta:"+route)
        print("")
        for i in range(len(route)):
            j = int(route[i])
            x += dx[j] #Directions
            y += dy[j]
            the_map[y][x] = 5  #This is Route
        the_map[y][x] = 4 #Here is added Destiny
        #The current state of the_map hasta Start, End, Obstacles and Route
    print()
    #-----------------------------
    print("MAPA CREADO Y MODIFICADO--------------")
    for yyy in range(m):
        print(the_map[yyy])


    #-----------------------------
    # display the map with the route added
    print ('Map:')
    for y in range(m):
        for x in range(n):
            xy = the_map[y][x]
            if xy == 0:
                print ('.',end="") # space
            elif xy == 1:
                print ('O',end="") # obstacle
            elif xy == 2:
                print ('S',end="") # start
            elif xy == 5:
                print ('R',end="") # route
            elif xy == 4:
                print ('F',end="") # finish
        print()

    input('Press Enter...')
    return the_map


def generateRamdonMaze(m,n):
    maze = []
    row = [1] * n
    for i in range(m): # create empty map
        maze.append(list(row))

    #the_map [Fila]
    # the_map[5][5]=1
    # the_map[15][9]=1
    # the_map[15][10]=1
    # the_map[15][11]=1
    # the_map[15][12]=1
    # the_map[15][13]=1
    # the_map[15][14]=1
    # the_map[14][7]=1
    # the_map[10][7]=1

    # the_map[1][9]=1

    maze[1][1]=0
    maze[2][1]=0
    maze[3][1]=0
    maze[4][1]=0  #Obstacle
    maze[5][1]=0
    maze[5][1]=0
    maze[5][2]=0
    maze[5][3]=0
    maze[5][4]=0

    maze[1][2]=0
    maze[1][3]=0
    maze[0][3]=0
    maze[0][4]=0
    maze[0][5]=0
    maze[1][5]=0
    maze[2][5]=0
    maze[3][5]=0
    maze[3][6]=0
    maze[4][6]=0
    maze[5][6]=0
    maze[5][5]=0

    #Diagonal
    maze[2][2]=0
    maze[3][3]=0
    maze[4][4]=0
    return maze

maze=generateRamdonMaze(7,7)
# searchBestRoute(mLarge,nHigh,maze,conDiagonal,start, end):
# Return list of list where 0=Space 1=Obstacle 2=
#  4=End 5=Route founded
print("Res:\n"+str(searchBestRoute(7,7,maze,False,(1,1),(5,4))))