#!/usr/bin/env python

from __future__ import print_function

import math
import os
from os import path
import sys
import rospy
from pantilt_control_ros_node_test.srv import PantiltControl
from pantilt_control_ros_node_test.srv import PantiltControlResponse


def pt_teleoperation_client(command, speed):
    rospy.wait_for_service('pantilt_control')
    try:
        pt_teleoperation = rospy.ServiceProxy('pantilt_control', PantiltControl)
        operation = "teleoperation"
        resp = pt_teleoperation(operation, command, speed)
        return resp.response_sucess
    except rospy.ServiceException as e:
        print("Service call failed: %e" % e)


def usage():
    return "%s [command speed]" % sys.argv[0]


if __name__ == "__main__":
    if len(sys.argv) == 3:
        command = str(sys.argv[1])  # ex: down
        speed = int(sys.argv[2])  # ex: 50

    else:
        print(usage())
        sys.exit(1)
    print("Requesting teleoperation --> %s --> %s"%(command, speed))
    pt_teleoperation_client(command, speed) 
