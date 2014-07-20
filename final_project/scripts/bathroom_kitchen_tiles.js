// BATHROOM TILES
function loadBathroomTile(objName, rep1, rep2) {
	loader.load('obj/'+objName+'.obj', function (obj) {
	    var tex1 = THREE.ImageUtils.loadTexture("textures/bathroom_floor.png");
	    var tex2 = THREE.ImageUtils.loadTexture("textures/bathroom_tile_white.png");
	    var tex3 = THREE.ImageUtils.loadTexture("textures/bathroom_tile.png");
	    var tex4 = THREE.ImageUtils.loadTexture("textures/bathroom_tile_white.png");
	    
	    var material1 = new THREE.MeshPhongMaterial({map:tex1});
	    var material2 = new THREE.MeshPhongMaterial({map:tex2});
	    var material3 = new THREE.MeshPhongMaterial({map:tex3});
	    var material4 = new THREE.MeshPhongMaterial({map:tex4});
	    
	    obj.children[0].material = material1;
	    obj.children[1].material = material2;
	    obj.children[2].material = material3;
	    obj.children[3].material = material4;

	    var bump1 = THREE.ImageUtils.loadTexture("textures/bathroom_floor-bump.png");
	    var bump2 = THREE.ImageUtils.loadTexture("textures/bathroom_tile_white-bump.png");
	    var bump3 = THREE.ImageUtils.loadTexture("textures/bathroom_tile-bump.png");
	    var bump4 = THREE.ImageUtils.loadTexture("textures/bathroom_tile_white-bump.png");

	    material1.bumpMap = bump1;
	    material2.bumpMap = bump2;
	    material3.bumpMap = bump3;
	    material4.bumpMap = bump4;
	    material1.bumpScale = 0.05;
	    material2.bumpScale = 0.1;
	    material3.bumpScale = 0.05;
	    material4.bumpScale = 0.1;

	    bump1.wrapS = bump1.wrapT = bump2.wrapS = bump2.wrapT = bump3.wrapS = bump3.wrapT = bump4.wrapS = bump4.wrapT = THREE.RepeatWrapping;
	    bump1.repeat.set(rep1,2);
	    bump2.repeat.set(rep1,4);
	    bump3.repeat.set(rep2,0.45);
	    bump4.repeat.set(rep1,2);
	    bump1.anisotropy = bump2.anisotropy = bump3.anisotropy = bump4.anisotropy = anisotropyNumber;

	    tex1.wrapS = tex1.wrapT = tex2.wrapS = tex2.wrapT = tex3.wrapS = tex3.wrapT = tex4.wrapS = tex4.wrapT = THREE.RepeatWrapping;
	    tex1.repeat.set(rep1,2);
	    tex2.repeat.set(rep1,4);
	    tex3.repeat.set(rep2,0.45);
	    tex4.repeat.set(rep1,2);
	    tex1.anisotropy = tex2.anisotropy = tex3.anisotropy = tex4.anisotropy = anisotropyNumber;

	    obj.rotation.x = -Math.PI/2;
	    scene.add(obj);
	    if(objName === "bathroom_tile_top_bottom") {
		    var obj2 = obj.clone();
		    obj2.translateY(20);
		    scene.add(obj2);
	    }
	});
}
loadBathroomTile("bathroom_tile_top_bottom", 8, 4);
loadBathroomTile("bathroom_tile_right", 6, 3);
loadBathroomTile("bathroom_tile_left", 7, 4);

// KITCHEN TILES
myOBJloader("kitchen_tile_bottom1", "kitchen_tile", "kitchen_tile-bump", 0.02, 50, 13,8);
myOBJloader("kitchen_tile_bottom2", "kitchen_tile2", "kitchen_tile-bump", 0.02, 50, 13,8);
myOBJloader("kitchen_tile_left1", "kitchen_tile", "kitchen_tile-bump", 0.02, 50, 11,8);
myOBJloader("kitchen_tile_left2", "kitchen_tile2", "kitchen_tile-bump", 0.02, 50, 11,8);
myOBJloader("kitchen_tile_top1", "kitchen_tile", "kitchen_tile-bump", 0.02, 50, 13,8);
myOBJloader("kitchen_tile_top2", "kitchen_tile2", "kitchen_tile-bump", 0.02, 50, 13,8);
myOBJloader("kitchen_tile_right1", "kitchen_tile", "kitchen_tile-bump", 0.02, 50, 11,8);
myOBJloader("kitchen_tile_right2", "kitchen_tile2", "kitchen_tile-bump", 0.02, 50, 11,8);
