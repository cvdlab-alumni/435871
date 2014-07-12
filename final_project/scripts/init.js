var stats = initStats();
function initStats() {
    var stats = new Stats();
    stats.setMode(0);
    $('body').append(stats.domElement);
    return stats;
}
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 5000);

camera.position.set(200,150,-200);
camera.up = new THREE.Vector3(0,1,0);
camera.lookAt(scene.position);

//var trackballControls = new THREE.TrackballControls(camera);
var orbitControls = new THREE.OrbitControls(camera);

var renderer = new THREE.WebGLRenderer({antialias:true});
renderer.setClearColor(new THREE.Color(0x000000, 1.0)); // 0x33ADFF skycolor
renderer.setSize(window.innerWidth, window.innerHeight);

// list of the objects with an animation
var animatedList = [];

var axisHelper = new THREE.AxisHelper(50);
scene.add(axisHelper);

// pointlight positioned on camera
var pointLight = new THREE.PointLight(0xffffff);
pointLight.intensity = 0.9;
pointLight.position = camera.position;
scene.add(pointLight);

// loader to load all OBJ files
var loader = new THREE.OBJLoader();
// max anisotropy for best texture result
var anisotropyNumber = renderer.getMaxAnisotropy();

var projector = new THREE.Projector();

document.addEventListener('mousedown', onDocumentMouseDown, false);

// function to animate the objects with a mouse click
function onDocumentMouseDown(event) {
    event.preventDefault();
    var vector = new THREE.Vector3(
         (event.clientX/window.innerWidth)*2-1,
        -(event.clientY/window.innerHeight)*2+1,
         (0.5));
    projector.unprojectVector(vector,camera);
    var raycaster = new THREE.Raycaster(camera.position,vector.sub(camera.position).normalize());
    var intersects = raycaster.intersectObjects(animatedList);
    if (intersects.length > 0) {
        console.log("Clicked an animated object.");
        intersects[0].object.anim() && intersects[0].object.anim;
    }
}

// -------- IMPORTING LAR MODEL --------
loader.load('obj/master.obj', function (obj) {
    var material = new THREE.MeshPhongMaterial({color: 0xFFFFFF, side: THREE.DoubleSide});
    obj.traverse(function (child) {
        if (child instanceof THREE.Mesh) {
            child.material = material;
        }
    });
    obj.rotation.x = -Math.PI/2;
    scene.add(obj);
});

