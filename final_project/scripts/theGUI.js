
var guiControls = new function() {
    this.enablePLC = enablePLC;
}

var gui = new dat.GUI();
gui.add(guiControls, "enablePLC");
