```
sudo apt update
```

```
cd simulation_ws
rosws update
colcon build
. install/setup.bash
ros2 run robot_drive rotate gui:=true
ros2 launch robot_drive start_auto_robot.launch.py gui:=true
```