
var stats = initStats();
var scene = new THREE.Scene();
var fov = 55;
var camera = new THREE.PerspectiveCamera(fov, window.innerWidth / window.innerHeight, 0.1, 5000);

var WIDTH = window.innerWidth;
var HEIGHT = window.innerHeight
var renderer = new THREE.WebGLRenderer({antialias:true});
renderer.setClearColor(new THREE.Color(0x33ADFF, 1.0)); // 0x33ADFF skycolor
renderer.setSize(WIDTH, HEIGHT);

// list of the objects with an animation
var animatedList = [];

var axisHelper = new THREE.AxisHelper(50);
scene.add(axisHelper);

// pointlight positioned on camera
var pointLight = new THREE.PointLight(0xffffff, 0.9);
pointLight.position = camera.position;
scene.add(pointLight);

// hemisphere light
var hemi = new THREE.HemisphereLight(0xFFDD99, 0xffffff, 0.5);
//scene.add(hemi);

// directional light
var dir = new THREE.DirectionalLight(0xffffff, 0.7);
dir.position.set(200,150,-200);;
//scene.add(dir);

// loader to load all OBJ files
var loader = new THREE.OBJLoader();

// max anisotropy for best texture result
//var anisotropyNumber = renderer.getMaxAnisotropy()/2;
var anisotropyNumber = 1;

var projector = new THREE.Projector();

camera.position.set(200,150,-200);
camera.up = new THREE.Vector3(0,1,0);
camera.lookAt(scene.position);

// Orbit controls
var orbitControls = new THREE.OrbitControls(camera);
scene.add(camera);

var reflex = false;
var PLCenabled = false;
var objects = [];
var ray = new THREE.Raycaster();
ray.ray.direction.set(0,-1,0);

document.addEventListener('mousedown', onDocumentMouseDown, false);
window.addEventListener('resize', onWindowResize, false);

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
