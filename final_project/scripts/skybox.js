var imagePrefix = "textures/skybox/";
var skyBoxDirections  = ["xpos", "xneg", "ypos", "yneg", "zpos", "zneg"];
var imageSuffix = ".png";
var skyGeometry = new THREE.BoxGeometry( 5000, 5000, 5000 );    

var materialArray = [];
for (var i=0; i<6; i++)
    materialArray.push( new THREE.MeshBasicMaterial({
        map: THREE.ImageUtils.loadTexture( imagePrefix + skyBoxDirections[i] + imageSuffix ),
        side: THREE.BackSide
    }));
var skyMaterial = new THREE.MeshFaceMaterial( materialArray );
var skyBox = new THREE.Mesh( skyGeometry, skyMaterial );
skyBox.rotateY(Math.PI);
scene.add(skyBox);