var crosshair = document.getElementById( 'crosshair' );
var blocker = document.getElementById( 'blocker' );
var instructions = document.getElementById( 'instructions' );
var stature = 17.7 // 177cm
var controls;

var havePointerLock = 'pointerLockElement' in document || 'mozPointerLockElement' in document || 'webkitPointerLockElement' in document;

if ( havePointerLock ) {
    var element = document.body;
    var pointerlockchange = function ( event ) {
        if ( document.pointerLockElement === element || document.mozPointerLockElement === element || document.webkitPointerLockElement === element ) {
            orbitControls.reset();
            camera.position.set(0,0,0);
            camera.up = new THREE.Vector3(0,1,0);
            controls.enabled = true;
            PLCenabled = true;
            controls.getObject().position.set(75,stature,-20);            
            blocker.style.display = 'none';
            crosshair.style.display = 'inline';
            dat.GUI.toggleHide();
        } else {
            // controls.enabled = false;
            // blocker.style.display = '-webkit-box';
            // blocker.style.display = '-moz-box';
            // blocker.style.display = 'box';
            // instructions.style.display = '';
            // crosshair.style.display = 'none';
            
            // refresh the page to quit PLC
            location.reload();
        }
    }

    var pointerlockerror = function ( event ) {
        instructions.style.display = '';
    }

    // Hook pointer lock state change events
    document.addEventListener( 'pointerlockchange', pointerlockchange, false );
    document.addEventListener( 'mozpointerlockchange', pointerlockchange, false );
    document.addEventListener( 'webkitpointerlockchange', pointerlockchange, false );

    document.addEventListener( 'pointerlockerror', pointerlockerror, false );
    document.addEventListener( 'mozpointerlockerror', pointerlockerror, false );
    document.addEventListener( 'webkitpointerlockerror', pointerlockerror, false );

    var enablePLC = function() {
        // instructions.style.display = 'none';
        controls = new THREE.PointerLockControls(camera);
        scene.add(controls.getObject());
        // Ask the browser to lock the pointer
        element.requestPointerLock = element.requestPointerLock || element.mozRequestPointerLock || element.webkitRequestPointerLock;
        if ( /Firefox/i.test( navigator.userAgent ) ) {
        var fullscreenchange = function ( event ) {
            if ( document.fullscreenElement === element || document.mozFullscreenElement === element || document.mozFullScreenElement === element ) {
                document.removeEventListener( 'fullscreenchange', fullscreenchange );
                document.removeEventListener( 'mozfullscreenchange', fullscreenchange );
                element.requestPointerLock();
            }
        }
        document.addEventListener( 'fullscreenchange', fullscreenchange, false );
        document.addEventListener( 'mozfullscreenchange', fullscreenchange, false );
        element.requestFullscreen = element.requestFullscreen || element.mozRequestFullscreen || element.mozRequestFullScreen || element.webkitRequestFullscreen;
        element.requestFullscreen();
        } else {
            element.requestPointerLock();
        }

    };


    function renderPLC() {
        if(guiControls.reflex) {
            scene.add(o3dreflex);
            o3dreflex.position.set(controls.getObject().position.x,
                                  controls.getObject().position.y+1.5,
                                  controls.getObject().position.z);
            o3dreflex.lookAt(new THREE.Vector3(controls.getObject().position.x+10,17,controls.getObject().position.z));
        }
        
        pointLight.position = controls.getObject().position;
        controls.isOnObject( false );
        ray.ray.origin.copy( controls.getObject().position );
        ray.ray.origin.y -= stature;
        var intersections = ray.intersectObjects( objects );
        if ( intersections.length > 0 ) {
            var distance = intersections[ 0 ].distance;
            if ( distance > 0 && distance < stature ) {
                controls.isOnObject( true );
            }
        }
        controls.update();
    }

} else {
    instructions.innerHTML = 'Your browser doesn\'t seem to support Pointer Lock API';
}
