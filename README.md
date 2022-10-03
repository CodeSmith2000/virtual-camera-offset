# virtual-camera-offset

The purpose of this code is to take the trandform data from a vive tracker that has been captured via free 3rd party blender plugins and to make it virtual production ready.
From 1 of the data will be set to (0,0,0) and new camera will be created that has the propper offsets of the real world camera from the vive tracker. The starting direction
of the tracking data will be placed tangent to the world axis.
The code assumes that the tracking data has been applied to a camera named "Camera". Camera was assumed to be the source of the tracking data because camera objects are easy to see the orientation of visually.

This code was created for Blender 3.0
It should work with all current versions ahead of 3.0

This code is intended to be run via the Blender scripting tab.
