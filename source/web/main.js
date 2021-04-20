
function Left (){
    val= document.getElementById("slider").value
    val = parseInt(val)
    eel.rotate_left(val)
}
document.getElementById("leftButton").addEventListener('click', Left)
function right (){
    val = document.getElementById("slider").value
    val = parseInt(val)
    eel.rotate_right(val)

}
document.getElementById("rightButton").addEventListener('click', right)

function stop (){
    eel.stop()
}

document.getElementById("stopButton").addEventListener('click', stop)

// EEL exported functions.
eel.expose(updStatusText)
function updStatusText(text) {
    document.getElementById("status-text").innerText = text    
}


eel.expose(updStatus)
function updStatus(st) {
    statusUpdate(st)
}