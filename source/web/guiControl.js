var controlStatus = document.getElementById("status-panel")
var graph = document.getElementById("Graph")
var controlPanel = document.getElementById("control-panel")
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
    if (controlPanel.style.display=== "none"){
        controlPanel.style.display = "flex";       
    }

}  

function hide(){
    controlPanel.style.display = "none"; 
    graph.style.display = "block";
}

// function Angle(){
    //todo
// }

// function light(){
//     todo

// }