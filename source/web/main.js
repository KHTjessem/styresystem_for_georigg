
function add_numb(n){
    document.getElementById('numb-test').innerText += ' ' + n;
}

function numb(){
    eel.rand_numb()(add_numb);
}

document.getElementById('get_numb').addEventListener('click', numb);

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
document.getElementById("emergency").addEventListener('click', stop)