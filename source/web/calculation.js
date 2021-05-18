
function calcRPM() {
    var mm = document.getElementById("wantVel").value
    var rpm = 1/5 *(mm/60)

    eel.calcVelRPM(rpm)(calculationVelocity)
}
function calculationVelocity(list){
    document.getElementById('engineVelValue').value = list[0]
    mm = (list[1]*60)/5
    document.getElementById("ClosestVel").value = mm.toFixed(2)
    return mm
}
function calcTimer() {
    timerOption = document.getElementById("timerOption").value
    timer = document.getElementById("timer").value
    list = [parseInt(timer), timerOption]
    return list
}

document.getElementById('velocitySlider').onmouseup = calcRPM
document.getElementById('velocitySlider').ontouchend = calcRPM
document.getElementById('wantVel').addEventListener('input', calcRPM)