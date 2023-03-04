#===============================================================================================#
#                                 Test_importer                                                 #
#                                                                                               #
#   Script designed only for testing the import of quaternion into a rig in Blender's scene.    #
#                                                                                               #
#                                                                        by Andrea Tessarolo    #
#===============================================================================================#

import bpy, math, time
import numpy as np

object = bpy.data.objects[0]
bpy.context.view_layer.objects.active = object
bpy.ops.object.mode_set(mode='POSE')

f_values = open("./data/quaternions.txt", "r")
Lines = f_values.readlines()

count = 0
for line in Lines:  
    line = line.replace("\n", "")
    line = line.split(",")
    npline = np.array(line) 
    v = npline.astype(np.float)
    count += 1

    #For each bone
    for i in range(31):
        bone = object.pose.bones[i]
    
        #Change location values for the Hips joint
        if i == 0:
            loc = bone.location
            loc.x = v[0]
            loc.y = v[1]
            loc.z = v[2]
            
            #Update location values
            bone.location = loc
    
    
        rot = bone.rotation_quaternion   
        rot.w = v[3+4*i]
        rot.x = v[3+4*i+1]
        rot.y = v[3+4*i+2]
        rot.z = v[3+4*i+3]
        print(rot) #DEBUGGING
    
        #Update rotation values   
        bone.rotation_quaternion = rot
    
    bpy.context.view_layer.update()
    time.sleep(1)


f_values.close()
