
var guiControls = new function() {
    this.enablePLC = enablePLC;
    this.sunLight = sunLight.intensity;
    this.lensFlare = false;
    this.axisHelper = false;
    this.showBuilding = false;
    this.reflexNikon = false;
    this.mirrors = false;
    this.brightness = pointLight.intensity;
}

var gui = new dat.GUI();

gui.add(guiControls, "enablePLC");

gui.add(guiControls, "sunLight", 0.0, 2.0).onChange(function(e) {
    sunLight.intensity = e;
});

gui.add(guiControls, "lensFlare").onChange(function(e) {
    e ? scene.add(lens) : scene.remove(lens);
});

gui.add(guiControls, "axisHelper").onChange(function(e) {
    e ? scene.add(axisHelper) : scene.remove(axisHelper);
});

gui.add(guiControls, "showBuilding").onChange(function(e) {
    e ? scene.add(simpleBuilding) : scene.remove(simpleBuilding);
});

gui.add(guiControls, "reflexNikon").onChange(function(e) {
    e ? scene.add(o3dreflex) : scene.remove(o3dreflex);
});

gui.add(guiControls, "mirrors").onChange(function(e) {
    if(e) {
    	scene.remove(bathMirrorMeshNo);
    	scene.add(o3dMirr);
    	scene.add(o3dMirr2);
    } else {
    	scene.add(bathMirrorMeshNo);
    	scene.remove(o3dMirr);
    	scene.remove(o3dMirr2);
    }
});

gui.add(guiControls, "brightness", 0.0, 1.0).onChange(function(e) {
    pointLight.intensity = e;
});
