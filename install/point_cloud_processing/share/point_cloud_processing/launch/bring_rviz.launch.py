
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import os

def generate_launch_description():

    config_file_path = os.path.join(get_package_share_directory('point_cloud_processing'),'rviz','kitti_viz2.rviz')

    return LaunchDescription([
        Node(
            package='rviz2', executable='rviz2', output='screen',
            arguments=['-d', config_file_path]
        ),
    ])

    # use_sim_time = LaunchConfiguration('use_sim_time')
    # qos = LaunchConfiguration('qos')
    # localization = LaunchConfiguration('localization')

    # parameters={
    #       'frame_id':'base_footprint',
    #       'use_sim_time':use_sim_time,
    #       'subscribe_depth':True,
    #       'use_action_for_goal':True,
    #       'qos_image':qos,
    #       'qos_imu':qos,
    #       'Reg/Force3DoF':'true',
    #       'Optimizer/GravitySigma':'0' # Disable imu constraints (we are already in 2D)
    # }

    # remappings=[
    #       ('rgb/image', '/camera/image_raw'),
    #       ('rgb/camera_info', '/camera/camera_info'),
    #       ('depth/image', '/camera/depth/image_raw')]

    # return LaunchDescription([

    #     # Launch arguments
    #     DeclareLaunchArgument(
    #         'use_sim_time', default_value='true',
    #         description='Use simulation (Gazebo) clock if true'),
        
    #     DeclareLaunchArgument(
    #         'qos', default_value='2',
    #         description='QoS used for input sensor topics'),
            
    #     DeclareLaunchArgument(
    #         'localization', default_value='false',
    #         description='Launch in localization mode.'),

    #     # Nodes to launch
        
    #     # SLAM mode:
    #     Node(
    #         condition=UnlessCondition(localization),
    #         package='rtabmap_slam', executable='rtabmap', output='screen',
    #         parameters=[parameters],
    #         remappings=remappings,
    #         arguments=['-d']), # This will delete the previous database (~/.ros/rtabmap.db)
            
    #     # Localization mode:
    #     Node(
    #         condition=IfCondition(localization),
    #         package='rtabmap_slam', executable='rtabmap', output='screen',
    #         parameters=[parameters,
    #           {'Mem/IncrementalMemory':'False',
    #            'Mem/InitWMWithAllNodes':'True'}],
    #         remappings=remappings),

    #     Node(
    #         package='rtabmap_viz', executable='rtabmap_viz', output='screen',
    #         parameters=[parameters],
    #         remappings=remappings),
    # ])