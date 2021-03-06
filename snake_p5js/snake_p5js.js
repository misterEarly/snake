let tiles;
let w;
let pos;
let tail;
let u, d, l, r;
let dir;
let fruit;

function reset() {
  keyCode = 0;
  tail = [];
  pos = createVector(7, 7);

  tail.push(pos);
  for (i = 1; i < 5; i++) {
    tail.push(createVector(pos.x, pos.y + 1 * i));
  }
  dir = u;
  fruit = createVector(floor(random(tiles)), floor(random(tiles)));
}

function keyPressed() {

  if (keyIsDown(LEFT_ARROW)) {
    dir = l;
    keyCode = 0;
  } else if (keyIsDown(RIGHT_ARROW)) {
    dir = r;
    keyCode = 0;
  } else if (keyIsDown(UP_ARROW)) {
    dir = u;
    keyCode = 0;
  } else if (keyIsDown(DOWN_ARROW)) {
    dir = d;
    keyCode = 0;
  }
}

function setup() {
  frameRate(5);
  tiles = 15;
  w = 40;
  createCanvas(tiles * w + 1, tiles * w + 1);

  u = createVector(0, -1);
  d = createVector(0, 1);
  l = createVector(-1, 0);
  r = createVector(1, 0);

  reset();
}

function draw() {
  background(255);

  fill(255);
  strokeWeight(2);
  for (i = 0; i < tiles; i++) {
    for (j = 0; j < tiles; j++) {
      rect(i * w, j * w, w, w);
    }
  }

  keyPressed();

  tail.splice(0, 0, tail[0].copy().add(dir));
  //console.log(pos.y)

  if (!(tail[0].x == fruit.x && tail[0].y == fruit.y)) {
    tail.splice(tail.length - 1, 1);
  } else {
    fruit = createVector(floor(random(tiles)), floor(random(tiles)));
  }
  for (i = 1; i < tail.length; i++) {
    if (tail[0].x == tail[i].x && tail[0].y == tail[i].y) {
      console.log("dead");
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
  for (i = 0; i < tail.length; i++) {
    rect(tail[i].x * w, tail[i].y * w, w, w);
  }
}
