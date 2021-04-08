var controlStatus = document.getElementById("status-panel")
var graph = document.getElementById("Graph")
var velocityPanel = document.getElementById("velocity-panel")

var positionPanel = document.getElementById("position-panel")

var homeButn = document.getElementById("homeButton")
var lightMotor = document.getElementById("light")

// for status panel
var slider = document.getElementById("slider")
var boks = document.getElementById("input")


// update the slider value.
function writeSlider () {
    boks.value = this.value;   
}
slider.oninput = writeSlider;

function writeBoks (){
    slider.value = this.value
}
boks.oninput = writeBoks
boks.value = slider.value

function hideStatus() {
    graph.style.display = "none";
    positionPanel.style.display = "none";
    velocityPanel.style.display = "block";      

} 
function hidePosition(){
    velocityPanel.style.display = "none"; 
    graph.style.display = "none";
    positionPanel.style.display = "flex"
}

function hide(){
    velocityPanel.style.display = "none";
    positionPanel.style.display = "none";
    graph.style.display = "block";
}

// function Angle(){
    //todo
// }

// function light(){
//     todo

// }