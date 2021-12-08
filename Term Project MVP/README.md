Welcome to my Term Project! My Name is Connor Tsui and this was my MVP for my 15-112 F21 Term Project.
This is a 3D Graphics Engine from scratch using purely linear algebra, matrices, and rasterized triangles.

To run this program, you must install numpy, and then go to main.py to execute.

There are no shortcut commands because this is an easy game and if you can't get through it you are bad.

jk, go to app.cheats in main.py and set it equal to True, and everything becomes a lot easier.
If you really want to go straight to a specific level go to GameFunctions/initGame.py, line 44 and set a specific start level.

That's basically it! That will run "The Floor is Lava."

If you want to instead create your own world and your own game, here are the built in functions/objects that I have made:


World Components:
Wall: Similar to RectPrism, except without top and bottom triangles. 4 total triangles.
Floor and Ceiling: Similar to RectPrism, except without side triangles. Each have 2 total triangles.

Components:
RectPrism(coord0, coord1, etc...): Takes in an initial coordinate and a final coordiante and creates a rectangular prism between the two points. coord1 MUST have each of the 3 dimensions larger than coord0, so coord0 < coord1. Made up of exactly 12 triangles.
Triangle: Given that all 3d objects can be represented by a triangle mesh, this engine CAN support importing obj models (without texture coordinates) and it can replicate any 3D object, however because this is written in a deprecated version of tkinter, any object with more than a handful of triangles and normals will slow this program down drastically. In my PyOpenGL version, I do have support for import obj models (not entirely my own code though), but it basically shows that as long as you have coordinates for triangles and their normals, you can make anything.


That's basically it! The real intention of this project was not to make a game, but to make an ENGINE that could support a game. Similar to how we can make triangles and squares in tkinter, with this you can make 3d objects. The rest of the "game" is determined by whoever wants to use this. I spent only a day and a half making the floor is lava game, but over a month on just the engine.
Theoretically, the deprecated version of Portal that I have in the next part of this project could very much be recreated in this game engine, albeit it will be literally 10x slower.

To whoever uses this, you probably shouldn't because there are still a lot of bugs (as comes with a very complex project) and I am not going to continue working on this. In the future I will be working on the next part of this project in the other folder, using PyOpenGL, or realistically I will be using OpenGL after I learn C in 15-122.

Thank you for reading! - Connor Tsui, 12/1/2021