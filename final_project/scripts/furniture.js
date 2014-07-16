//                                      scale x y z     pos x y z       rot x y z
// MYROOM
myOBJMTLloader("myroom_office_chair",   0.8,1,0.8,      109,6.8,-90,    0,-Math.PI/2,0);
myOBJMTLloader("myroom_table",          0.1,0.1,0.1,    110,9.3,-82,    0,Math.PI/2,0);
myOBJMTLloader("myroom_bookcase",       0.13,0.13,0.13, 100,13.5,-63.5, 0,Math.PI,0);
myOBJMTLloader("curtain",               0.22,0.27,0.1,  115,1,-106,     0,0,0);
myOBJMTLloader("myroom_desk_lamp",      1.2,1.2,1.2,    105,10.1,-100,  0,0,0);
myOBJMTLloader("myroom_applepc",        2,2,2,          106,10.15,-92,  0,Math.PI/2,0);
myOBJMTLloader("myroom_bed",            0.11,0.1,0.1,   125,2.6,-82,    0,0,0);
myOBJMTLloader("myroom_iphone",         0.1,0.1,0.1,    105,10.26,-94,  0,Math.PI/3,0);


// LOUNGE
myOBJMTLloader("lounge_sofa",           0.1,0.1,0.1,    60.5,5.9,-70,   0,Math.PI/2,0);
myOBJMTLloader("lounge_sofa",           0.1,0.1,0.1,    62.5,5.9,-93,   0,Math.PI/2.4,0);
myOBJMTLloader("lounge_furni_tv",       0.1,0.1,0.1,    90.6,2.6,-82,   0,-Math.PI/2,0);
myOBJMTLloader("lounge_floor_lamp",     0.1,0.12,0.1,   60,2.6,-81,     0,0,0);
myOBJMTLloader("curtain_tied",          1,1.4,1,        80,31,-105,     0,0,0);
myOBJMTLloader("curtain_tied",          1,1.4,1,        64,31,-105,     0,Math.PI,0);
myOBJMTLloader("curtain_rod",           4,3,3,    71.5,31.5,-105.5,  0,0,0);
myOBJMTLloader("lounge_speaker",        0.15,0.13,0.12, 87,2.6,-102,    0,-Math.PI/3,0);
myOBJMTLloader("lounge_speaker",        0.15,0.13,0.12, 87,2.6,-62,     0,-Math.PI*3/5,0);
myOBJMTLloader("lounge_corridor_lights",1.2,1.5,1.5,    75,32.5,-50,    Math.PI/2,0,0);


// LOFT
myOBJMTLloader("loft_yucca",            0.15,0.11,0.15, 8,2.6,-46,      0,Math.PI/2,0);
myOBJMTLloader("loft_chair",            0.1,0.1,0.1,    28,2.7,-70,     0,-Math.PI/2,0);
myOBJMTLloader("loft_chair",            0.1,0.1,0.1,    28,2.7,-80,     0,-Math.PI/2,0);
myOBJMTLloader("loft_umbrella",         0.08,0.1,0.08,  42,2.6,-90,     0,-Math.PI/2,0);


// KITCHEN
myOBJMTLloader("kitchen_table",         0.15,0.10,0.17, 153,2.6,-16,    0,0,0);
myOBJMTLloader("kitchen_chair",         0.10,0.10,0.10, 153,7,-27,      0,0,0);
myOBJMTLloader("kitchen_chair",         0.10,0.10,0.10, 160,7,-27,      0,0,0);
myOBJMTLloader("kitchen_chair",         0.10,0.10,0.10, 147,7,-5,       0,Math.PI,0);
myOBJMTLloader("kitchen_chair",         0.10,0.10,0.10, 154,7,-5,       0,Math.PI,0);
myOBJMTLloader("toplight_kitchen",      1.3,1.5,1.3,    153,22.7,-16,   0,0,0);
myOBJMTLloader("kitchen_fridge",        2.5,2.5,2,      166,18.5,-18,   0,0,0);
myOBJMTLloader("kitchen_oven",          0.1,0.1,0.1,    169.5,2.6,-13.9,0,-Math.PI/2,0);
myOBJMTLloader("kitchen_basin",         0.1,0.1,0.1,    162.2,2.6,-17.5,0,0,0);
myOBJMTLloader("kitchen_dishwasher",    1,1,1,          159,5,-35,      0,0,0);
myOBJMTLloader("kitchen_angle",         0.2,0.1,0.1,    156,2.6,-72,    0,-Math.PI/2,0);
myOBJMTLloader("kitchen_toaster",       0.1,0.1,0.1,    173,11.1,-33,    0,-Math.PI/2,0);
myOBJMTLloader("kitchen_toast",         0.2,0.2,0.2,    173.3,11.5,-32.9,    Math.PI/2,0,Math.PI/2);
myOBJMTLloader("kitchen_coffee",         0.1,0.1,0.1,    173,11.8,-27,    0,-Math.PI/2,0);


