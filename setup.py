from setuptools import find_packages, setup

package_name = 'carom'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nithish',
    maintainer_email='nithish@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['tracking = carom.tracking:main',
        'odometry_subscriber = carom.odometry_subscriber:main',
        'tracking_version2 = carom.tracking_version2:main',
        'tracking_version3 = carom.tracking_version3:main'
        ],
    },
)
