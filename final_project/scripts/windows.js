loader.load('obj/window_lounge_myroom_bedroom_fixed.obj', function (obj) {
    var material1 = new THREE.MeshPhongMaterial({color:0xFFFFFF});
    var material2 = new THREE.MeshPhongMaterial({color:0xE5F9FF, opacity:0.5, transparent:true});
    var tex1 = THREE.ImageUtils.loadTexture("textures/loft_marble.png");
    var material3 = new THREE.MeshPhongMaterial({map:tex1});

    obj.children[0].material = material1; // wf
    obj.children[1].material = material2; // wfg
    obj.children[2].material = material3; // wmarble

    tex1.wrapS = tex1.wrapT = THREE.RepeatWrapping;
    tex1.repeat.set(5,1);
    tex1.anisotropy = anisotropyNumber;

    obj.rotation.x = -Math.PI/2;
    
    // lounge window fixed
    scene.add(obj);

    // myroom window fixed
    var obj2 = obj.clone();
    scene.add(obj2.translateX(40.5));

    // bedroom window fixed
    var obj3 = obj.clone();
    obj3.position.set(-72.0, -17.475, 107.8);
    var o3dbedroom = new THREE.Object3D();
    o3dbedroom.add(obj3);
    o3dbedroom.rotateY(-Math.PI/2);
    o3dbedroom.position.set(176.8,17.475,-84.5);
    scene.add(o3dbedroom);
});

function loadWindow(objName, posX, posY, posZ, angle) {
    loader.load('obj/'+objName+'.obj', function (obj) {
        var material1 = new THREE.MeshPhongMaterial({color:0xFFFFFF});
        var material2 = new THREE.MeshPhongMaterial({color:0xE5F9FF, opacity:0.5, transparent:true});

        obj.children[0].material = material1; // window
        obj.children[1].material = material2; // window glass

        obj.rotation.x = -Math.PI/2;

        animatedList.push(obj.children[0]);
        animatedList.push(obj.children[1]);

        var o3dWindows = new THREE.Object3D();
        o3dWindows.add(obj);

        obj.isOpen = false;

        obj.children[0].anim = obj.children[1].anim = function() {
            if(!obj.isOpen) {
                obj.position.set(-posX, -posY, posZ);
                var tw = new TWEEN.Tween(o3dWindows.rotation)
                    .to({x:0, y:angle, z:0 }, 1000)
                    .easing(TWEEN.Easing.Quadratic.Out)
                    .delay(500)
                    .start();
                o3dWindows.position.set(posX, posY, -posZ);
                soundWindowOpen.position.set(posX, posY, -posZ);
                soundWindowOpen.play();
                obj.isOpen = true;
            } else {
                obj.position.set(-posX, -posY, posZ);
                var tw = new TWEEN.Tween(o3dWindows.rotation)
                    .to({x:0, y:0, z:0 }, 1000)
                    .easing(TWEEN.Easing.Quadratic.Out)
                    .start();
                o3dWindows.position.set(posX, posY, -posZ);
                setTimeout(function() {
                    soundWindowClose.position.set(posX, posY, -posZ);
                    soundWindowClose.play();
                },600);
                obj.isOpen = false;
            }
        }
        scene.add(o3dWindows);
    });
}

loadWindow("window_lounge1",    63.56, 12.01, 107.2,    -Math.PI/2);
loadWindow("window_lounge2",    74.963, 12.01, 107.2,   Math.PI/2);
loadWindow("window_myroom1",    104.064, 12.01, 107.2,  -Math.PI/2);
loadWindow("window_myroom2",    115.468, 12.01, 107.2,  Math.PI/2);
loadWindow("window_bedroom1",   176.2, 12.01, 92.94,    -Math.PI/2);
loadWindow("window_bedroom2",   176.2, 12.01, 81.537,   Math.PI/2);
loadWindow("window_loft1",      54.26, 5.024, 53.694,   Math.PI/2);
loadWindow("window_loft2",      54.26, 5.024, 46.313,   -Math.PI/2);
loadWindow("window_bathroom1",  176.026, 12.03, 45.473, Math.PI/2);
loadWindow("window_bathroom2",  176.026, 5.022, 54.524, -Math.PI/2);
loadWindow("window_kitchen1",   176.096, 12.03, 7.027,  Math.PI/2);

function loadWindowFixed(objName) {
    loader.load('obj/'+objName+'.obj', function (obj) {
        var material1 = new THREE.MeshPhongMaterial({color:0xFFFFFF});
        var tex1 = THREE.ImageUtils.loadTexture("textures/loft_marble.png");
        var material3 = new THREE.MeshPhongMaterial({map:tex1});

        obj.children[0].material = material1; // wf

        if(obj.children[1]) {
            obj.children[1].material = material3; // wmarble     
            tex1.wrapS = tex1.wrapT = THREE.RepeatWrapping;
            tex1.repeat.set(3,1);
            tex1.anisotropy = anisotropyNumber;
        }
        obj.rotation.x = -Math.PI/2;

        scene.add(obj);
    });
}

loadWindowFixed("window_loft_fixed");
loadWindowFixed("window_bathroom_fixed");
loadWindowFixed("window_kitchen1_fixed");
loadWindowFixed("window_kitchen2_fixed");

// KITCHEN SLIDING WINDOWS
function loadSlidingWindow(objName, posZ) {
    loader.load('obj/'+objName+'.obj', function (obj) {
        var material1 = new THREE.MeshPhongMaterial({color:0xFFFFFF});
        var bump = THREE.ImageUtils.loadTexture("textures/glass-bump.png");
        var material2 = new THREE.MeshPhongMaterial({color:0xE5F9FF, opacity:0.98, transparent:true, bumpMap:bump, bumpScale:0.05});
        var material3 = new THREE.MeshPhongMaterial({color:0x444444});

        obj.children[0].material = material1;
        obj.children[1].material = material2;
        obj.children[2].material = material3;

        obj.rotation.x = -Math.PI/2;

        bump.wrapS = bump.wrapT = THREE.RepeatWrapping;
        bump.repeat.set(3,4);

        animatedList.push(obj.children[0]);
        animatedList.push(obj.children[1]);
        animatedList.push(obj.children[2]);
        
        obj.isOpen = false;

        obj.children[0].anim = obj.children[1].anim = obj.children[2].anim = function() {
            if(!obj.isOpen) {
                var tw = new TWEEN.Tween(obj.position)
                    .to({x:0, y:0, z:posZ }, 1500)
                    .easing(TWEEN.Easing.Quadratic.InOut)
                    .start();
                soundSlWindowOpen.position.set(135, 12, -17);
                soundSlWindowOpen.play();
                obj.isOpen = true;
            } else {
                var tw = new TWEEN.Tween(obj.position)
                    .to({x:0, y:0, z:0 }, 1200)
                    .easing(TWEEN.Easing.Quadratic.In)
                    .start();
                soundSlWindowClose.position.set(135, 12, -17);
                soundSlWindowClose.play();
                obj.isOpen = false;
            }
        }
        scene.add(obj);
    });
}

loadSlidingWindow("window_kitchen21", 2.5);
loadSlidingWindow("window_kitchen22", -2.5);
