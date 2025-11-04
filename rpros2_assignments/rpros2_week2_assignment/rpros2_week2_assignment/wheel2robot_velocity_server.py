#!/usr/bin/env python3

import math

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


class Wheel2RobotVelocityServer(Node):
    def __init__(self):
        super().__init__('wheel2robot_velocity_server')

        # >>>>>>>>>>> STUDENT IMPLEMENTATION >>>>>>>>>>>
        #
        # TODO: Declare the following ROS 2 parameters with
        # default values for your differential drive robot:
        #
        # wheel_radius          (default: 0.1)      radius of each wheel [m]
        # wheel_distance        (default: 0.5)      distance between left and right wheels [m]
        # wheel_velocity_unit   (default: 'rpm')    unit for wheel speed output ['rpm' or 'm/s']
        #
        # Tip: Use `ros2 param list` to verify your parameters are correctly declared.
        #
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        # >>>>>>>>>>> STUDENT IMPLEMENTATION >>>>>>>>>>>
        #
        # TODO: Create a service named 'compute_wheel_velocities'
        # using your custom interface:
        #
        #   rpros2_interfaces.srv/Wheel2RobotVelocity
        #
        # The service should handle requests in the method
        # `compute_callback()`, where you will perform the
        # necessary velocity calculations.
        #
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def compute_callback(self, request, response):

        # >>>>>>>>>>> STUDENT IMPLEMENTATION >>>>>>>>>>>
        #
        # TODO: Retrieve the declared parameters (wheel_radius,
        # wheel_distance, wheel_velocity_unit) as they are required
        # for your calculations.
        #
        # Perform the conversion from robot linear and angular
        # velocities (v, w) in the service request to individual
        # wheel velocities (v_l, v_r) in the response.
        #
        # Use the standard kinematic equations for a differential
        # drive robot:
        #   v_r = (2 * v + w * wheel_distance) / 2
        #   v_l = (2 * v - w * wheel_distance) / 2
        #
        # Check the parameter `wheel_velocity_unit` to determine
        # whether to output the speeds in 'rpm' or 'm/s' and apply
        # the proper conversion.
        #
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        return response


def main(args=None):
    rclpy.init(args=args)

    node = Wheel2RobotVelocityServer()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
