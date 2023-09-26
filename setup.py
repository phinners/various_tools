# import os
# from glob import glob

from setuptools import setup, find_packages

package_name = "vartools"

setup(
    name=package_name,
    version="0.0.1",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Lukas Huber",
    maintainer_email="lukas.huber@epfl.ch",
    description="Various Mathematical Tools",
    # license_file=LICENSE,
    # package_dir={'': 'src'},
    tests_require=["pytest"],
    # entry_points={
    # 'console_scripts': ['simulation_loader = pybullet_ros2.simulation_loader:main',
    # 'pybullet_ros2 = pybullet_ros2.pybullet_ros2:main']
    # }
)
