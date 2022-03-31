import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name='gui',
            default_value='false'
        ),
        launch_ros.actions.Node(
            package='robot_drive',
            executable='rotate',
            output='screen',
            name='rotate',
        )
    ])