import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'rpros2_week2_assignment'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='erfan',
    maintainer_email='erf.riazati@gmail.com',
    description='Robot Programming with ROS2 | Week 2 | ROS Interfaces, Services, and Actions',
    license='MIT',
    entry_points={
        'console_scripts': [
            'wheel2robot_vel_server = rpros2_week2_assignment.wheel2robot_velocity_server:main',
            'wheel2robot_vel_client = rpros2_week2_assignment.wheel2robot_velocity_client:main',
        ],
    },
)
