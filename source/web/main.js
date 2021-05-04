// Python functions through EEL
function Left (){
    val= document.getElementById("engineVelValue").value;
    val = parseInt(val);
    eel.rotate_left(val);
}
document.getElementById("leftButton").addEventListener('click', Left)

function right (){
    val = document.getElementById("engineVelValue").value;
    val = parseInt(val);
    eel.rotate_right(val);
}
document.getElementById("rightButton").addEventListener('click', right);

function stop (){
    eel.stop()
}
document.getElementById("stopButton").addEventListener('click', stop);



function setHome() {
    eel.setHome()    
}
document.getElementById('setHomebtn').addEventListener('click', setHome)
function goToHome() { 
    eel.moveto_abs(0)    
}
document.getElementById('goHomebtn').addEventListener('click', goToHome)



function moveEngRel() {
    dist = document.getElementById('positionInput').value;
    dist = parseFloat(dist)
    eel.moveto_rel(dist);
}
document.getElementById('relativeBtn').addEventListener('click', moveEngRel)
function moveEngAbs() {
    pos = document.getElementById('positionInput').value;
    pos = parseFloat(pos)
    eel.moveto_abs(pos);
}
document.getElementById('absoluteBtn').addEventListener('click', moveEngAbs)


function attemptReconnect() {
    eel.attemptReconnect()(reconnectResp);
}
document.getElementById("reconnectBtn"),addEventListener("click", attemptReconnect)

function reconnectResp(connected) {
    if (!connected){
        return
    }
    document.getElementById('reconnectBtn').hidden = true
}

// EEL exported functions.
eel.expose(updStatusText)
function updStatusText(text) {
    document.getElementById("status-text").innerText = text;
}

eel.expose(updStatus)
function updStatus(st) {
    statusUpdate(st);
}

eel.expose(updatePosition)
function updatePosition(mm) {
    positionRange.value = mm.toFixed(2);
    UpdatePSlider();
}

eel.expose(notConnected)
function notConnected() {
    statusUpdate([30, "Not connected to engine"]);
    reconnButton();
}