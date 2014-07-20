#Davide Violante - 435871
##Computational Graphics Project
This repository contains the final project for the Computational Graphics exam of Roma Tre University (Italy), master degree course. The project goal was to create a good looking representation of our own apartment, including also some cool animations.

###Run the project
[Show me!](http://davideviolante.github.io/)

###Tools used
* [Three.js](http://www.threejs.org)
* jQuery.js
* [Tween.js](https://github.com/sole/tween.js/)
* [PyPlasm](https://github.com/plasm-language/pyplasm)
* [larcc](https://github.com/cvdlab/lar-cc)
* 3D Studio Max 7
* Adobe Photoshop
* Sublime Text 2
* Google Chrome

_____________________

###Project features
* 3D model made in larcc, converted to [OBJ](http://en.wikipedia.org/wiki/Wavefront_OBJ) and imported into Three.js
* First person camera controls
* Orbit camera controls
* Floors and walls with realistic bump-map effect
* 50+ objects of furniture (OBJ+MTL) all over the apartment
* Animated objects (+ sounds):
  * Lights
  * TV
  * Vinyl player
  * Doors
  * Windows
  * Shower
  * Toaster
  * Door bell
  * Elevator
  * and more...
* [Skybox](http://en.wikipedia.org/wiki/Skybox_(video_games)) with sunset
* [Lens flare](http://en.wikipedia.org/wiki/Lens_flare) effect on the Sun
* Real mirrors on elevator and bathroom
* Particle effect on bathroom shower
* Animated roof to see the apartment interiors
* 3D model made from scratch:
  * Apartment skeleton (larcc)  
  * Doors
  * Windows
  * Ceiling lamps
  * Vinyl player
  * and more...

___________________

###Project file and folders organization
* **images**: some cool images of the project
* **libs**: javascript libraries used
* **obj**: OBJ models
* **objmtl**: OBJ models with a MTL
* **scripts**:
   * PLC.js: includes all the features of the Pointer Lock Controls (first person camera)
   * functions.js: most important parametric functions called from other files
   * init.js: initialization of the most common variables and parameters
   * lights.js: lights switch button models and light effect
   * lensflare.js: lensflare effect functions
   * particles.js: particles for shower effect animation
   * skybox.js: skybox effect functions
   * roof.js: roof model and animation
   * vinyl_player.js: vinyl player model and animation
   * video_sounds.js: tv video effect and all sound effects (doors, windows, etc)
   * furniture.js: all furniture objects are loaded here
   * floor_walls.js: floors and walls models
   * doors.js: doors models and animation
   * windows.js: windows models and animation
   * elevator.js: elevator model and animation
   * dingdong.js: door bell model and animation including apartment owner surname
   * bathroom_kitchen_tiles.js: only bathroom and kitchen wall tiles
   * theGUi.js: interactive GUI where some parameters can be changed
* **sounds**: sounds used for animations
* **textures**: textures used for models
* **videos**: video used for TV animation
* Readme.md: this file
* **index.html**: main file to run the project
