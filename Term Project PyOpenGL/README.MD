Hi, my name is Connor Tsui, and this is my 15-112 F21 Term Project: P0RTA112!

To run this, you must have PyOpenGL installed, and you MUST use Windows.
If you don't use windows, I assume you have a mac, and in that case good luck! I have no idea how to help you.

This is the video I used to install it: https://www.youtube.com/watch?v=a4NVQC_2S2U
Here are the binaries: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl
See if you can find me in the comments :)

Basically you have to install the PyOpenGL binaries using pip.
The ones already downloaded in the Binaries folder are specifically for Python 3.9
Good luck!

You must also install numpy and pyrr libraries for math, and also pathlib.

Finally, install pygame.

Once you have that running, you should be able to run App.py!
To quit the program, press escape.

I write this again in App.py but I will emphasize here:
All credit for basic PyOpenGL code goes to GetIntoGameDev and his PyOpenGl tutorials: https://www.youtube.com/playlist?list=PLn3eTxaOtL2PDnEVNwOgZFm5xYPr4dUoR
His github: https://github.com/amengede/getIntoGameDev/tree/main/pyopengl

Without this code I would have never been able to do anything here so all credit to him. I go up to his 8th video with the code, so everything after his 8th video I am writing purely myself.

If I have written a comment next to a OpenGL function, it means I understand what it is doing. If I did not, then I sort of understand what it is.

IF I WROTE A #? COMMENT NEXT TO A GL FUNCTION, THEN I HAVE NO CLUE WHAT IT IS DOING. This will mainly be for the shading and the texturing functions, since those are written in GLSL, which is very similar to C, which I will not know until next semester when I take 15-122. I understand what is going on in the vertex and fragment shaders, but if you asked me to replicate it I would not know how.
For reference, this project is about 1000 lines of code, and about 200 lines of code was not written by me.


!!! THIS PROJECT IS A WIP !!!
I'm sorry that the code is so unreadable compared to the previous part. Unfortunately I do not have the same grasp over the logic and the math that I had for the previous graphics engine.

PLEASE IGNORE THE MODELS FOLDER! THis program does support loading in object models, but it doesn't work perfectly.
ALSO IGNORE THE IGNORE FOLDER INSIDE THE TEXTURE FOLDER! (Those diffuse images were found on google, and I created the specular textures)

Doing actual portal technology is a lot more difficult than it seems (even within a computer), and this is without the iconic portal effect where you can see what is on the other side. Having proper portals with the correct rotation and momentum preservation requires a gimbal lock, which requires quaternions. I have not taken linear algebra or matrices (21-241). I have also not taken imperative programming (C, 15-122). I don't even know what quaternions are they just sound scary. This was a very difficult project for me.

I plan to re-attempt this project when I have learned C and when I have learned proper linear algebra so I can have another go at this in OpenGL instead of PyOpenGL.

- Connor Tsui, 12/1/2021


