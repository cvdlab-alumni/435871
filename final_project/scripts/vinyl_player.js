
// GIRADISCHI (parti fisse)
var loader2 = new THREE.OBJMTLLoader();
loader2.addEventListener('load', function (event) {
    var o3d = new THREE.Object3D();
    var object = event.content;
	var tex1 = THREE.ImageUtils.loadTexture("textures/doors_jamb.png");
    var material1 = new THREE.MeshPhongMaterial({map:tex1});
    var material2 = new THREE.MeshPhongMaterial({color:0xAAAAAA});
    var material3 = new THREE.MeshPhongMaterial({color:0x111111});
    var material4 = new THREE.MeshPhongMaterial({color:0x888888});
    object.children[0].material = material1; // base
    object.children[1].material = material2; // base top
    object.children[2].material = material3; // base testina
    object.children[3].material = material3; // basette
    object.children[4].material = material4; // button ngiri
	object.children[5].material = material3; // text33
	object.children[6].material = material3; // textonoff

	tex1.wrapS = tex1.wrapT = THREE.RepeatWrapping;
	tex1.repeat.set(4,0.5);
	tex1.anisotropy = anisotropyNumber;

    o3d.add(object);
    scene.add(o3d);
});
loader2.load(
    'objmtl/gd_fixed.obj', 
    'objmtl/gd_fixed.mtl', 
    {side: THREE.DoubleSide}
);

// Disk
var o3dgd = new THREE.Object3D();
loader.load('obj/gd_disk.obj', function (obj) {
	var tex1 = THREE.ImageUtils.loadTexture("textures/thewall_vinyl.png");
	var bump1 = THREE.ImageUtils.loadTexture("textures/thewall_vinyl-bump.png");
    var material1 = new THREE.MeshPhongMaterial({map:tex1,bumpMap:bump1,bumpScale:0.02});
    var material2 = new THREE.MeshPhongMaterial({color:0x222222, metal:true, shininess:200});
    var material3 = new THREE.MeshPhongMaterial({color:0xAAAAAA});
    obj.children[0].material = material2; // base disk
    obj.children[1].material = material1; // disk
    obj.children[2].material = material3; // pirillo
    o3dgd.add(obj);
    o3dgd.gd_disk = obj;
    scene.add(o3dgd);
});


// Testina
var o3dgdt = new THREE.Object3D();
loader.load('obj/gd_testina.obj', function (obj) {
    var posX = 89.208;
    var posY = 15.152;
    var posZ = 66.545;

    var material1 = new THREE.MeshPhongMaterial({color:0xCCCCCC, metal:true, shininess:200});
    obj.children[0].material = material1;

    o3dgdt.add(obj);

    animatedList.push(obj.children[0]);
    obj.isOn = false;

    // testina shaking
    var tw2 = new TWEEN.Tween(o3dgdt.rotation)
        .to({x:0, y:-Math.PI/5.53, z:0 }, 100)
        .easing(TWEEN.Easing.Linear.None)
        .yoyo(true)
        .repeat(Infinity);
    // testina rotation
    var tw1 = new TWEEN.Tween(o3dgdt.rotation)
        .to({x:0, y:-Math.PI/5.5, z:0 }, 3000)
        .easing(TWEEN.Easing.Quartic.InOut)
        .chain(tw2);
    // testina rotation original pos
    var tw0 = new TWEEN.Tween(o3dgdt.rotation)
        .to({x:0, y:0, z:0}, 2000)
        .easing(TWEEN.Easing.Quartic.InOut);

    obj.children[0].anim = function() {
        if(!obj.isOn) {
            obj.position.set(-posX, -posY, posZ);
            tw1.start();
            o3dgdt.position.set(posX, posY, -posZ);
            setTimeout(function() {
                soundVinyl.position.set(posX ,posY, -posZ);
                soundVinyl.play();
            },3000);
            obj.isOn = true;
        } else {
            soundVinyl.pause();
            TWEEN.remove(tw2);
            obj.position.set(-posX, -posY, posZ);
            tw0.start();
            o3dgdt.position.set(posX, posY, -posZ);
            obj.isOn = false;
        }
    }

    scene.add(o3dgdt);
});

// Button ON / OFF
loader.load('obj/gd_buttononoff.obj', function (obj) {
    var posX = 88.802;
    var posY = 15.271;
    var posZ = 68.404;

    var material2 = new THREE.MeshPhongMaterial({color:0x888888});
    obj.children[0].material = material2;

    animatedList.push(obj.children[0]);

    obj.isOn = false;

    // disk rotation
    var tw3 = new TWEEN.Tween(o3dgd.rotation)
        .to({x:0, y:-4*Math.PI, z:0 }, 2000)
        .easing(TWEEN.Easing.Linear.None)
        .repeat(Infinity);
    // initial disk rotation
    var tw2 = new TWEEN.Tween(o3dgd.rotation)
        .to({x:0, y:-2*Math.PI, z:0 }, 5000)
        .easing(TWEEN.Easing.Quadratic.In)
        .delay(500)
        .chain(tw3);
    var tw4 = new TWEEN.Tween(o3dgd.rotation)
        .to({x:0, y:-6*Math.PI, z:0 }, 5000)
        .easing(TWEEN.Easing.Quadratic.Out)
        .onComplete(function() {
            o3dgd.rotation.set(0,o3dgd.rotation.y+6*Math.PI,0);
        });
    // button on off
    var tw1 = new TWEEN.Tween(obj.position)
        .to({x:0, y:0, z:-0.3}, 500)
        .easing(TWEEN.Easing.Quartic.InOut);
    var tw0 = new TWEEN.Tween(obj.position)
        .to({x:0, y:0, z:0}, 500)
        .easing(TWEEN.Easing.Quartic.InOut);

    obj.children[0].anim = function() {
        if(!obj.isOn) {
            tw1.start();
            o3dgd.gd_disk.position.set(-posX, -posY, posZ);
            tw2.start();
            o3dgd.position.set(posX, posY, -posZ);
			
			obj.isOn = true;
        } else {
            o3dgd.position.set(posX, posY, -posZ);
            tw0.start();
            tw3.stop();
            tw4.start();
            obj.isOn = false;
        }
    }
    scene.add(obj);
    scene.add(o3dgd);
});

