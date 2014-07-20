
var gParticle = new THREE.Geometry();
var texParticle = THREE.ImageUtils.loadTexture("textures/water_drop.png");
var mParticle = new THREE.ParticleSystemMaterial({size:0.3, map:texParticle, transparent:true, opacity:0.5});
// Cube area where particles appears
var cubeArea = [0.7, 19, 0.7];

var num = 1000;
for (i=0; i<num; i++) {
	var vertex = new THREE.Vector3();
	vertex.x = Math.random() * cubeArea[0];
	vertex.y = Math.random() * cubeArea[1];
	vertex.z = Math.random() * cubeArea[2];
	gParticle.vertices.push(vertex);
}

water_drops = new THREE.ParticleSystem(gParticle, mParticle);
water_drops.speed = 1;

water_drops.toUpdate = true;

water_drops.update = function() {
	var numVer = gParticle.vertices.length;
	if (this.toUpdate) {
		for (var i=0; i<numVer; i++) {
			if (gParticle.vertices[i].y < 0)
				gParticle.vertices[i].y += cubeArea[1];
			gParticle.vertices[i].y -= this.speed;
		}
		gParticle.verticesNeedUpdate = true;
	}
}

var particleList = [];
particleList.push(water_drops);

