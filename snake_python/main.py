import numpy as np
import random
import tkinter

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

main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg="white", height=tiles * w, width=tiles * w)


def reset():
    global tail, direct, fruit
    for x in range(5):
        val = np.array([7, 7 + 1 * x])
        # print(val)
        tail.append(val)
        # print(tail)
    direct = u;
    fruit = np.array([random.randrange(0, tiles), random.randrange(0, tiles)])


#
# def keyPressed():
#     if (keyIsDown(LEFT_ARROW)):
#
#         dir = l;
#         keyCode = 0;
#     elif (keyIsDown(RIGHT_ARROW)):
#         dir = r;
#         keyCode = 0;
#     elif (keyIsDown(UP_ARROW)):
#         dir = u;
#         keyCode = 0;
#     elif (keyIsDown(DOWN_ARROW)):
#         dir = d;
#         keyCode = 0;


# frameRate(5);


reset()

while 1:
    # background(255);

    # fill(255);
    # strokeWeight(2);
    for i in range(tiles):
        for j in range(tiles):
            canvas.create_rectangle(i * w, j * w, i * w + w, j * w + w)

    # keyPressed();

    np.insert(tail, 0, tail[0] + direct)

    if not (tail[0][0] == fruit[0] and tail[0][1] == fruit[1]):
        del tail[-1]
    else:
        fruit = np.array([random.randrange(0, tiles), random.randrange(0, tiles)])

    for i in range(len(tail)):
        if tail[0][0] == tail[i][0] and tail[0][1] == tail[i][1]:
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

    # fill(80, 255, 0);
    # rect(fruit.x * w, fruit.y * w, w, w);
    canvas.create_rectangle(fruit[0] * w, fruit[1] * w, fruit[0] * w + w, fruit[1] * w + w, fill="lime")

    # fill(0, 0, 255);
    for i in range(len(tail)):
        canvas.create_rectangle(tail[i][0] * w, tail[i][1] * w, tail[i][0] * w + w, tail[i][1] * w + w, fill="blue")

    canvas.pack()
    main.mainloop()
