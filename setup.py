from setuptools import find_packages, setup

package_name = 'hewo_bot_module_web_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Daiego43',
    maintainer_email='diedelcha@gmail.com',
    description='A Web App to monitor the status of the robot and command actions to it',
    license='MIT License',
    entry_points={
        'console_scripts': [
        ],
    },
)
