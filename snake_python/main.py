import numpy as np
import random

tiles = 15
w = 40
pos = np.array([7, 7])
tail = []
u = np.array([0, -1])
d = np.array([0, -1])
l = np.array([0, -1])
r = np.array([0, -1])
direct = u
fruit = np.array([random.randrange(0, tiles), random.randrange(0, tiles)])


def reset():
    for i in range(5):
        tail.append(np.array([7, 7 + 1 * i]))

    direct = u;
    fruit = np.array([random.randrange(0, tiles), random.randrange(0, tiles)])


def keyPressed():
    if (keyIsDown(LEFT_ARROW)):

        dir = l;
        keyCode = 0;
    else if (keyIsDown(RIGHT_ARROW)):
        dir = r;
        keyCode = 0;
    else if (keyIsDown(UP_ARROW)):
        dir = u;
        keyCode = 0;
    else if (keyIsDown(DOWN_ARROW)):
        dir = d;
        keyCode = 0;


frameRate(5);
createCanvas(tiles * w + 1, tiles * w + 1);

reset()

while 1:
    background(255);

    fill(255);
    strokeWeight(2);
    for i in range(tiles):
        for j in range(tiles):
            rect(i * w, j * w, w, w);

    keyPressed();

    tail.splice(0, 0, tail[0].copy().add(dir));
    // console.log(pos.y)

    if (!(tail[0].x == fruit.x & & tail[0].y == fruit.y)):
        tail.splice(tail.length - 1, 1);
    else:
        fruit = createVector(floor(random(tiles)), floor(random(tiles)));

    for i in range(tail.length):
        if (tail[0].x == tail[i].x) & & (tail[0].y == tail[i].y):
            print("dead");
            reset();

    if tail[0][0] < 0:
        tail[0][0] = tiles - 1
    elif tail[0][1] < 0:
        tail[0][1] = tiles - 1
    elif tail[0][0] > tiles - 1:
        tail[0][0] = 0
    elif tail[0][1] > tiles - 1:
        tail[0][1] = 0

    fill(80, 255, 0);
    rect(fruit.x * w, fruit.y * w, w, w);

    fill(0, 0, 255);
    for i in range(tail.length):
        rect(tail[i].x * w, tail[i].y * w, w, w)

