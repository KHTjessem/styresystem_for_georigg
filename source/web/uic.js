var controlStatus = document.getElementById("status-panel")
var graph = document.getElementById("Graph")
var controlPanel = document.getElementById("control-panel")

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
    if (controlStatus.style.display=== "none"){
        controlStatus.style.display = "block";
        controlPanel.style.display = "block";       
    }

}  

function hide(){
    controlStatus.style.display = "none";
    controlPanel.style.display = "none"; 
    if (graph.style.display=== "none")
        graph.style.display = "block";
}

