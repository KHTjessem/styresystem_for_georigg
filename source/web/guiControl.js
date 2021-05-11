var controlStatus = document.getElementById("status-panel")
var velocityPanel = document.getElementById("velocity-panel")

var positionPanel = document.getElementById("position-panel")

var homeButn = document.getElementById("homeButton")
var lightMotor = document.getElementById("light")



function hideStatus() {
    positionPanel.style.display = "none";
    velocityPanel.style.display = "flex";      

} 
function hidePosition(){
    velocityPanel.style.display = "none"; 
    positionPanel.style.display = "flex"
}





// reconnect button
function reconnButton() {
    btn = document.getElementById('reconnectBtn');
    btn.hidden = false;
    btn.disabled = false;
}
