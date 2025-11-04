#!/usr/bin/env python3

import sys

import rclpy
from rclpy.node import Node

# >>>>>>>>>>> STUDENT IMPLEMENTATION >>>>>>>>>>>
#
# TODO: Import your custom service interface defined
# in the rpros2_interfaces/srv directory. This service
# will be used to convert robot linear and angular
# velocities (v, w) into individual wheel speeds (v_l, v_r).
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class Wheel2RobotVelocityClient(Node):
    def __init__(self):
        super().__init__('wheel2robot_velocity_client')

        # >>>>>>>>>>> STUDENT IMPLEMENTATION >>>>>>>>>>>
        #
        # TODO: Create a ROS 2 service client for the service
        # named 'compute_wheel_velocities' using your custom
        # interface (rpros2_interfaces.srv/Wheel2RobotVelocity).
        #
        # Implement a timeout loop to wait until the service
        # becomes available before proceeding.
        #
        # Also, create a request object instance that will hold
        # the request part of the service message (v and w values).
        #
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def send_request(self, v, w):
        # >>>>>>>>>>> STUDENT IMPLEMENTATION >>>>>>>>>>>
        #
        # TODO: Assign the input arguments (v, w) to the request
        # fields of your service message.
        #
        # Use the asynchronous service call method This allows 
        # the node to continue running while waiting for the 
        # service response.
        #
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        pass


def main(args=None):
    rclpy.init(args=args)

    client = Wheel2RobotVelocityClient()

    # >>>>>>>>>>> STUDENT IMPLEMENTATION >>>>>>>>>>>
    #
    # TODO: Retrieve the linear (v) and angular (w) velocity
    # values from the command line arguments using `sys.argv[]`.
    #
    # Send the service request to calculate individual wheel
    # velocities and spin the node to process the async future.
    #
    # Once the response is received, print the results (v_l, v_r),
    # then destroy the node to stop execution.
    #
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