// BATHROOM
myOBJMTLloader("bathroom_bath",         0.08,0.08,0.08, 158,2.7,-60,    0,0,0);
myOBJMTLloader("bathroom_shower",       0.06,0.06,0.06, 159,11,-59.8,   0,0,0);
myOBJMTLloader("bathroom_washbasin",    0.1,0.1,0.1,    170,2.7,-60,    0,0,0);
// mirror
var bathMirrorMeshNo = new THREE.Mesh( new THREE.PlaneGeometry( 8, 8 ), new THREE.MeshPhongMaterial(0xFFFFFF) );
bathMirrorMeshNo.position.set(170,17,-59.6);
scene.add(bathMirrorMeshNo);
var bathMirror = new THREE.Mirror( renderer, camera, {
    clipBias: 0.003, textureWidth: WIDTH, textureHeight: HEIGHT, color:0x889999 } );
var bathMirrorMesh = new THREE.Mesh( new THREE.PlaneGeometry( 8, 8 ), bathMirror.material );
bathMirrorMesh.add(bathMirror);
bathMirrorMesh.position.set(170,17,-59.5);
var o3dMirr2 = new THREE.Object3D();
o3dMirr2.bathMirror = bathMirror;
o3dMirr2.add(bathMirrorMesh);
// end mirror
myOBJMTLloader("bathroom_toilet",       0.1,0.1,0.1,    169,2.7,-40.1,  0,Math.PI,0);
myOBJMTLloader("bathroom_paper",        0.1,0.1,0.1,    173,6,-40.1,    0,Math.PI,0);
myOBJMTLloader("bathroom_towel",        0.1,0.1,0.1,    163,4.5,-40,    0,Math.PI,0);
myOBJMTLloader("bathroom_radiator",     0.1,0.1,0.1,    148,-6,-42,     0,Math.PI,0);
myOBJMTLloader("bathroom_shower_curtain",0.1,0.1,0.1,          170.5,15.7,-59.1,   0,-Math.PI/2,0);
myOBJMTLloader("bathroom_shower_curtain_rod",0.175,0.1,0.1,    157.5,24.5,-54.6,   0,0,0);


// BEDROOM
myOBJMTLloader("bedroom_bed",           0.10,0.10,0.10, 155,2.7,-92,    0,0,0);
myOBJMTLloader("curtain_tied",          1,1.4,1,        174.5,31,-77,     0,-Math.PI/2,0);
myOBJMTLloader("curtain_tied",          1,1.4,1,        174,31,-92,     0,Math.PI/2,0);
myOBJMTLloader("toplight",              1,1,1,          156,26,-83.5,   0,0,0);
myOBJMTLloader("bedroom_wardrobe",      0.08,0.1,0.08,  161,2.6,-63.9,  0,Math.PI,0);
myOBJMTLloader("curtain_rod",           4,3,3,    174.2,31.5,-83,  0,Math.PI/2,0);


// SELF CAMERA
var o3dreflex = new THREE.Object3D();
var loader3 = new THREE.OBJMTLLoader();
loader3.addEventListener('load', function (event) {
    var object = event.content;
    object.scale.set(0.1,0.1,0.1);
    o3dreflex.add(object);
});
loader3.load(
    '../objmtl/reflex.obj', 
    '../objmtl/reflex.mtl', 
    {side: THREE.DoubleSide}
);
