#!/usr/bin/env python

import rospy, math
import numpy as np
from person_quaternion_msgs.msg import Person_Quaternion, BodyPart_Quaternion

joints = ['Hips', 'LHipJoint', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 'LowerBack', 'Spine', 'Spine1', 'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand', 'LThumb', 'LeftFingerBase', 'LeftHandFinger1', 'Neck', 'Neck1', 'Head', 'RightShoulder', 'RightArm', 'RightForeArm', 'RightHand', 'RThumb', 'RightFingerBase', 'RightHandFinger1', 'RHipJoint', 'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase']


def parser():
    #Lettura del file contenente l'animazione
    f_values = open("/home/andrea/data/walk.txt", "r")
    Lines = f_values.readlines()
    
    count = 0
    for line in Lines:
        line = line.replace("\n", "")
        line = line.split(",")
        npline = np.array(line)
        frame = npline.astype(np.float)
        if count == 0:
            Frames = np.array([frame])
        else: 
            Frames = np.vstack((Frames, frame))
        count += 1

    return(Frames)


def talker():
    while not rospy.is_shutdown():
        pub = rospy.Publisher('blender', Person_Quaternion, queue_size=10)
        rospy.init_node('sender', anonymous=True)
        rate = rospy.Rate(24) #hz
        v = parser()

        #Per ogni frame contenuto in v
        for x in v:
            msg = Person_Quaternion()

            i = 0
            #Per ogni giunto
            for i in range(31):
                part = BodyPart_Quaternion()           
                part.label = joints[i]
                if i == 0:
                    part.position_x = x[0]
                    part.position_y = x[1]
                    part.position_z = x[2]
                part.rotation_w = x[3+4*i]
                part.rotation_x = x[3+4*i+1]
                part.rotation_y = x[3+4*i+2]
                part.rotation_z = x[3+4*i+3]
                msg.bodyParts = np.append(msg.bodyParts, part)
           
            #Pubblicazione del messaggio ROS per il frame corrente
            rospy.loginfo(msg)
            pub.publish(msg)
            rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
