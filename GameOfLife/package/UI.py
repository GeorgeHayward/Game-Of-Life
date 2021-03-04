'''
The time complexity of this implementation is poor, will require some optimization
'''

import pygame

from package import grid

''' Constants'''
ALIVE_COLOUR = (0,255,0) # Green
SPACING = 10

'''Grid Setup'''
gridSize = 40
gridObject = grid.grid(gridSize)
gridObject.generateRandomGrid()
gridObject.setNeighbours()

pygame.init()
screen = pygame.display.set_mode([gridSize * SPACING, gridSize * SPACING]) # Drawing window
running = True # Run until user asks to quit

'''Main Loop'''
while running: 
        for event in pygame.event.get(): # User closes window
            if event.type == pygame.QUIT:
                running = False
        
        
        '''Get and display grid'''
        for y in range(len(gridObject.currentGrid)):
            for x in range(len(gridObject.currentGrid)):
                surf = pygame.Surface((gridSize*SPACING, gridSize*SPACING))
                if gridObject.currentGrid[y][x].status == 1: # Alive, draw green
                    surf.fill(ALIVE_COLOUR)
                screen.blit(surf, (x*SPACING, y*SPACING))
        
        gridObject.getNextGrid()        
        pygame.display.flip() # Flip display


    