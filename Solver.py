import bpy


current_scene = bpy.context.scene

#Assume the main object with tracking data applied is object named "Camera"
TrackedObject = current_scene.objects['Camera']

bpy.context.scene.frame_set(0)
SLocation = [0,0,0]
SRotation = [0,0,0]
SLocation[0] = TrackedObject.location.x
SLocation[1] = TrackedObject.location.y
SLocation[2] = TrackedObject.location.z
SRotation[0] = TrackedObject.rotation_euler.x
SRotation[1] = TrackedObject.rotation_euler.y
SRotation[2] = TrackedObject.rotation_euler.z

#send the camera to origin and set rotation to 0 so we can calculate offsets easier
TrackedObject.rotation_euler = (3.141604933483303,0,0)
TrackedObject.location = (0,0,0)
TrackedObject.keyframe_insert(data_path="location", frame=0)
TrackedObject.keyframe_insert(data_path="rotation_euler", frame=0)

#create a new camera that will be out primary camera used for rendering
camera = bpy.data.cameras.new(name='NewCamera')
NewCamera = bpy.data.objects.new('NewCamera', camera)
bpy.context.scene.collection.objects.link(NewCamera)


#parent the new offset camera to the tracked object
NewCamera.location.x = 0
NewCamera.location.y = 0.0381 #meters is 1.5 inches     #the tracker is 1.5 inches behind the camera sensor, so I will be putting the camera 1.5 inches in front the tracked point.      
NewCamera.location.z = 0.06096 #meters is 2.4  inches   #the tracker is 2.4 inches above the camera sensor, so I will be putting the camera 2.4 inches below the tracked point.
NewCamera.keyframe_insert(data_path="location", frame=0)

#orient the new camera to be 90 degrees off of the tracked point
NewCamera.rotation_euler.x = -1.570796374369257#converts to -90deg
NewCamera.rotation_euler.y = 0
NewCamera.rotation_euler.z = -3.141604933483303#converts to 180deg
NewCamera.keyframe_insert(data_path="rotation_euler", frame=0)

#parent the offset camera to the tracked camera
NewCamera.parent = TrackedObject




#put the tracked camera back where it was supposed to be before we moved it
TrackedObject.location.x = SLocation[0]
TrackedObject.location.y = SLocation[1]
TrackedObject.location.z = SLocation[2]
TrackedObject.rotation_euler.x = SRotation[0]
TrackedObject.rotation_euler.y = SRotation[1]
TrackedObject.rotation_euler.z = SRotation[2]
TrackedObject.keyframe_insert(data_path="location", frame=0)
TrackedObject.keyframe_insert("rotation_euler", frame=0)

#now we have a camera "NewCamera" that is offset from the tracker exactly like the real world camera.
#Next, we need to set the tracking data to the origin point for easier use. We will do this by parenting it to an empty


#create an empty named "Main"
Main = bpy.data.objects.new("empty", None)
Main.empty_display_type = 'PLAIN_AXES'
Main.location = TrackedObject.location
Main.rotation_euler = TrackedObject.rotation_euler
bpy.context.scene.collection.objects.link(Main)

#parent the tracked data to the empty "Main"
bpy.data.objects["Camera"].select_set(True)
bpy.context.view_layer.objects.active = Main
bpy.ops.object.parent_set()

#set "Main" location to origin and rotate so camera is tangent to world axis
Main.location.x = 0
Main.location.y = 0
Main.location.z = 0
Main.rotation_euler.x = 0
Main.rotation_euler.y = 3.141604933483303
Main.rotation_euler.z = 0

#The tracker sits 4 3/8" above the ground when the camera is sitting down
Main.location.z = 0.111125 #meters equals 4 3/8"

#Make original tracked camera invisible
TrackedObject.hide_set(True)

#camera settings - You can select the camera settings to be auto applied.
#This is for a BMPCC4K
#camera.lens = 24#mm
#camera.sensor_fit = "HORIZONTAL"
#camera.sensor_width = 18.96#mm
#camera.sensor_height = 10#mm
