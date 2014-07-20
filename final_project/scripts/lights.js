loader.load('obj/lightallbuttons.obj', function (obj) {
    var material2 = new THREE.MeshPhongMaterial({color:0xFFDF80, metal:true, shininess:50});
    obj.children[0].material = material2;
    obj.rotation.x = -Math.PI/2;
    scene.add(obj);
});

loader.load('obj/lounge_lb.obj', function (obj) {
    var material2 = new THREE.MeshPhongMaterial({color:0xFFFFFF, metal:true, shininess:50});
    obj.children[0].material = material2;
    obj.rotation.x = -Math.PI/2;

    animatedList.push(obj.children[0]);
    
    var o3dw1 = new THREE.Object3D();
    o3dw1.add(obj);

    var isLightOn = false;
    
    var plh = 32.5/1.5;
    var pLight1 = new THREE.PointLight(0xFFFFFF, 0, 35);
    pLight1.position.set(73.7,plh,-89);
    var pLight2 = pLight1.clone();
    pLight2.position.set(73.7,plh,-58);
    var pLight3 = pLight1.clone();
    pLight3.position.set(107,plh,-50);
    pLight3.distance = 23;
    var pLight4 = pLight3.clone();
    pLight4.position.set(130,plh,-50);

    scene.add(pLight1);
    scene.add(pLight2);
    scene.add(pLight3);
    scene.add(pLight4);

    obj.children[0].anim = function() {
        var x = 88.674;
        var y = 11.908;
        var z = 40.143;
        if(!isLightOn) {
            obj.position.set(-x, -y, z);
            var tw = new TWEEN.Tween(o3dw1.rotation)
                .to({x:-Math.PI/6.7, y:0, z:0}, 500)
                .easing(TWEEN.Easing.Quartic.InOut)
                .start();
            o3dw1.position.set(x, y, -z);
            var tw1 = new TWEEN.Tween(pLight1)
                .to({intensity:1.5},700)
                .easing(TWEEN.Easing.Quartic.InOut)
                .start();
            var tw2 = new TWEEN.Tween(pLight2)
                .to({intensity:1.5},700)
                .easing(TWEEN.Easing.Quartic.InOut)
                .start();
            var tw3 = new TWEEN.Tween(pLight3)
                .to({intensity:1.5},700)
                .easing(TWEEN.Easing.Quartic.InOut)
                .start();
            var tw4 = new TWEEN.Tween(pLight4)
                .to({intensity:1.5},700)
                .easing(TWEEN.Easing.Quartic.InOut)
                .start();
            soundLightOn.position.set(x, y, -z);
            soundLightOn.play();
            isLightOn = true;
        } else {
            obj.position.set(-x, -y, z);
            var tw = new TWEEN.Tween(o3dw1.rotation)
                .to({x:0, y:0, z:0 }, 500)
                .easing(TWEEN.Easing.Quartic.InOut)
                .start();
            o3dw1.position.set(x, y, -z);
            var tw1 = new TWEEN.Tween(pLight1)
                .to({intensity:0},500)
                .easing(TWEEN.Easing.Quartic.InOut)
                .start();
            var tw2 = new TWEEN.Tween(pLight2)
                .to({intensity:0},500)
                .easing(TWEEN.Easing.Quartic.InOut)
                .start();
            var tw3 = new TWEEN.Tween(pLight3)
                .to({intensity:0},500)
                .easing(TWEEN.Easing.Quartic.InOut)
                .start();
            var tw4 = new TWEEN.Tween(pLight4)
                .to({intensity:0},500)
                .easing(TWEEN.Easing.Quartic.InOut)
                .start();
            soundLightOff.position.set(x, y, -z);
            soundLightOff.play();
            isLightOn = false;
        }
    }
    scene.add(o3dw1);
});

function loadLight(objName, posX, posY, posZ, lposX, lposY, lposZ, angleX, angleZ, distance) {
    loader.load('obj/'+objName+'.obj', function (obj) {
        var material2 = new THREE.MeshPhongMaterial({color:0xFFFFFF, metal:true, shininess:50});
        obj.children[0].material = material2;
        obj.rotation.x = -Math.PI/2;

        animatedList.push(obj.children[0]);
        
        var o3dLights = new THREE.Object3D();
        o3dLights.add(obj);

        obj.isOn = false;
        
        var pLight1 = new THREE.PointLight(0xFFFFFF, 0, distance);
        pLight1.position.set(lposX,lposY,lposZ);

        scene.add(pLight1);

        obj.children[0].anim = function() {
            if(!obj.isOn) {
                obj.position.set(-posX, -posY, posZ);
                var tw = new TWEEN.Tween(o3dLights.rotation)
                    .to({x:angleX, y:0, z:angleZ}, 500)
                    .easing(TWEEN.Easing.Quartic.InOut)
                    .start();
                o3dLights.position.set(posX, posY, -posZ);
                var tw1 = new TWEEN.Tween(pLight1)
                    .to({intensity:1.5}, 500)
                    .easing(TWEEN.Easing.Quartic.InOut)
                    .start();
                soundLightOn.position.set(posX ,posY, -posZ);
                soundLightOn.play();
                obj.isOn = true;
            } else {
                obj.position.set(-posX, -posY, posZ);
                var tw = new TWEEN.Tween(o3dLights.rotation)
                    .to({x:0, y:0, z:0 }, 500)
                    .easing(TWEEN.Easing.Quartic.InOut)
                    .start();
                o3dLights.position.set(posX, posY, -posZ);
                var tw1 = new TWEEN.Tween(pLight1)
                    .to({intensity:0},500)
                    .easing(TWEEN.Easing.Quartic.InOut)
                    .start();
                soundLightOff.position.set(posX ,posY, -posZ);
                soundLightOff.play();
                obj.isOn = false;
            }
        }
        scene.add(o3dLights);
    });
}

loadLight("myroom_lb", 110.527, 11.908, 61.646, 112.5, 32.5/1.5, -84, -Math.PI/6.7, 0, 40);
loadLight("bedroom_lb", 148.285, 11.908, 61.646, 156, 32.5/1.5, -84, -Math.PI/6.7, 0, 40);
loadLight("bathroom_lb", 150.956, 11.908, 56.588, 163.5, 32.5/1.5, -50, 0, -Math.PI/6.7, 30);
loadLight("kitchen_lb", 148.91, 11.908, 37.25, 156, 32.5/1.5, -19.3, Math.PI/6.7, 0, 40);
loadLight("loft_lb", 55.146, 11.908, 55.777, 37, 32.5/1.5, -75, 0, -Math.PI/6.7, 50);
loadLight("outside_lb", 72.59, 11.908, 37.35, 78.814, 32.5/1.5, -19.438, Math.PI/6.7, 0, 40);
