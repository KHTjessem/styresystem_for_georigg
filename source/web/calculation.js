// Velocity mode
function calcRPM() {
    var mm = document.getElementById("wantVel").value;
    var rpm = (mm/60)/5;
    if (mm > 343){ // Max engine can provide.
        document.getElementById("wantVel").value = 343;
        mm = 343;
    }
    if (mm < 0){
        document.getElementById("wantVel").value = 0.168;
        mm = 0.168; // Min engine can provide.
    }
    pdiv = 9;
    eel.calcVelRPM(rpm, pdiv)(calculationVelocity);
}
function calculationVelocity(list){
    document.getElementById('engineVelValue').value = list[0]
    mm = (list[1]*60)*5
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


// Positionong mode
function calcMaxSpeedRPM() {
    var mm = document.getElementById("MaxSpeedPmode").value;
    var rpm = (mm/60)/5;

    pdiv = 9;
    eel.calcVelRPM(rpm, pdiv)(SetMaxSpeedCallback);
}
document.getElementById('MaxSpeedPmode').addEventListener('input', calcMaxSpeedRPM)

function SetMaxSpeedCallback(list) {
    setMaxSpeed(list[0])
}

function setMaxSpeed(speedVel) {
    eel.SetMaxSpeed(speedVel)
}