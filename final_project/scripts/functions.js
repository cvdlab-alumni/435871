function myOBJloader(objName, texName, texBumpName, bumpScale, shine, repX, repZ) {
    loader.load('obj/'+objName+'.obj', function (obj) {
        var tex = THREE.ImageUtils.loadTexture("../textures/"+texName+".png");
        var material = new THREE.MeshPhongMaterial({
                                                    map:tex,
                                                    metal:true,
                                                    shininess:shine,
                                                    side: THREE.DoubleSide
                                                });
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

function myOBJMTLloader(objName, scaleX, scaleY, scaleZ, posX, posY, posZ, rotX, rotY, rotZ) {
    var loader2 = new THREE.OBJMTLLoader();
    var o3d = new THREE.Object3D();
    loader2.addEventListener('load', function (event) {
        var object = event.content;
        object.scale.set(scaleX, scaleY, scaleZ);
        object.position.set(posX, posY, posZ);
        object.rotation.set(rotX, rotY, rotZ);
        o3d.add(object);
        scene.add(o3d);
    });
    loader2.load(
        'objmtl/'+objName+'.obj', 
        'objmtl/'+objName+'.mtl', 
        {side: THREE.DoubleSide}
    );
}

var Sound = function ( sources, radius, volume ) {
    var audio = document.createElement( 'audio' );
    for ( var i = 0; i < sources.length; i++ ) {
        var source = document.createElement( 'source' );
        source.src = sources[ i ];
        audio.appendChild( source );
    }
    this.position = new THREE.Vector3();
    this.play = function () {
        audio.play();
    }
    this.pause = function() {
        audio.pause();
    }
    this.loop = function() {
        audio.setAttribute("loop", "true");
    }
    this.update = function ( camera ) {
        var distance = this.position.distanceTo(PLCenabled ? controls.getObject().position : camera.position);
        if ( distance <= radius ) {
            audio.volume = volume * ( 1 - distance / radius );
        } else {
            audio.volume = 0;
        }
    }
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

var rendered = false;
function render() {
    requestAnimationFrame(render);
    renderer.render(scene, camera);
    TWEEN.update();
    stats.update();
    orbitControls.update();
    pointLight.position = camera.position;

    if(PLCenabled) { renderPLC(); }

    if(guiControls.mirrors) {
        o3dMirr.elevMirror.render();
        o3dMirr2.bathMirror.render();
    }

    soundList.forEach(function(val) {
        val.update(camera);
    });

    if (videotv.readyState === videotv.HAVE_ENOUGH_DATA) {
        imageContext.drawImage(video,0,0);
        if(videoTexture)
            videoTexture.needsUpdate = true;
        videotv.updateVol();
    }

    if(document.getElementById('start').style.display === 'inline')
        document.getElementById('start').style.display = 'none';

    particleList.forEach(function(val) {
        val.update();
    })

}