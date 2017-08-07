var distances = [];
var dots = [];
var dotindex = 0;
var maxDistance;
var spacer;
var mouseClicked = false;
var matNum = 1;



function setup() {
    var w = 150;
    createCanvas(w, 150);
    maxDistance = dist(width/2, height/2, width, height);
    for (var x = 0; x < width; x++) {
        distances[x] = []; // create nested array
        for (var y = 0; y < height; y++) {
            var distance = dist(width/2, height/2, x, y);
            distances[x][y] = distance/maxDistance * 255;
        }
    }
    spacer = 30;
    if (mouseClicked) {
        noLoop();
    }
    else {
        loop();
    }
}

function draw() {
    cleaner();
    background(255);
    var matx = 0;
    var maty = 0;
        for (var x = 0; x < width; x += spacer) {
            dots[matx] = []
            for (var y = 0; y < height; y += spacer) {
                colorMode(RGB);
                stroke(255,255,0);
                matdot = new MatDot(x + spacer/2, y + spacer/2, 10)
                matdot.size = 10;
                matdot.mouseLocator(matx, maty);
                maty += 1;
            }
            matx += 1;
            maty = 0;
        }
}

function MatDot(x, y, size) {
    this.x = x;
    this.y = y;
    this.size = size;
    this.color = (255, 255, 255);
    this.display = function(matx, maty) {
        colorMode(RGB);
        stroke(this.color);
        ellipse(this.x, this.y, this.size, this.size);
        dots[matx][maty] = this;
        dotindex += 1;
    }
    this.mouseLocator = function(matx, maty) {
        if (this.x <= mouseX && this.y <= mouseY) {
                this.size = 20;
                this.color = (10, 255, 100);
                this.display(matx, maty);

        }
    }
}

function mousePressed() {
    if (!mouseClicked) {
        noLoop();
        mouseClicked = true;
        setup();
        inputGen();
    }
    else {
        loop();
        matNum += 1;
        mouseClicked = false;
        setup();
    }
}

function cleaner() {
    dotindex = 0;
    for (var i=0; i < dots.length; i++) {
        dots.pop();
    }
    dotsCleaned = true;
}

function inputGen() {
    var matBox = document.createElement("div");
    matBox.className = "matBox";
    matBox.id = "mat_" + matNum.toString();
    for (var i=0; i < dots.length; i++) {
        for (var j=0; j < dots[i].length; j++) {
            var numInput = document.createElement("input");
            numInput.className = "matInput";
            numInput.id =  i.toString() + "_" + j.toString();
            matBox.appendChild(numInput);
        }
    }
    var safetyMouse = mouseX + 10;
    matBox.style.width = safetyMouse.toString() + "px";
    document.body.appendChild(matBox);
}