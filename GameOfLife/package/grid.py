import random
from package import cell

''''
Game of Life Rules
1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.
'''

class grid(object):
    
    def __init__(self, gridSize):
        self.gridSize = gridSize
        self.currentGrid = [] # Set empty
    
    def generateRandomGrid(self):
        ''' Generate a new random grid. Will randomly select between live and dead cells. X/Y size is determined by 'size' input'''
        randomGrid = []
        for y in range(self.gridSize):
            row = []
            for x in range(self.gridSize):
                row.append(cell.cell(random.choice([0,0,0,0,0,0,0,0,1]))) # Randomly select between '0': Dead and '1' Alive.
            randomGrid.append(row)
        self.currentGrid = randomGrid
        
    def setNeighbours(self):
        ''' Set's the neighbours of each cell in input grid. Discount neighbours which are outside the border.'''
        for y in range(len(self.currentGrid)):
            for x in range(len(self.currentGrid)):    
                allPossibleNeighbours = [[y - 1, x - 1],[y, x - 1],[y + 1, x - 1],[y - 1, x], # All possible surrounding neighbour coordinates
                                         [y + 1, x],[y -1, x + 1],[y, x + 1],[y + 1, x + 1]]
                for neighbour in allPossibleNeighbours:
                    if not any(n < 0 or n > len(self.currentGrid) - 1 for n in neighbour): # Remove coordinates that are < 0 and > max size.
                        self.currentGrid[y][x].neighbours.append(neighbour)        
    
    def getLiveNeighbourCount(self, y, x):
        ''' Get's the live neighbour count for the input cell coordinate. '''
        liveNeighbours = 0
        for neighbour in self.currentGrid[y][x].neighbours:
            if self.currentGrid[neighbour[0]][neighbour[1]].status == 1:
                liveNeighbours += 1
        return liveNeighbours
    
    def applyRule(self, targetCell, liveNeighbourCount):
        ''' Return's input cell next status based on it's current state and its live neighbour count. '''
        if targetCell == 0: # Cell is dead
            if liveNeighbourCount == 3: # 3 alive means the cell becomes alive
                return 1
            else: # Remains dead
                return 0
        else: # Cell is alive
            if liveNeighbourCount == 2: # 2 alive means the cell remains alive
                return 1
            elif liveNeighbourCount == 3: # 3 alive means the cell remains alive
                return 1
            else: # Cell dies
                return 0
            
    
    def getNextGrid(self):
        ''' Cycles through each cell in the grid and determines if they are alive or dead next grid'''
        newGrid = self.currentGrid
        for y in range(len(self.currentGrid)):
            for x in range(len(self.currentGrid)):
                liveNeighbourCount = self.getLiveNeighbourCount(y, x)
                nextStatus = self.applyRule(self.currentGrid[y][x].status, liveNeighbourCount)
                newGrid[y][x].status = nextStatus
        self.currentGrid = newGrid

            