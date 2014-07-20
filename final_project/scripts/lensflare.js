var textureFlare0 = THREE.ImageUtils.loadTexture( "textures/lensflare/lensflare0.png" );
var textureFlare2 = THREE.ImageUtils.loadTexture( "textures/lensflare/lensflare2.png" );
var textureFlare3 = THREE.ImageUtils.loadTexture( "textures/lensflare/lensflare3.png" );

var sunLight = new THREE.PointLight( 0xffffff, 2, 4500 );

var lens = addLight( 0.1, 0.8, 0.5, -2000, 280, -2000 );

function addLight( h, s, l, x, y, z ) {
    sunLight.color.setHSL( h, s, l );
    sunLight.position.set( x, y, z );
    scene.add(sunLight);

    var flareColor = new THREE.Color( 0xffffff );
    flareColor.setHSL( h, s, l + 0.5 );

    var lensFlare = new THREE.LensFlare( textureFlare0, 300, 0, THREE.AdditiveBlending, flareColor );

    lensFlare.add( textureFlare3, 60, 0.4, THREE.AdditiveBlending );
    lensFlare.add( textureFlare3, 40, 0.5, THREE.AdditiveBlending );
    lensFlare.add( textureFlare3, 50, 0.6, THREE.AdditiveBlending );
    lensFlare.add( textureFlare3, 80, 0.7, THREE.AdditiveBlending );
    lensFlare.add( textureFlare3, 60, 0.8, THREE.AdditiveBlending );

    lensFlare.customUpdateCallback = lensFlareUpdateCallback;
    lensFlare.position.copy( sunLight.position );
    return lensFlare;
}


function lensFlareUpdateCallback( object ) {
    var f, fl = object.lensFlares.length;
    var flare;
    var vecX = -object.positionScreen.x * 2;
    var vecY = -object.positionScreen.y * 2;
    
    for( f = 0; f < fl; f++ ) {
        flare = object.lensFlares[ f ];
        flare.x = object.positionScreen.x + vecX * flare.distance;
        flare.y = object.positionScreen.y + vecY * flare.distance;
        flare.rotation = 0;
    }

    object.lensFlares[ 2 ].y += 0.025;
    object.lensFlares[ 3 ].rotation = object.positionScreen.x * 0.5 + THREE.Math.degToRad( 45 );
}