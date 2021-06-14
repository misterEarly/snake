let tiles;
let w;
let pos;
let tail;
let len;
let u, d, l, r;

function setup() {
  frameRate(2);
  tiles = 15;
  w = 40;
  createCanvas(tiles * w + 1, tiles * w + 1);

  pos = createVector(7, 7);
  tail = [];
  len = 5;

  u = createVector(0, -1);
  d = createVector(0, 1);
  l = createVector(-1, 0);
  r = createVector(-1, 0);
  
  tail.push(pos);
  for (i = 1; i < len; i++) {
    tail.push(createVector(pos.x, pos.y+(1*i)));
  }
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

  tail.splice(0,0,tail[0].copy().add(u));
  //console.log(pos.y)
  tail.splice(tail.length-1,1);

  if (tail[0].x < 0) {
    tail[0].x = tiles - 1;
  } else if (tail[0].y < 0) {
    tail[0].y = tiles - 1;
  } else if (tail[0].x > tiles - 1) {
    tail[0].x = 0;
  } else if (tail[0].y > tiles - 1) {
    tail[0].y = 0;
  }
  
  //console.log(pos.y)
  fill(0, 255, 0);
  for (i=0; i<tail.length; i++){
    rect(tail[i].x * w, tail[i].y * w, w, w);
  }
  
}
