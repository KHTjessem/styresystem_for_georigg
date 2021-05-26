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
    setMaxSpeed(2000) // Set max speed for home button during velmode.
    // 2000 vel is an estimated 5.6 mm/min
} 
function hidePosition(){
    velocityPanel.style.display = "none";
    positionPanel.style.display = "flex";
    eel.newPdiv(3);
    calcMaxSpeedRPM() // Sets max speed in pos mode.
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


function downloadManual() {
    window.open('./Manual.pdf', '_blank');
}
document.getElementById('UManualBtn').addEventListener('click', export_chart)
function export_chart() {
    var a = document.createElement('a');
    a.href = './Manual.pdf';
    a.download = 'Manual.pdf';
 
 // Trigger the download
    a.click();
 }