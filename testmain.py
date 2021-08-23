import pygame, random, sys
pygame.init()
screen = pygame.display.set_mode((500,500))

# [loc, vel, timer]
particles = []
clock = pygame.time.Clock()

while True:
    screen.fill((0,0,0))

    particles.append([[250,250],[random.randint(0,20)/10-1, random.randint(0,20)/10-1], random.randint(4,6)])

    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1

        pygame.draw.circle(screen,(255,255,255), [int(particle[0][0]),int(particle[0][1])],int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)


    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(1)
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print(2)
                    run = False
                    pygame.quit()
                    sys.exit()
    pygame.display.update()
    clock.tick(60)