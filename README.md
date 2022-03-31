```
sudo apt update
source /usr/share/gazebo/setup.sh
export DISPLAY=:0
```

```
cd simulation_ws
rosws update
rosdep install --from-paths src --ignore-src -r -y
colcon build
. install/setup.bash
ros2 run robot_drive rotate gui:=true
ros2 launch robot_drive start_auto_robot.launch.py gui:=true
```