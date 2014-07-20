loader.load('obj/dingdong_lb.obj', function (obj) {
    var material2 = new THREE.MeshPhongMaterial({color:0xFFFFFF, metal:true, shininess:50});
    obj.children[0].material = material2;
    obj.rotation.x = -Math.PI/2;

    animatedList.push(obj.children[0]);

    var o3dDingDong = new THREE.Object3D();
    o3dDingDong.add(obj);

    obj.children[0].anim = function() {
        var x = 89.467;
        var y = 12.126;
        var z = 37.268;

        obj.position.set(-x, -y, z);
        soundDoorBell.position.set(x , y, -z);
        soundDoorBell.play();

        var tw2 = new TWEEN.Tween(o3dDingDong.rotation)
            .to({x:0, y:0, z:0}, 500)
            .easing(TWEEN.Easing.Sinusoidal.InOut);                  
        var tw = new TWEEN.Tween(o3dDingDong.rotation)
            .to({x:Math.PI/14, y:0, z:0}, 500)
            .easing(TWEEN.Easing.Sinusoidal.InOut)
            .chain(tw2)
            .start();
        o3dDingDong.position.set(x, y, -z);
    }
    scene.add(o3dDingDong);
});

loader.load('obj/signature.obj', function (obj) {
    var tex1 = THREE.ImageUtils.loadTexture("textures/signature.png");
    var material1 = new THREE.MeshPhongMaterial({color:0xFFFFFF, map:tex1, side:THREE.DoubleSide, metal:true, shininess:50});
    var material2 = new THREE.MeshPhongMaterial({color:0xFFDF80, metal:true, shininess:300});
    tex1.anisotropy = anisotropyNumber;

    obj.children[0].material = material2;
    obj.children[1].material = material1;

    obj.rotation.x = -Math.PI/2;
    scene.add(obj);
});