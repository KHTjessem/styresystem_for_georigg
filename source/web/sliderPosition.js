const
  positionRange = document.getElementById('positionRange'),
  PositionValue = document.getElementById('PositionValue'),
  
  UpdatePSlider = ()=>{
    const
      newValue = Number( (positionRange.value - positionRange.min) * 100 / (positionRange.max - positionRange.min) ),
      newPosition = 10 - (newValue * 0.2);
      PositionValue.innerHTML = `<span>${positionRange.value} mm</span>`;
      PositionValue.style.left = `calc(${newValue}% + (${newPosition}px))`;
  };
document.addEventListener("DOMContentLoaded", UpdatePSlider);
positionRange.addEventListener('input', UpdatePSlider);



var slider = document.getElementById("velocitySlider")
var boks = document.getElementById("wantVel")


// update the slider value.
function writeSlider () {
    boks.value = this.value;   
}
slider.oninput = writeSlider;

function writeValue (){
    slider.value = this.value
}
boks.oninput = writeValue
boks.value = slider.value
