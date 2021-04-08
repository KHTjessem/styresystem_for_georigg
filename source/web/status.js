var light = document.getElementById("light")
var feedback = document.getElementById("status-text")


function statusUpdate(liste){
    if (liste[0] == 10){
        light.style.backgroundColor= "#01BAEF"
    }
    else if (liste[0]==20){
        light.style.backgroundColor= "#008000"
    }

    else if (liste[0]==30){
        light.style.backgroundColor="#D64933"
    }

    feedback.innerText = liste[1]
}
