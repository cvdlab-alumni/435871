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
