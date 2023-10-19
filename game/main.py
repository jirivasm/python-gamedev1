import asyncio
import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
dt = 0


def drawGrid():
    for x in range(1,3):
        pygame.draw.line(screen,(0,255,0),(0,x * screen.get_height()/3),(screen.get_width(), x * screen.get_height()/3),4)
        pygame.draw.line(screen,(0,255,0),(0,x * screen.get_height()/3),(screen.get_width(), x * screen.get_height()/3),4)
        pygame.draw.line(screen,(0,255,0),(x * screen.get_width()/3,0),(x * screen.get_width()/3, screen.get_height()),4)
        pygame.draw.line(screen,(0,255,0),(x * screen.get_width()/3,0),(x * screen.get_width()/3, screen.get_height()),4)



 
myGrid = []
#Top Left
myGrid.append(pygame.Rect(0,0,screen.get_width()/3,screen.get_height()/3))
#Top Middle
myGrid.append(pygame.Rect(screen.get_width()/3,0,screen.get_width()/3,screen.get_height()/3))
#top Right
myGrid.append(pygame.Rect(2*screen.get_width()/3,0,screen.get_width()/3,screen.get_height()/3))
#middle Left
myGrid.append(pygame.Rect(0,screen.get_height()/3,screen.get_width()/3,screen.get_height()/3))
#Middle Middle
myGrid.append(pygame.Rect(screen.get_width()/3,screen.get_height()/3,screen.get_width()/3,screen.get_height()/3))
#Middle Right
myGrid.append(pygame.Rect(2*screen.get_width()/3,screen.get_height()/3,screen.get_width()/3,screen.get_height()/3))
#Low Left
myGrid.append(pygame.Rect(0,2*screen.get_height()/3,screen.get_width()/3,screen.get_height()/3))
#Low Middle
myGrid.append(pygame.Rect(screen.get_width()/3,2*screen.get_height()/3,screen.get_width()/3,screen.get_height()/3))
#Low Right
myGrid.append(pygame.Rect(2*screen.get_width()/3,2*screen.get_height()/3,screen.get_width()/3,screen.get_height()/3))


async def main():
    isRunning = True
    while isRunning:
        #handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        #filling screen
        screen.fill("blue")
        drawGrid()
        
        mouse_pos = pygame.mouse.get_pos(); 
        
        #coloring according to mouse position
        if mouse_pos[0]<screen.get_width()/3 and mouse_pos[1]<screen.get_height()/3:
            pygame.draw.rect(screen,(0,0,100),myGrid[0])
        elif mouse_pos[0]>screen.get_width()/3 and mouse_pos[0]<2*screen.get_width()/3 and mouse_pos[1]< screen.get_height()/3:
            pygame.draw.rect(screen,(0,0,100),myGrid[1])
        elif mouse_pos[0]>2*screen.get_width()/3 and mouse_pos[1]<screen.get_height()/3:
             pygame.draw.rect(screen,(0,0,100),myGrid[2])
        elif mouse_pos[0]<screen.get_width()/3 and mouse_pos[1]>screen.get_height()/3 and mouse_pos[1]<2*screen.get_height()/3:
             pygame.draw.rect(screen,(0,0,100),myGrid[3])
        elif mouse_pos[0]>screen.get_width()/3 and mouse_pos[0]<2*screen.get_width()/3 and mouse_pos[1]>screen.get_height()/3 and mouse_pos[1]<2*screen.get_height()/3:
            pygame.draw.rect(screen,(0,0,100),myGrid[4])
        elif mouse_pos[0]>2*screen.get_width()/3 and mouse_pos[1]<2*screen.get_height()/3 and mouse_pos[1]>screen.get_height()/3:
            pygame.draw.rect(screen,(0,0,100),myGrid[5])
        elif mouse_pos[0]<screen.get_width()/3 and mouse_pos[1]>2*screen.get_height()/3:
            pygame.draw.rect(screen,(0,0,100),myGrid[6])
        elif mouse_pos[0]>screen.get_width()/3 and mouse_pos[0]<2*screen.get_width()/3 and mouse_pos[1]>2*screen.get_height()/3:
            pygame.draw.rect(screen,(0,0,100),myGrid[7])
        elif mouse_pos[0]>2*screen.get_width()/3 and mouse_pos[1]>2*screen.get_height()/3:
            pygame.draw.rect(screen,(0,0,100),myGrid[8])


        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            isRunning = False
        
        #show work on screen
        pygame.display.flip()

        #60 fps
        dt = clock.tick(60)/1000
        await asyncio.sleep(0)  # Very important, and keep it 0

    pygame.quit()

asyncio.run(main())