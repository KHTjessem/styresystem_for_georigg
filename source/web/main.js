
function add_numb(n){
    document.getElementById('numb-test').innerText += ' ' + n;
}

function numb(){
    eel.rand_numb()(add_numb);
}

document.getElementById('get_numb').addEventListener('click', numb);