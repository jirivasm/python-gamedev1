import asyncio
import pygame

COUNT_DOWN = 3

async def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    isRunning = True
    dt = 0
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    while isRunning:
        #handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        #filling screen
        screen.fill("blue")
        pygame.draw.circle(screen, "red", player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            isRunning = False
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
        #show work on screen
        pygame.display.flip()

        #60 fps
        dt = clock.tick(60)/1000
        await asyncio.sleep(0)  # Very important, and keep it 0

        # if not COUNT_DOWN:
        #     return

        # COUNT_DOWN = COUNT_DOWN - 1
    pygame.quit()

asyncio.run(main())