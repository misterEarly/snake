let tiles;
let w;
let pos;
let tail;

function setup() {
  tiles = 15;
  w = 40;
  createCanvas(tiles * w + 1, tiles * w + 1);

  pos = createVector(7, 7);
  tail = [];
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
  fill(0, 255, 0);
  rect(pos.x*w, pos.y*w, w, w);
}
