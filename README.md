# AA Time Zones

[![Version](https://img.shields.io/pypi/v/aa-timezones?label=release)](https://pypi.org/project/aa-timezones/)
[![License](https://img.shields.io/badge/license-GPLv3-green)](https://pypi.org/project/aa-timezones/)
[![Python](https://img.shields.io/pypi/pyversions/aa-timezones)](https://pypi.org/project/aa-timezones/)
[![Django](https://img.shields.io/pypi/djversions/aa-timezones?label=django)](https://pypi.org/project/aa-timezones/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/aa-timezones)](https://pypi.org/project/aa-timezones/)
[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](http://black.readthedocs.io/en/latest/)


App for displaying different time zones with Alliance Auth

![Time Zones](https://raw.githubusercontent.com/ppfeufer/aa-timezones/master/timezones/docs/time-zones.jpg)


## Contents

- [Installation](#installation)
- [Updating](#updating)
- [Configure Timezone Panels](#configure-timezone-panels)
- [Adjusting Time](#adjusting-time)
- [Change Log](CHANGELOG.md)


## Installation

**Important**: This app is a plugin for Alliance Auth.
If you don't have Alliance Auth running already, please install it first before proceeding.
(see the official [AA installation guide](https://allianceauth.readthedocs.io/en/latest/installation/allianceauth.html)
for details)


### Step 1 - Install app

Make sure you are in the virtual environment (venv) of your Alliance Auth installation.
Then install the latest version:

```bash
pip install aa-timezones
```


### Step 2 - Update your AA settings

Configure your AA settings (`local.py`) as follows:

- Add `'timezones',` to `INSTALLED_APPS`


### Step 3 - Finalize the installation

Run migrations & copy static files

```bash
python manage.py collectstatic
python manage.py migrate
```

Restart your supervisor services for AA

Once done, it's time to add all the time zone informations, so you can define your
own set of panels later. To do so, simply run:

```bash
python manage.py timezones_load_tz_data
```


### Step 4 - Setup permissions

Now you can setup permissions in Alliance Auth for your users.
Add ``timezones|aa timezones|Can access ths app`` to the states and/or groups you would
like to have access.


## Updating

To update your existing installation of AA Time Zones first enable your virtual environment.

Then run the following commands from your AA project directory (the one that contains `manage.py`).

```bash
pip install -U aa-timezones
```

```bash
python manage.py collectstatic
```

```bash
python manage.py migrate
```

Now restart your AA supervisor services.


## Configure Timezone Panels
Per default there are 10 additional time zone panels that are displayed (see first image).
If you want to change those, you can create your own set of panels in your admin backend.

**NOTE:** "Local Time" and "EVE Time" will always be displayed as the first two panels,
no matter what.


## Adjusting Time

You can easiely adjust the time that is displayed for all timezones.
This is useful for reinforcement timers or pre-planned fleets. To do so,
click on the "Adjust Time" button below the time zone panels and you will see 2 different ways to set a new time.

![Adjusting Time](https://raw.githubusercontent.com/ppfeufer/aa-timezones/master/timezones/docs/adjust-time.jpg)

The first one is meant for timers, like reinforcement timers, anchoring timers or the like.
It's maximum is 7 day, 59 minutes and 59 seconds into the future. That should cover pretty much all
timers you can find in Eve Online.

The second one is best suited for pre-planned fleets. Here you can set a fixed date and time based
on the selected time zone. The default selected time zone is "EVE Time" but you can change it
to all the available options. Keep in mind, the selected time zone is the one the time and date will be adjusted to.
So if you are going to use it to plan fleets it is recommanded to keep this set to "EVE Time".

To set the adjusted time, simply click on "Set Time" in the row you altered. This will than adjust all
time zone panels to the time you selected and will also alter the link in your browser, so you can share it
with others directly.
