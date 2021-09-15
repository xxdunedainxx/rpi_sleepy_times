#/bin/bash

# Python3 install
apt-get install python3

# Install pip and this app's dependencies
python3 -m pip install -U pip
python3 -m pip install setuptools
python3 -m pip install python-kasa --pre # used if smart outlet

python3 ./setup.py install

