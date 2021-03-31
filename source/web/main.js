
btn = document.getElementById('get_numb')
function add_numb(n){
    disableToggle(btn)
    document.getElementById('data').innerText += ' ' + n;
}

function numb(){
    disableToggle(btn)
    eel.getNum()(add_numb);
}
btn.addEventListener('click', numb);



function disableToggle(ele){
    if(ele.disabled){
        ele.disabled = false;
    }else{
        ele.disabled = true;
    }
}


function jsmsg(n){
    document.getElementById('data').innerText += ' ' + n;
}
eel.expose(jsmsg);