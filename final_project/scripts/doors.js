function loadDoor(objName, posX, posY, posZ, angle) {
    loader.load('obj/'+objName+'.obj', function (obj) {
        var tex1 = THREE.ImageUtils.loadTexture("textures/doors_jamb.png");
        var mat1 = new THREE.MeshPhongMaterial({color:0xCCCCCC, map:tex1, metal:true, shininess:50});
        var mat2 = new THREE.MeshPhongMaterial({color:0xE5F9FF, metal:true, shininess:50, opacity:0.9, transparent:true});
        var mat3 = new THREE.MeshPhongMaterial({color:0xE6B800, metal:true, shininess:300});

        obj.children[0].material = mat1;
        obj.children[1].material = mat2;
        obj.children[2].material = mat3;
    
        tex1.wrapS = tex1.wrapT = THREE.RepeatWrapping;
        tex1.repeat.set(2,7);
        tex1.anisotropy = anisotropyNumber;

        obj.rotation.x = -Math.PI/2;

        animatedList.push(obj.children[0]);
        animatedList.push(obj.children[1]);
        animatedList.push(obj.children[2]);

        var o3dDoors = new THREE.Object3D();
        o3dDoors.add(obj);

        obj.isOpen = false;

        obj.children[0].anim = obj.children[1].anim = obj.children[2].anim = function() {
            if(!obj.isOpen) {
                obj.position.set(-posX, -posY, posZ);
                var tw = new TWEEN.Tween(o3dDoors.rotation)
                    .to({x:0, y:angle, z:0 }, 1500)
                    .easing(TWEEN.Easing.Quadratic.Out)
                    .start();
                o3dDoors.position.set(posX, posY, -posZ);

                soundDoorOpen.position.set(posX, posY, -posZ);
                soundDoorOpen.play();

                obj.isOpen = true;
            } else {
                obj.position.set(-posX, -posY, posZ);
                var tw = new TWEEN.Tween(o3dDoors.rotation)
                    .to({x:0, y:0, z:0 }, 1500)
                    .easing(TWEEN.Easing.Quadratic.Out)
                    .start();
                o3dDoors.position.set(posX, posY, -posZ);
                setTimeout(function() {
                    soundDoorClose.position.set(posX ,posY, -posZ);
                    soundDoorClose.play();
                },1000);
                obj.isOpen = false;
            }
        }
        scene.add(o3dDoors);
    });
}

loadDoor("door_myroom", 121.108, 2.5, 61.1, -Math.PI/2);
loadDoor("door_bedroom", 136.928, 2.5, 61.1, Math.PI/2);
loadDoor("door_bathroom", 150.313, 2.5, 46.156, -Math.PI/2);
loadDoor("door_kitchen", 139.324, 2.5, 38.4, -Math.PI/2);

// DOOR ENTRANCE
loader.load('obj/door_entrance.obj', function (obj) {
    var tex1 = THREE.ImageUtils.loadTexture("textures/doors_jamb.png");
    var material1 = new THREE.MeshPhongMaterial({color:0xCCCCCC, map:tex1, side:THREE.DoubleSide, metal:true, shininess:50});
    var material2 = new THREE.MeshPhongMaterial({color:0xE6B800, metal:true, shininess:300});

    obj.children[0].material = material1;
    obj.children[1].material = material2;

    tex1.wrapS = tex1.wrapT = THREE.RepeatWrapping;
    tex1.repeat.set(4,7);
    tex1.anisotropy = anisotropyNumber;

    obj.rotation.x = -Math.PI/2;

    animatedList.push(obj.children[0]);
    animatedList.push(obj.children[1]);

    var o3dDoors = new THREE.Object3D();
    o3dDoors.add(obj);

    obj.isOpen = false;

    obj.children[0].anim = obj.children[1].anim = function() {
        var x = 75.167;
        var y = 2.5;
        var z = 38.953;
        if(!obj.isOpen) {
            obj.position.set(-x, -y, z);
            var tw = new TWEEN.Tween(o3dDoors.rotation)
                .to({x:0, y:Math.PI/2, z:0 }, 2000)
                .easing(TWEEN.Easing.Quadratic.Out)
                .delay(1200)
                .start();
            o3dDoors.position.set(x, y, -z);
            soundDoorEntOpen.position.set(x, y, -z);
            soundDoorEntOpen.play();
            obj.isOpen = true;
        } else {
            obj.position.set(-x, -y, z);
            var tw = new TWEEN.Tween(o3dDoors.rotation)
                .to({x:0, y:0, z:0 }, 2000)
                .easing(TWEEN.Easing.Quadratic.Out)
                .start();
            o3dDoors.position.set(x, y, -z);
            setTimeout(function() {
                soundDoorEntClose.position.set(x, y, -z);
                soundDoorEntClose.play();
            },1500);
            obj.isOpen = false;
        }
    }
    scene.add(o3dDoors);
});
