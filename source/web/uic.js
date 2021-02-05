var controlStatus = document.getElementById("status-panel")
var Graph = document.getElementById("Graph")
var controlPanel = document.getElementById("control-panel")

function hideStatus() {
    if (controlStatus.style.display=== "none"){
        controlStatus.style.display = "block";
        controlPanel.style.display = "block";
        Graph.style.display = "none";
        
        
    }
    else {
    controlStatus.style.display = "none";
    controlPanel.style.display = "none";
    Graph.style.display = "block";
    

    }

}  

