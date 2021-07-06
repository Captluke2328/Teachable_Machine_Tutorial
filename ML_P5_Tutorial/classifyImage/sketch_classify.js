let MobileNet
let imgs

function modelReady(){
    console.log('Model is Ready !!')
}

// --- This one go first ---
function preload() {
  MobileNet = ml5.imageClassifier('MobileNet', modelReady);
  imgs = loadImage('images_classify/dog.jpeg');
}

function setup() {
  createCanvas(400, 400);
MobileNet.classify(imgs, gotResult);
  image(imgs, 0, 0, width,height);
}

function gotResult(error, results) {
  // Display error in the console
  if (error) {
    console.error(error);
  } else {
    // The results are in an array ordered by confidence.
    console.log(results);
    createDiv(`Label: ${results[0].label}`);
    createDiv(`Confidence: ${nf(results[0].confidence, 0, 2)}`);
    textSize(25)
    text(results[0].label,10,height-50)
  }
}
