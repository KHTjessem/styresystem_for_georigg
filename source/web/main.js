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