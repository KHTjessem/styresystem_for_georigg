var controlStatus = document.getElementById("status-panel")
var graph = document.getElementById("Graph")
var velocityPanel = document.getElementById("velocity-panel")

var positionPanel = document.getElementById("position-panel")

var homeButn = document.getElementById("homeButton")
var lightMotor = document.getElementById("light")



function hideStatus() {
    positionPanel.style.display = "none";
    velocityPanel.style.display = "flex";
    eel.newPdiv(9);

} 
function hidePosition(){
    velocityPanel.style.display = "none";
    positionPanel.style.display = "flex";
    eel.newPdiv(3);
}

function hide(){
    velocityPanel.style.display = "none";
    positionPanel.style.display = "none";
}



// reconnect button
function reconnButton() {
    btn = document.getElementById('reconnectBtn');
    btn.hidden = false;
    btn.disabled = false;
}
