# pip install setuptools
# pip install ./

import sys


if (sys.version_info.major < 3):
    print('PYTHON VERSION MUST BE 3 OR GREATER!!')
    exit(1)

# from setuptools import setup, find_packages

# setup(
#     name="rpisleepytimer",
#     version="0.0.1",
#     author="Zach McFadden",
#     author_email="zrmmaster92@gmail.com",
#     description="A sleeper GUI to have the pi sleep after x time",
#     long_description='',
#     long_description_content_type="text/markdown",
#     url="https://github.com/xxdunedainxx/rpi_sleepy_times",
#     install_requires=["kivy"],
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
#     python_requires='>=3.6',
# )

from src.Util import installer

installer()