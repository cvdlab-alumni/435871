loader.load('obj/elevator_door.obj', function (obj) {
    var bump = THREE.ImageUtils.loadTexture("textures/glass-bump.png");
    var material1 = new THREE.MeshPhongMaterial({color:0x990033, bumpMap:bump, bumpScale:0.005, metal:true, shininess:50});
    var material2 = new THREE.MeshPhongMaterial({color:0x555555, metal:true, shininess:25, opacity:0.7, transparent:true});
    var material3 = new THREE.MeshPhongMaterial({color:0xAAAAAA, metal:true, shininess:50});

    obj.children[0].material = material1;
    obj.children[1].material = material2;
    obj.children[2].material = material3;

    bump.wrapS = bump.wrapT = THREE.RepeatWrapping;
    bump.repeat.set(3,4);

    obj.rotation.x = -Math.PI/2;
    animatedList.push(obj.children[0]);
    animatedList.push(obj.children[1]);
    animatedList.push(obj.children[2]);

    var o3dElevator = new THREE.Object3D();
    o3dElevator.add(obj);
    
    obj.isOpen = false;

    obj.children[0].anim = obj.children[1].anim = obj.children[2].anim = function() {
        var x = 99.276;
        var y = 2.55;
        var z = 22.608;
        if(!obj.isOpen && isUpElev) {
            obj.position.set(-x, -y, z);
            var tw = new TWEEN.Tween(o3dElevator.rotation)
                .to({x:0, y:Math.PI/2, z:0 }, 1200)
                .easing(TWEEN.Easing.Quadratic.Out)
                .start();
            o3dElevator.position.set(x, y, -z);
            obj.isOpen = true;
        } else {
            obj.position.set(-x, -y, z);
            var tw = new TWEEN.Tween(o3dElevator.rotation)
                .to({x:0, y:0, z:0 }, 1700)
                .easing(TWEEN.Easing.Quartic.InOut)
                .start();
            o3dElevator.position.set(x, y, -z);
            obj.isOpen = false;
        }
    }
    scene.add(o3dElevator);
});

loader.load('obj/elevator_box.obj', function (obj) {
    var material1 = new THREE.MeshPhongMaterial({color:0xAAAAAA, metal:true, shininess:50});
    var texButtons = THREE.ImageUtils.loadTexture("textures/elevator_buttons.png");
    var material2 = new THREE.MeshPhongMaterial({map:texButtons, metal:true, shininess:50});
    var material3 = new THREE.MeshPhongMaterial({color:0xFFFFFF, metal:true, shininess:200});
    var texInternal = THREE.ImageUtils.loadTexture("textures/elevator_texture.png");
    var material4 = new THREE.MeshPhongMaterial({map:texInternal, metal:true, shininess:20});
    var material5 = new THREE.MeshPhongMaterial({color:0xFFFFE5, metal:true, shininess:50});

    obj.children[0].material = material2; // buttons
    obj.children[1].material = material1; // cylinder
    obj.children[2].material = material1; // external
    obj.children[3].material = material3; // glass
    obj.children[4].material = material4; // internal
    obj.children[5].material = material5; // light
    
    texInternal.wrapS = texInternal.wrapT = THREE.RepeatWrapping;
    texInternal.repeat.set(3,4);
    texButtons.wrapS = texButtons.wrapT = THREE.RepeatWrapping;
    texButtons.repeat.set(1,1);
    obj.rotation.x = -Math.PI/2;

    isUpElev = false;

    ele = obj;

    scene.add(obj);
});

// Mirror into the elevator
var elevMirror = new THREE.Mirror( renderer, camera, {
    clipBias: 0.003, textureWidth: WIDTH, textureHeight: HEIGHT, color:0x889999 } );
var elevMirrorMesh = new THREE.Mesh( new THREE.PlaneGeometry( 11, 11 ), elevMirror.material );
elevMirrorMesh.add(elevMirror);
elevMirrorMesh.position.set(113.8,-4.4,-27.5);
elevMirrorMesh.rotateY(-Math.PI/2);
var o3dMirr = new THREE.Object3D();
o3dMirr.elevMirror = elevMirror;
o3dMirr.add(elevMirrorMesh);


function loadElevAutoDoor(objName) {
    loader.load('obj/'+objName+'.obj', function (obj) {
        var bump = THREE.ImageUtils.loadTexture("textures/glass-bump.png");
        var material2 = new THREE.MeshPhongMaterial({color:0xCCCCCC, bumpMap:bump, bumpScale: 0.01, metal:true, shininess:50});
        obj.children[0].material = material2;
        bump.wrapS = bump.wrapT = THREE.RepeatWrapping;
        bump.repeat.set(3,4);
        obj.rotation.x = -Math.PI/2;
        if(objName === "elevator_doorauto1") elevautodoor1 = obj;
        scene.add(obj);
    }); 
}

loadElevAutoDoor("elevator_doorauto1");

loader.load('obj/elevator_caller.obj', function (obj) {
    var texButtons = THREE.ImageUtils.loadTexture("textures/elevator_caller.png");
    var material2 = new THREE.MeshPhongMaterial({map:texButtons, metal:true, shininess:50});

    obj.children[0].material = material2;
    
    obj.rotation.x = -Math.PI/2;

    var isElevCalled = false;
    var pLight1 = new THREE.PointLight(0xFFFFEE, 0, 20);
    pLight1.position.set(107.806,17.5,-27.5);
    scene.add(pLight1);

    animatedList.push(obj.children[0]);

    obj.children[0].anim = function() {
        if(!isElevCalled) {
            isElevCalled = true;
            twElevAutoDoors1 = new TWEEN.Tween(elevautodoor1.position)
                .to({x:0, y:20, z:9.5 }, 3000)
                .easing(TWEEN.Easing.Linear.None)
            twElevLight = new TWEEN.Tween(pLight1)
                .to({intensity:1.2}, 1000)
                .easing(TWEEN.Easing.Quadratic.InOut)
                .onComplete(function() {
                    isUpElev = true;
                })
                .chain(twElevAutoDoors1);
            twElev = new TWEEN.Tween(ele.position)
                .to({x:0, y:20, z:0 }, 5000)
                .easing(TWEEN.Easing.Quadratic.InOut)
                .chain(twElevLight);
            twElevMirror1 = new TWEEN.Tween(o3dMirr.position)
                .to({x:0, y:20, z:0 }, 5000)
                .easing(TWEEN.Easing.Quadratic.InOut)
                .start();
            twElevAutoDoors1a = new TWEEN.Tween(elevautodoor1.position)
                .to({x:0, y:20, z:0 }, 5000)
                .easing(TWEEN.Easing.Quadratic.InOut)
                .start();
            twCaller = new TWEEN.Tween(obj.position)
                .to({x:0.05, y:0, z:0 }, 0)
                .easing(TWEEN.Easing.Linear.None)
                .chain(twElev)
                .start();
        } else {
            isElevCalled = false;
        }
    }
    scene.add(obj);
});
