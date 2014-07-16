
var guiControls = new function() {
    this.enablePLC = enablePLC;
    this.bgcolor = true;
    this.cameraPointLight = pointLight.intensity;
    this.mirrors = false;
    this.reflex = false;
}

var gui = new dat.GUI();

gui.add(guiControls, "enablePLC");

gui.add(guiControls, "reflex").onChange(function(e) {
    e ? scene.add(o3dreflex) : scene.remove(o3dreflex);
});

gui.add(guiControls, "bgcolor").onChange(function(e) {
    if(e) {
    	renderer.setClearColor(new THREE.Color(0x33ADFF, 1.0));
    } else {
    	renderer.setClearColor(new THREE.Color(0x000000, 1.0));
    }
});

gui.add(guiControls, "cameraPointLight", 0.1, 1).onChange(function(e) {
    pointLight.intensity = e;
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