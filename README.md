# [HackathonPythonista2015](https://github.com/ChamGeeks/ChamonixHackathon2015)

[burgers_and_beer.py](https://github.com/ChamGeeks/HackathonPythonista2015/blob/master/burgers_and_beer.py) is an iOS app written entirely on an iPad in Python 2.7 using the [Pythonista](http://omz-software.com/pythonista) for iOS Integrated Development Environment.  The app is a single Python file that uses the [requests](http://python-requests.org) module to gather bar and offers data from the [ChamonixHackathon2015 API](https://chamonix-hackathon-2015.herokuapp.com/). The Pythonista [console](http://omz-software.com/pythonista/docs/ios/console.html) and [ui](http://omz-software.com/pythonista/docs/ios/ui.html) modules are then used to create two user interfaces:
- [BarsView](screenshots/BarsView.jpg) which displays graphic buttons for seven bars in Chamonix, France
- [BarView](screenshots/BarView.jpg) which displays the photo, map, and table of food and drink offers for one bar

## Installation:
1. In Pythonista, open a new, empty script.
2. Paste the contents of `burgers_and_beer.py` into the Editor window.
3. Press the run button `▶` at the top right of the Editor.

## Known [issues](https://github.com/ChamGeeks/HackathonPythonista2015/issues):
1. The app runs only in landscape mode
2. The app was built for the iPad form factor and might need adjustment for iPhones
3. Downloading the images of all seven bars causes a long startup delay. Images should be cached after the first download.
4. The Munster bar image does not show up in BarsView but does show up in BarView.

We gladly accept pull requests for improvements of the app.  Happy hacking.
