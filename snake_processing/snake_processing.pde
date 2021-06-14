int tiles;
int w;
PVector pos;
PVector[] tail = new PVector[5];
PVector u, d, l, r;
PVector dir;
PVector fruit;

void reset() {
  keyCode = 0;

  pos = new PVector(7, 7);

  append(tail, pos);
  for (int i = 1; i < 5; i++) {
    append(tail, new PVector(pos.x, pos.y + 1 * i));
  }
  dir = u;
  fruit = new PVector(floor(random(tiles)), floor(random(tiles)));
}

void keyPressed() {
  if (keyPressed) {
    if (keyCode == LEFT) {
      dir = l;
      keyCode = 0;
    } else if (keyCode == RIGHT) {
      dir = r;
      keyCode = 0;
    } else if (keyCode == UP) {
      dir = u;
      keyCode = 0;
    } else if (keyCode == DOWN) {
      dir = d;
      keyCode = 0;
    }
  }
}

void setup() {
  frameRate(5);
  tiles = 15;
  w = 40;
  //int x = tiles * w + 1;
  //print(x);
  size(601, 601);

  u = new PVector(0, -1);
  d = new PVector(0, 1);
  l = new PVector(-1, 0);
  r = new PVector(1, 0);

  reset();
}

void draw() {
  background(255);

  fill(255);
  strokeWeight(2);
  for (int i = 0; i < tiles; i++) {
    for (int j = 0; j < tiles; j++) {
      rect(i * w, j * w, w, w);
    }
  }

  keyPressed();

  append(tail, tail[0].copy().add(dir));
  //console.log(pos.y)

  if (!(tail[0].x == fruit.x && tail[0].y == fruit.y)) {
    shorten(tail);
  } else {
    fruit = new PVector(floor(random(tiles)), floor(random(tiles)));
  }
  for (int i = 1; i < tail.length; i++) {
    if (tail[0].x == tail[i].x && tail[0].y == tail[i].y) {
     print("dead");
      reset();
    }
  }

  if (tail[0].x < 0) {
    tail[0].x = tiles - 1;
  } else if (tail[0].y < 0) {
    tail[0].y = tiles - 1;
  } else if (tail[0].x > tiles - 1) {
    tail[0].x = 0;
  } else if (tail[0].y > tiles - 1) {
    tail[0].y = 0;
  }

  fill(80, 255, 0);
  rect(fruit.x * w, fruit.y * w, w, w);
  //console.log(pos.y)
  fill(0, 0, 255);
  for (int i = 0; i < tail.length; i++) {
    rect(tail[i].x * w, tail[i].y * w, w, w);
  }
}
