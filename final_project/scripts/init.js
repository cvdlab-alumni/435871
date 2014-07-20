
var stats = initStats();
var scene = new THREE.Scene();
var fov = 55;
var camera = new THREE.PerspectiveCamera(fov, window.innerWidth / window.innerHeight, 0.1, 7000);

var WIDTH = window.innerWidth;
var HEIGHT = window.innerHeight
var renderer = new THREE.WebGLRenderer({antialias:true, alpha:true});
renderer.setClearColor(new THREE.Color(0xFFFFFF, 1.0)); // 0x33ADFF skycolor
renderer.setSize(WIDTH, HEIGHT);

// list of the objects with an animation
var animatedList = [];
var soundList = [];

var axisHelper = new THREE.AxisHelper(50);

// pointlight positioned on camera
var pointLight = new THREE.PointLight(0xffffff, 0.9);
pointLight.position = camera.position;
scene.add(pointLight);

// loader to load all OBJ files
var loader = new THREE.OBJLoader();
var loader2 = new THREE.OBJMTLLoader();

// max anisotropy for best texture result
//var anisotropyNumber = renderer.getMaxAnisotropy()/2;
var anisotropyNumber = 1;

var projector = new THREE.Projector();

camera.position.set(250,105,130);
camera.up = new THREE.Vector3(0,1,0);

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

// Whole simplified building
var gBuilding = new THREE.BoxGeometry(178.2,200,109.2, 1, 1, 1);
var mBuilding = new THREE.MeshPhongMaterial({color:0xE7BC84});
var simpleBuilding = new THREE.Mesh(gBuilding, mBuilding);
simpleBuilding.position.set(89,-100,-54.5);
