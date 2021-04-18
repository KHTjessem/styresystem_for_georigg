const
  positionRange = document.getElementById('positionRange'),
  PositionValue = document.getElementById('PositionValue'),
  setValue = ()=>{
    const
      newValue = Number( (positionRange.value - positionRange.min) * 100 / (positionRange.max - positionRange.min) ),
      newPosition = 10 - (newValue * 0.2);
      PositionValue.innerHTML = `<span>${positionRange.value}</span>`;
      PositionValue.style.left = `calc(${newValue}% + (${newPosition}px))`;
  };
document.addEventListener("DOMContentLoaded", setValue);
positionRange.addEventListener('input', setValue);