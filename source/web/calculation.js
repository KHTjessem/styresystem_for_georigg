relvelocity = document.getElementById("relVolocity")


pulseDiv= 3
usr = 8
fclk= 16*10^6


// function calcrpm(relvelocity){
//     rpm = 5(relvelocity/60)

//     eel.calVelRPM(rpm)(calculationVelocity)
// }

function calcRPM(mm) {
    rpm = 5*(mm/60)

    eel.calcVelRPM(rpm)(calculationVelocity)
}

function calculationVelocity(list){
    console.log(list)
    mm = (list[1]*60)/5
    document.getElementById("GetInput").value = mm
    return mm
}


function calcTimer() {
    timerOption = document.getElementById("timerOption").value
    timer = document.getElementById("timer").value
    list = [parseInt(timer), timerOption]
    return list
// TODO: send to backen

}
