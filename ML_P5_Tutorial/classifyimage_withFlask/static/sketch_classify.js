let MobileNet
let imgs
function modelReady(){
    console.log('Model is Ready !!')
}

// --- This one go first ---
function preload() {
  MobileNet = ml5.imageClassifier('MobileNet', modelReady);
  imgs = loadImage('static/cat.png');  
}

function setup() {
  createCanvas(400, 400);
  MobileNet.classify(imgs, gotResult);
  image(imgs, 0, 0, width,height);
}

function gotResult(error, results) {
  // Display error in the console
  if (error) {
    console.log(error);
    
  } else {
    // The results are in an array ordered by confidence.
    console.log(results);
    createDiv(`Label: ${results[0].label}`);
    createDiv(`Confidence: ${nf(results[0].confidence, 0, 2)}`);
    textSize(25)
    text(results[0].label,10,height-50)
    document.getElementById('label').innerHTML = results[0].label // -> Set the label in html to label value by using its ID
    document.getElementById('result').value = results[0].label // -> Set the result for python input value by using result ID
    document.getElementById('myForm').submit(); // -> Automatic submit the button
  }
}
