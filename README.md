# rpi_sleepy_times

![See screen capture for example](/assets/screencapofapp.png) 

I decided to build this dumb application to enable myself to have the a device shut itself off after a certain amount of time. 

The app will display a GUI built in PyQT, expecting the user to input an integer, which will be the sleep time in minutes.

### Components

`app.py`: Contains the 'main' logic of the app

`setup.py`: simple setup script. Initially I built a formal 'setup' script w/ setup utils, but decided that was overkill.

`install.sh`: this will install python3.6 on the debian based machine it runs on, and then run `setup.py`

`src.Sleeper.py`: contains the logic for spinning up the child process which does the sleep + shutdown

`src.SleepyGui.py`: contains all the PyQT gui crap

`src.Util.py`: contains the 'installer' for the app, which will setup a nice desktop icon, with the icon based on the **clock.png** file specified in `./assets`.

### Setup

Requires python 3.6+

Install: `bash install.sh` or simply `./install.sh`