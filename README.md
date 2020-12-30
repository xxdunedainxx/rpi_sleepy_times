# rpi_sleepy_times

![See screen capture for example](/assets/screencapofapp.png) 

Erin and I frequently watch shows on our raspberry pi media system at night to go to sleep. The Pi will run until it shuts off. 

I decided to build this dumb application to enable Erin or I to have the pi shut itself off after a certain amount of time we define. 

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