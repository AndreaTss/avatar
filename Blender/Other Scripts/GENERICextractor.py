#====================================================================================#
#                                 GENERIC extractor                                  #
#                                                                                    #
#                                                           by Andrea Tessarolo      #
#====================================================================================#

import bpy, math
import numpy as np


#Select the RIG object in Blender's scene, than activate Pose Mode
object = bpy.data.objects[0]
bpy.context.view_layer.objects.active = object
bpy.ops.object.mode_set(mode='POSE')


#Open a file which it will contains all quaternion rotations for each frame
f_log = open("./data/log.txt", "w")
f_values = open("./data/quaternions.txt", "w")


#For each frame in BVH file
frame = 0
for frame in range (345):
    bpy.context.scene.frame_set(frame)
    print(f"FRAME {frame}", file = f_log)

    #For each bone in the rig
    for i in range(31):
        bone = object.pose.bones[i]
        
        if i == 0:
            loc = bone.location
            print(f"{bone.name} Location {round(loc[0], 3)} {round(loc[1], 3)} {round(loc[2], 3)}", file = f_log)
            print(f"{round(loc[0], 3)},{round(loc[1], 3)},{round(loc[2], 3)},", file = f_values, end = '')
        
        rot = bone.rotation_quaternion
        print(f"{bone.name} {round(rot[0], 3)} {round(rot[1], 3)} {round(rot[2], 3)} {round(rot[3], 3)}", file = f_log)
        if i == 30:
            print(f"{round(rot[0], 3)},{round(rot[1], 3)},{round(rot[2], 3)},{round(rot[3], 3)}", file = f_values, end = '')
        else:
            print(f"{round(rot[0], 3)},{round(rot[1], 3)},{round(rot[2], 3)},{round(rot[3], 3)},", file = f_values, end = '')
    print("", file = f_log)
    if frame != 345:
        print("\n", file = f_values, end = '')
    
    frame += 1


f_log.close()
f_values.close()