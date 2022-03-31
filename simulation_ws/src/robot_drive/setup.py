import os
from glob import glob
from setuptools import setup

package_name = 'robot_drive'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        # Install marker file in the package index
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        # Include our package.xml file
        (os.path.join('share', package_name), ['package.xml']),
        # Include all launch files.
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='martinig',
    maintainer_email='martinig@amazon.com',
    description='Robomaker sample for Robomaker book',
    license='MIT-LICENSE',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rotate = robot_drive.rotate:main'
        ],
    },
)
