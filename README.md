# [HackathonPythonista2015](https://github.com/ChamGeeks/ChamonixHackathon2015)

[burgers_and_beer.py](https://github.com/ChamGeeks/HackathonPythonista2015/blob/master/burgers_and_beer.py) is an iOS app written entirely on an iPad in Python 2.7 using the [Pythonista](http://omz-software.com/pythonista) for iOS Integrated Development Environment.  It uses [requests](http://python-requests.org) and the Pythonista [console](http://omz-software.com/pythonista/docs/ios/console.html) and [ui](http://omz-software.com/pythonista/docs/ios/ui.html) modules to create two user interfaces:
- __BarsView__ which displays graphic buttons for seven bars in Chamonix, France
- __BarView__ which displays the photo, map, and table of food and drink offers for one bar

The __requests__ module is used to gather bar and offers data from the [ChamonixHackathon2015 API](https://chamonix-hackathon-2015.herokuapp.com/).

## Known issues:
1. The app runs only in landscape mode
2. The app was built for the iPad form factor and might need adjustment for iPhones
3. Downloading the images of all seven bars causes a long startup delay. Images should be cached after the first download.
4. The Munster bar image does not show up in BarsView but does show up in BarView.

We gladly accept pull requests for improvements of the app.  Happy hacking.
