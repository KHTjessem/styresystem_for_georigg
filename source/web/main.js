window.addEventListener("contextmenu", function(e) { e.preventDefault(); })
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
document.getElementById('posStopBtn').addEventListener('click', stop);

function slowRigth() {
    eel.rotate_right(20);
}
document.getElementById('RightBtn').addEventListener('touchstart', slowRigth);
document.getElementById('RightBtn').addEventListener('touchend', stop);
document.getElementById('RightBtn').addEventListener('mousedown', slowRigth);
document.getElementById('RightBtn').addEventListener('mouseup', stop);
function slowLeft() {
    eel.rotate_left(20);
}
document.getElementById('LeftRBtn').addEventListener('touchstart', slowLeft);
document.getElementById('LeftRBtn').addEventListener('touchend', stop);
document.getElementById('LeftRBtn').addEventListener('mousedown', slowLeft);
document.getElementById('LeftRBtn').addEventListener('mouseup', stop);


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
document.getElementById("reconnectBtn").addEventListener("click", attemptReconnect)

function reconnectResp(connected) {
    if (!connected){
        return
    }
    document.getElementById('reconnectBtn').hidden = true
    document.getElementById('reconnectBtn').disabled = true
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
    console.log('New pos: ' + mm);
    UpdatePSlider();
}

eel.expose(notConnected)
function notConnected() {
    statusUpdate([30, "Not connected to engine"]);
    reconnButton();
}