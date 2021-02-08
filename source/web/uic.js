var controlStatus = document.getElementById("status-panel")
var graph = document.getElementById("Graph")
var controlPanel = document.getElementById("control-panel")

function hideStatus() {
    graph.style.display = "none";
    if (controlStatus.style.display=== "none"){
        controlStatus.style.display = "block";
        controlPanel.style.display = "block";       
    }

}  

function hide(){
    controlStatus.style.display = "none";
    controlPanel.style.display = "none"; 
    if (graph.style.display=== "none")
        graph.style.display = "block";
}
