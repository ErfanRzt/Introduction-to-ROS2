<div align="justify">

## Robot Programming with ROS2 Assignment Template

Follow the steps below to set up your environment and complete the assignment.

### 1. Create a ROS2 Workspace

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```

### 2. Copy the Assignment Package

Copy the provided ROS2 package (e.g. `rpros2_week1_assignment`) into your workspace:

```bash
cd ~/ros2_ws/src
cp -r /path/to/rpros2_week1_assignment .
```

### 3. Build the Assignment Package

```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

### 4. Modify the Student Sections

Open the package source files and complete the parts marked with:

```python
# >>>>>>>>>>> STUDENT IMPLEMENTATION >>>>>>>>>>>
#
# TODO: Write your code in here.
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
```

Make sure your code runs correctly and meets the assignment objectives.


## Table of Contents
- [Week 1](#week-1-turtlesim-target-visualization-and-teleop)
- [Week 2](#week-2-differential-drive-robot-to-wheel-velocity-converter)


## `Week 1` Turtlesim Target Visualization and Teleop 

### Assignment Task: 
In this first project, you will develop a Turtlesim visualizer and keyboard teleoperation interface.

The package contains two main nodes:

1. turtle_keyboard_control — Publishes velocity commands to the topic `/turtle1/cmd_vel`, allowing you to control the turtle using the keyboard.

2. turtle_target_plot — Subscribes to `/turtle1/pose` and visualizes the turtle’s position and orientation. It also spawns a randomly placed box in the Turtlesim window. When the turtle reaches the box, the box disappears and respawns at another random location.

A launch file named `turtle_target_teleop.launch.py` should start all required nodes together, including turtlesim_node. Modify the `STUDENT IMPLEMENTATION` sections and then run your launch file to verify correct functionality.

### Reuslts:
You should include figures or screen recordings of your results in the folder `./figures/rpros2_week1/`. Below is a sample markdown structure for embedding figures (e.g., `.png`, `.jpg`, or `.gif`):

<div align="center">

| <img src=".\figures\week1\turtle_target_teleop_node_example.gif" alt="turtle_target_teleop_node_example" width="1024"/> |
|:--:| 
| <b>Fig. 1.</b> Turtlesim Target Visualization and Teleop Node Example |

</div>

<div align="center">
  
| <img src=".\figures\week1\turtle_target_teleop_launch_example.gif" alt="turtle_target_teleop_launch_example" width="1024"/> |
|:--:| 
| <b>Fig. 2.</b> Turtlesim Target Visualization and Teleop Launch Example |

</div>

### Challenges:
Describe any errors, issues, or challenges you encountered during this assignment.
Explain the steps or solutions you used to fix them.

**For Example:**
- Missing dependencies during build.
- Incorrect topic names or launch configuration.
- Logical errors in handling keyboard inputs or random target generation.

## `Week 2` Differential-Drive Robot to Wheel Velocity Converter 

### Learning Objective: 
- Create custom ROS interfaces.
- Implement a ROS service server and client.
- Work with ROS parameters.

### Assignment Task: 
In this assignment, you will develop a ROS 2 service that converts a differential-drive mobile robot’s linear and angular velocities (`v` and `w`) to individual wheel velocities (`v_l` and `v_r`).

The assignment is broken down into the following steps:

1. Define a custom service interface:
- In the `rpros2_interfaces` package, create `Wheel2RobotVelocity.srv`.
- The request should contain `v` (linear velocity) and `w` (angular velocity).
- The response should contain `v_l` (left wheel velocity) and `v_r` (right wheel velocity).
- Update the `CMakeLists.txt` file to build the new service.

2. Create a service server:
- Implement the service server in `wheel2robot_velocity_server.py`.
- Verify that the service is available using the `rqt` Service Caller plugin.

3. Use ROS parameters:
- Check that the parameters are correctly set using `ros2 param list`.
- Modify parameters dynamically with `ros2 param set` and observe changes in the service calculation.

4. Create a service client:
- Implement a client node wheel2robot_velocity_client.py that takes v and w as command line arguments.
- Test calling the service from the command line.

5. Use a YAML configuration file:
- Define custom ROS parameters in `config/wheel2robot_service_params.yaml`.
- Run the launch file and ensure the parameters are correctly assigned to the service node.

6. Launch the system:
- Verify that the server node spawns correctly.
- Confirm that changing parameters in the YAML file affects the service calculations as expected.

### Results: 

</div>