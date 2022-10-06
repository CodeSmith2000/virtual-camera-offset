# virtual-camera-offset

The purpose of this code is to take the transform data from a vive tracker that has been captured via free 3rd party blender plugins and to make it virtual production ready.
The floor under the tracker will be set to (0,0,0) and a new camera will be created that has the proper offsets of the real world camera from the vive tracker. 
The starting direction of the tracking data will be placed tangent to the world axis. Finally, everything will be parented to an empty so you have full directional and positional control.
The code assumes that the tracking data has been applied to a camera named "Camera". Camera was assumed to be the source of the tracking data because camera objects are easy to see the orientation of visually. The code also assumes that a vive tracker has been placed upright in the top of the camera.

This code was created for Blender 3.0
It should work with all current versions ahead of 3.0

This code is intended to be run via the Blender scripting tab.
