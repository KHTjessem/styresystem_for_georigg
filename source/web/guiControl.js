var controlStatus = document.getElementById("status-panel")
var graph = document.getElementById("Graph")
var velocityPanel = document.getElementById("velocity-panel")

var positionPanel = document.getElementById("position-panel")

var homeButn = document.getElementById("homeButton")
var lightMotor = document.getElementById("light")



function hideStatus() {
    graph.style.display = "none";
    positionPanel.style.display = "none";
    velocityPanel.style.display = "flex";      

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
