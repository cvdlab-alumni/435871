// VIDEO
var videotv = document.getElementById( 'video' );

var image = document.createElement( 'canvas' );
image.width = 640;
image.height = 360;

var imageContext = image.getContext( '2d' );
imageContext.fillStyle = '#000000';
imageContext.fillRect( 0, 0, 640, 360 );

var videoTexture = new THREE.Texture( image );
videoTexture.minFilter = THREE.LinearFilter;
videoTexture.magFilter = THREE.LinearFilter;

var material = new THREE.MeshBasicMaterial( { map: videoTexture } );

var videoPlane = new THREE.PlaneGeometry( 8.7, 5.4, 4, 4 );

var videoMesh = new THREE.Mesh( videoPlane, material );
videoMesh.rotateY(-Math.PI/2);
videoMesh.position.set(88, 11.2, -82);
animatedList.push(videoMesh);
scene.add(videoMesh);
videoMesh.playing = false;
videoMesh.visible = false;
var tvLight = new THREE.PointLight(0xffffff, 0, 30);
scene.add(tvLight);
videoMesh.anim = function() {
	if(!videoMesh.playing) {
		videoMesh.visible = true;
		videotv.play();
		videoMesh.playing = true;
		tvLight.position = videoMesh.position;
		tvLight.intensity = 0.3;
	} else {
		videoMesh.visible = false;
		videotv.pause();
		videoMesh.playing = false;
		tvLight.intensity = 0;
	}
}
videotv.updateVol = function() {
	var distance = videoMesh.position.distanceTo((PLCenabled) ? controls.getObject().position : camera.position);
	if (distance <= 70) {
		videotv.volume = 1 * (1 - distance / 70);
	} else {
		videotv.volume = 0;
	}
}


// SOUNDS
var soundVinyl = new Sound( [ 'sounds/pinkfloyd-intheflesh.mp3' ], 80, 1 );
var soundDoorOpen = new Sound( [ 'sounds/door_open.mp3' ], 50, 1 );
var soundDoorClose = new Sound( [ 'sounds/door_close.mp3' ], 50, 1 );
var soundDoorEntOpen = new Sound( [ 'sounds/door_entrance_open.mp3' ], 50, 1 );
var soundDoorEntClose = new Sound( [ 'sounds/door_entrance_close.mp3' ], 50, 1 );
var soundLightOn = new Sound( [ 'sounds/light_on.mp3' ], 40, 1 );
var soundLightOff = new Sound( [ 'sounds/light_off.mp3' ], 40, 1 );
var soundDoorBell = new Sound( [ 'sounds/door_bell.mp3' ], 50, 1 );
var soundWindowOpen = new Sound( [ 'sounds/window_open.mp3' ], 50, 1 );
var soundWindowClose = new Sound( [ 'sounds/window_close.mp3' ], 50, 1 );
var soundSlWindowOpen = new Sound( [ 'sounds/sliding_window_open.mp3' ], 50, 1 );
var soundSlWindowClose = new Sound( [ 'sounds/sliding_window_close.mp3' ], 50, 1 );
var soundToaster = new Sound( [ 'sounds/sound_toaster.mp3' ], 50, 1 );
var soundShower = new Sound( [ 'sounds/shower.mp3' ], 50, 1 );

soundList.push(soundVinyl);
soundList.push(soundDoorOpen);
soundList.push(soundDoorClose);
soundList.push(soundDoorEntOpen);
soundList.push(soundDoorEntClose);
soundList.push(soundLightOn);
soundList.push(soundLightOff);
soundList.push(soundDoorBell);
soundList.push(soundWindowOpen);
soundList.push(soundWindowClose);
soundList.push(soundSlWindowOpen);
soundList.push(soundSlWindowClose);
soundList.push(soundToaster);
soundList.push(soundShower);
