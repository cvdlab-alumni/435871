function myOBJloader(objName, texName, texBumpName, bumpScale, shine, repX, repZ) {
    loader.load('../obj/'+objName+'.obj', function (obj) {
        var tex = THREE.ImageUtils.loadTexture("../textures/"+texName+".png");
        var material = new THREE.MeshPhongMaterial({
                                                    map:tex,
                                                    side:THREE.DoubleSide,
                                                    metal:true,
                                                    shininess:shine});
        if (texBumpName) {
            var bump = THREE.ImageUtils.loadTexture("../textures/"+texBumpName+".png");
            material.bumpMap = bump;
            material.bumpScale = bumpScale;
            bump.wrapS = bump.wrapT = THREE.RepeatWrapping;
            bump.repeat.set(repX,repZ);
            bump.anisotropy = anisotropyNumber;
        }
        tex.wrapS = tex.wrapT = THREE.RepeatWrapping;
        tex.repeat.set(repX,repZ);
        tex.anisotropy = anisotropyNumber;
        obj.traverse(function (child) {
            if (child instanceof THREE.Mesh) {
                child.material = material;
            }
        });
        obj.rotation.x = -Math.PI/2;
        scene.add(obj);
    });
}

function onDocumentMouseDown(event) {
    event.preventDefault();
    if(document.pointerLockElement === element || document.mozPointerLockElement === element || document.webkitPointerLockElement === element) {
        var vector = new THREE.Vector3(0,0,0.5);
        projector.unprojectVector(vector,camera);
        var raycaster = new THREE.Raycaster(vector,controls.getDirection(new THREE.Vector3(0,0,0)).clone());
    } else {
        var vector = new THREE.Vector3(
             (event.clientX/window.innerWidth)*2-1,
            -(event.clientY/window.innerHeight)*2+1,
             (0.5));
        projector.unprojectVector(vector,camera);
        var raycaster = new THREE.Raycaster(camera.position,vector.sub(camera.position).normalize());
    }
    var intersects = raycaster.intersectObjects(animatedList);
    if (intersects.length > 0) {
        console.log("Clicked an animated object.");
        intersects[0].object.anim() && intersects[0].object.anim;
    }
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize( window.innerWidth, window.innerHeight );
}

function initStats() {
    var stats = new Stats();
    stats.setMode(0);
    $('body').append(stats.domElement);
    return stats;
}

function render() {
    requestAnimationFrame(render);
    renderer.render(scene, camera);
    TWEEN.update();
    stats.update();
    if(PLCenabled) { renderPLC(); }
}