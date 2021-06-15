import numpy as np
import random
import pygame
from time import sleep
import keyboard as kb

tiles = 15
w = 40
pos = np.array([7, 7])
tail = []
u = np.array([0, -1])
d = np.array([0, 1])
l = np.array([-1, 0])
r = np.array([1, 0])
direct = u
fruit = np.array([random.randrange(0, tiles), random.randrange(0, tiles)])

pygame.init()
screen = pygame.display.set_mode((w * tiles, w * tiles))
pygame.display.set_caption("Snake in Python!")

clock = pygame.time.Clock()


def reset():
    global tail, direct, fruit
    tail = []
    for x in range(5):
        val = np.array([7, 7 + 1 * x])
        # print(val)
        tail.append(val)
        # print(tail)
    direct = u
    fruit = np.array([random.randrange(0, tiles), random.randrange(0, tiles)])


# frameRate(5);


reset()
active = True

while active:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            active = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direct = r
            elif event.key == pygame.K_LEFT:
                direct = l
            elif event.key == pygame.K_UP:
                direct = u
            elif event.key == pygame.K_DOWN:
                direct = d

    screen.fill("white")
    for i in range(tiles):
        for j in range(tiles):
            pygame.draw.rect(screen, "black", [i * w, j * w, w, w], 1)

    tail.insert(0, tail[0] + direct)
    print(tail)
    if not (tail[0][0] == fruit[0] and tail[0][1] == fruit[1]):
        del tail[-1]
    else:
        fruit = np.array([random.randrange(0, tiles), random.randrange(0, tiles)])

    for i in range(1, len(tail)):
        if tail[0][0] == tail[i][0] and tail[0][1] == tail[i][1]:
            print("dead")
            reset()
            continue

    if tail[0][0] < 0:
        tail[0][0] = tiles - 1
    elif tail[0][1] < 0:
        tail[0][1] = tiles - 1
    elif tail[0][0] > tiles - 1:
        tail[0][0] = 0
    elif tail[0][1] > tiles - 1:
        tail[0][1] = 0

    # canvas.create_rectangle(fruit[0] * w, fruit[1] * w, fruit[0] * w + w, fruit[1] * w + w, fill="lime")
    pygame.draw.rect(screen, "green", [fruit[0] * w, fruit[1] * w, w, w])
    pygame.draw.rect(screen, "black", [fruit[0] * w, fruit[1] * w, w, w], 1)

    for i in range(len(tail)):
        pygame.draw.rect(screen, "blue", [tail[i][0] * w, tail[i][1] * w, w, w])
        pygame.draw.rect(screen, "black", [tail[i][0] * w, tail[i][1] * w, w, w], 1)

    pygame.display.flip()
    clock.tick(5)

pygame.quit()
