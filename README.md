# AA Time Zones

[![Version](https://img.shields.io/pypi/v/aa-timezones?label=release)](https://pypi.org/project/aa-timezones/)
[![License](https://img.shields.io/github/license/ppfeufer/aa-timezones)](https://github.com/ppfeufer/aa-timezones/blob/master/LICENSE)
[![Python](https://img.shields.io/pypi/pyversions/aa-timezones)](https://pypi.org/project/aa-timezones/)
[![Django](https://img.shields.io/pypi/djversions/aa-timezones?label=django)](https://pypi.org/project/aa-timezones/)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)
[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](http://black.readthedocs.io/en/latest/)
[![Discord](https://img.shields.io/discord/790364535294132234?label=discord)](https://discord.gg/zmh52wnfvM)
[![Checks](https://github.com/ppfeufer/aa-timezones/actions/workflows/automated-checks.yml/badge.svg)](https://github.com/ppfeufer/aa-timezones/actions/workflows/automated-checks.yml)
[![codecov](https://codecov.io/gh/ppfeufer/aa-timezones/branch/master/graph/badge.svg?token=ZSRTW5FR4C)](https://codecov.io/gh/ppfeufer/aa-timezones)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](https://github.com/ppfeufer/aa-timezones/blob/master/CODE_OF_CONDUCT.md)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/N4N8CL1BY)

App for displaying different time zones with Alliance Auth


---

<!-- TOC -->
* [AA Time Zones](#aa-time-zones)
  * [Installation](#installation)
    * [Step 1: Install the App](#step-1-install-the-app)
    * [Step 2: Update Your Alliance Auth Settings](#step-2-update-your-alliance-auth-settings)
    * [Step 3: Finalizing the Installation](#step-3-finalizing-the-installation)
    * [Step 4: Setting up the permissions](#step-4-setting-up-the-permissions)
  * [Updating](#updating)
  * [Configure the Timezone Panels](#configure-the-timezone-panels)
  * [Adjusting Time](#adjusting-time)
  * [Discord Bot Command](#discord-bot-command)
<!-- TOC -->

---


![Time Zones](https://raw.githubusercontent.com/ppfeufer/aa-timezones/master/timezones/docs/screenshots/time-zones.jpg)


## Installation

**Important**: This app is a plugin for Alliance Auth.
If you don't have Alliance Auth running already, please install it first before
proceeding. (See the official
[AA installation guide](https://allianceauth.readthedocs.io/en/latest/installation/allianceauth.html)
for details)


### Step 1: Install the App

Make sure you're in the virtual environment (venv) of your Alliance Auth installation.
Then install the latest version:

```bash
pip install aa-timezones
```


### Step 2: Update Your Alliance Auth Settings

Configure your AA settings (`local.py`) as follows:

- Add `'timezones',` to `INSTALLED_APPS`


### Step 3: Finalizing the Installation

Run migrations & copy static files

```bash
python manage.py collectstatic
python manage.py migrate
```

Restart your supervisor services for AA

Once done, it's time to add all the time zone information, so you can define your
own set of panels later. To do so, simply run:

```bash
python manage.py timezones_load_tz_data
```


### Step 4: Setting up the permissions

Now you can set up permissions in Alliance Auth for your users.
Add ``timezones|aa timezones|Can access ths app`` to the states and/or groups you would
like to have access.


## Updating

To update your existing installation of AA Time Zones, first enable your virtual
environment.

Then run the following commands from your AA project directory (the one that
contains `manage.py`).

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


## Configure the Timezone Panels
Per default, there are 10 additional time zone panels that are displayed (see first
image). If you want to change those, you can create your own set of panels in your
admin backend.

**NOTE:** "Local Time" and "EVE Time" will always be displayed as the first two panels,
no matter what.


## Adjusting Time

You can easily adjust the time that is displayed for all timezones. This is useful
for reinforcement timers or pre-planned fleets. To do so, click on the "Adjust Time"
button below the time zone panels, and you will see 2 different ways to set a new time.

![Adjusting Time](https://raw.githubusercontent.com/ppfeufer/aa-timezones/master/timezones/docs/screenshots/weblate/adjust-time-settings.jpg)

The first one is meant for timers, like reinforcement timers, anchoring timers or
the like. Its maximum is 7 days, 59 minutes and 59 seconds into the future. That
should cover pretty much all timers you can find in Eve Online.

The second one is best suited for pre-planned fleets. Here you can set a fixed date
and time based on the selected time zone. The default selected time zone is "EVE
Time" but you can change it to all the available options. Keep in mind the selected
time zone is the one the time and date will be adjusted to. So if you are going to
use it to plan fleets, it is recommended to keep this set to "EVE Time".

To set the adjusted time, simply click on "Set Time" in the row you altered. This
will then adjust all time zone panels to the time you selected and will also alter
the link in your browser, so you can share it with others directly.


## Discord Bot Command

**For this to work, you'll need to have `allianceauth-discordbot` installed, configured
and running.** ([See this link](https://github.com/pvyParts/allianceauth-discordbot))

| Command            | Effect                                                                                                                                                                                                                         |
|:-------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `!time` or `/time` | Shows the current Eve time and what time it is in the <br/>configured time zones<br>![Discord Bot Response](https://raw.githubusercontent.com/ppfeufer/aa-timezones/master/timezones/docs/screenshots/discordbot-response.jpg) |
