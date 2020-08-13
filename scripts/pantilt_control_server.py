#!/usr/bin/env python3

from __future__ import print_function

from pantilt_control_code import StandardCommands as teleop_pantilt
from pantilt_control_code import AdvancedCommands as set_pantilt

from pantilt_control_ros_node_test.srv import PantiltControl
from pantilt_control_ros_node_test.srv import PantiltControlResponse
import rospy

serial_port = '/dev/ttyUSB0'


def handle_pan_tilt_control(req):

    print("operation_type = ", req.operation_type)
    print("operation_specification | required_value = %s | %s" % (
          req.operation_specification, req.required_value))

    if req.operation_type == "panoramic":
        panomaric = set_pantilt(serial_port)
        panomaric.set_angle(req.operation_specification, req.required_value)
        return PantiltControlResponse(True)

    elif req.operation_type == "teleoperation":
        teleop = teleop_pantilt(serial_port)
        print("req.operation_type == teleoperation")
        teleop.teleoperation(req.operation_specification, req.required_value)
        return PantiltControlResponse(True)

    else:
        return PantiltControlResponse(False)


def pan_tilt_control_server():
    rospy.init_node('pantilt_control_server')
    service = rospy.Service('pantilt_control',
                            PantiltControl, handle_pan_tilt_control)
    print("Ready to control pantilt")
    rospy.spin()


if __name__ == "__main__":
    pan_tilt_control_server()
