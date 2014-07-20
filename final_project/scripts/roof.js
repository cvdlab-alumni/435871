loader.load('obj/roof.obj', function (obj) {
    var tex1 = THREE.ImageUtils.loadTexture("textures/wall_white.png");
    var material1 = new THREE.MeshPhongMaterial({map:tex1, bumpMap:tex1, bumpScale:-0.2});
    var tex2 = THREE.ImageUtils.loadTexture("textures/wall_external.png");
    var bump2 = THREE.ImageUtils.loadTexture("textures/wall_external-bump.png");
    var material2 = new THREE.MeshPhongMaterial({map:tex2, bumpMap:bump2, bumpScale:-0.2});
    var material3 = new THREE.MeshPhongMaterial({color:0xEFD3AF, map:tex1, bumpMap:tex1, bumpScale:-0.4});
    tex1.anisotropy = anisotropyNumber;
    tex2.anisotropy = anisotropyNumber;
    bump2.anisotropy = anisotropyNumber;
    bump2.wrapS = bump2.wrapT = THREE.RepeatWrapping;
    bump2.repeat.set(12,15);
    tex1.wrapS = tex1.wrapT = THREE.RepeatWrapping;
    tex1.repeat.set(12,15);
    tex2.wrapS = tex2.wrapT = THREE.RepeatWrapping;
    tex2.repeat.set(15,1);

    obj.children[0].material = material1;
    obj.children[1].material = material2;
    obj.children[2].material = material3;

    obj.rotation.x = -Math.PI/2;

    animatedList.push(obj.children[0]);
    animatedList.push(obj.children[1]);
    animatedList.push(obj.children[2]);

    var o3dRoof = new THREE.Object3D();
    o3dRoof.add(obj);

    obj.isOpen = false;

    obj.children[0].anim = obj.children[1].anim = obj.children[2].anim = function() {
        var x = 52.54;
        var y = 32.5;
        var z = 0;
        if(!obj.isOpen) {
            if(!PLCenabled) {
                obj.position.set(-x, -y, z);
                var tw = new TWEEN.Tween(o3dRoof.rotation)
                    .to({x:Math.PI/1.9, y:0, z:0 }, 6000)
                    .easing(TWEEN.Easing.Quadratic.Out)
                    .start();
                o3dRoof.position.set(x, y, -z);
                obj.isOpen = true;
            }
        } else {
            obj.position.set(-x, -y, z);
            var tw = new TWEEN.Tween(o3dRoof.rotation)
                .to({x:0, y:0, z:0 }, 6000)
                .easing(TWEEN.Easing.Quadratic.Out)
                .start();
            o3dRoof.position.set(x, y, -z);
            obj.isOpen = false;
        }
    }
    scene.add(o3dRoof);
});