import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'rpros2_description'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*')),
        (os.path.join('share', package_name, 'models'), glob('models/*')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='erfan',
    maintainer_email='erf.riazati@gmail.com',
    description='Robot Programming with ROS2 | Robot Description Models',
    license='MIT',
    entry_points={
        'console_scripts': [
        ],
    },
)
