# AA Time Zones<a name="aa-time-zones"></a>

[![Version](https://img.shields.io/pypi/v/aa-timezones?label=release)](https://pypi.org/project/aa-timezones/)
[![License](https://img.shields.io/github/license/ppfeufer/aa-timezones)](https://github.com/ppfeufer/aa-timezones/blob/master/LICENSE)
[![Python](https://img.shields.io/pypi/pyversions/aa-timezones)](https://pypi.org/project/aa-timezones/)
[![Django](https://img.shields.io/pypi/djversions/aa-timezones?label=django)](https://pypi.org/project/aa-timezones/)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ppfeufer/aa-timezones/master.svg)](https://results.pre-commit.ci/latest/github/ppfeufer/aa-timezones/master)
[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](http://black.readthedocs.io/en/latest/)
[![Discord](https://img.shields.io/discord/790364535294132234?label=discord)](https://discord.gg/zmh52wnfvM)
[![Checks](https://github.com/ppfeufer/aa-timezones/actions/workflows/automated-checks.yml/badge.svg)](https://github.com/ppfeufer/aa-timezones/actions/workflows/automated-checks.yml)
[![codecov](https://codecov.io/gh/ppfeufer/aa-timezones/branch/master/graph/badge.svg?token=ZSRTW5FR4C)](https://codecov.io/gh/ppfeufer/aa-timezones)
[![Translation status](https://weblate.ppfeufer.de/widget/alliance-auth-apps/aa-timezones/svg-badge.svg)](https://weblate.ppfeufer.de/engage/alliance-auth-apps/)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](https://github.com/ppfeufer/aa-timezones/blob/master/CODE_OF_CONDUCT.md)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/N4N8CL1BY)

App for displaying different time zones with Alliance Auth

______________________________________________________________________

<!-- mdformat-toc start --slug=github --maxlevel=6 --minlevel=2 -->

- [Installation](#installation)
  - [Step 1: Install the App](#step-1-install-the-app)
  - [Step 2: Update Your Alliance Auth Settings](#step-2-update-your-alliance-auth-settings)
  - [Step 3: Finalizing the Installation](#step-3-finalizing-the-installation)
- [(Optional) Public Views](#optional-public-views)
- [Updating](#updating)
- [Configure the Timezone Panels](#configure-the-timezone-panels)
- [Adjusting Time](#adjusting-time)
- [Discord Bot Command](#discord-bot-command)
- [Changelog](#changelog)
- [Translation Status](#translation-status)
- [Contributing](#contributing)

<!-- mdformat-toc end -->

______________________________________________________________________

![Time Zones](https://raw.githubusercontent.com/ppfeufer/aa-timezones/master/docs/images/presentation/aa-timezones.jpg)

## Installation<a name="installation"></a>

> [!NOTE]
>
> **AA Time Zones >= 2.0.0 needs at least Alliance Auth v4.0.0!**
>
> Please make sure to update your Alliance Auth instance _before_ you install this
> module or update to the latest version, otherwise an update to Alliance Auth will
> be pulled in unsupervised.
>
> The last version compatible with Alliance Auth v3 is `1.16.2`.

### Step 1: Install the App<a name="step-1-install-the-app"></a>

Make sure you're in the virtual environment (venv) of your Alliance Auth installation.
Then install the latest version:

```bash
pip install aa-timezones
```

### Step 2: Update Your Alliance Auth Settings<a name="step-2-update-your-alliance-auth-settings"></a>

Configure your AA settings (`local.py`) as follows:

- Add `'timezones',` to `INSTALLED_APPS`

### Step 3: Finalizing the Installation<a name="step-3-finalizing-the-installation"></a>

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

## (Optional) Public Views<a name="optional-public-views"></a>

This app supports AA's feature of public views, since time zones conversion is not
any mission-critical information. To allow users to view the time zone conversion page
without the need to log in, please add `"timezones",` to the list of
`APPS_WITH_PUBLIC_VIEWS` in your `local.py`:

```python
# By default, apps are prevented from having public views for security reasons.
# To allow specific apps to have public views, add them to APPS_WITH_PUBLIC_VIEWS
#   » The format is the same as in INSTALLED_APPS
#   » The app developer must also explicitly allow public views for their app
APPS_WITH_PUBLIC_VIEWS = [
    "timezones",  # https://github.com/ppfeufer/aa-timezones
]
```

> **Note**
>
> If you don't have a list for `APPS_WITH_PUBLIC_VIEWS` yet, then add the whole
> block from here. This feature has been added in Alliance Auth v3.6.0 so you
> might not yet have this list in your `local.py`.

## Updating<a name="updating"></a>

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

## Configure the Timezone Panels<a name="configure-the-timezone-panels"></a>

Per default, there are 10 additional time zone panels that are displayed (see first
image). If you want to change those, you can create your own set of panels in your
admin backend.

**NOTE:** "Local time" and "EVE time" will always be displayed as the first two panels,
no matter what.

## Adjusting Time<a name="adjusting-time"></a>

You can easily adjust the time that is displayed for all timezones. This is useful
for reinforcement timers or pre-planned fleets. To do so, click on the "Adjust Time"
button below the time zone panels, and you will see 2 different ways to set a new time.

![Adjusting Time](https://raw.githubusercontent.com/ppfeufer/aa-timezones/master/docs/images/weblate/aa-timezones_adjust-time-settings.jpg)

The first one is meant for timers, like reinforcement timers, anchoring timers or
the like. Its maximum is 7 days, 59 minutes and 59 seconds into the future. That
should cover pretty much all timers you can find in Eve Online.

The second one is best suited for pre-planned fleets. Here you can set a fixed date
and time based on the selected time zone. The default selected time zone is "EVE
time" but you can change it to all the available options. Keep in mind the selected
time zone is the one the time and date will be adjusted to. So if you are going to
use it to plan fleets, it is recommended to keep this set to "EVE time".

To set the adjusted time, simply click on "Set Time" in the row you altered. This
will then adjust all time zone panels to the time you selected and will also alter
the link in your browser, so you can share it with others directly.

## Discord Bot Command<a name="discord-bot-command"></a>

**For this to work, you'll need to have `allianceauth-discordbot` installed, configured
and running.** ([See this link](https://github.com/pvyParts/allianceauth-discordbot))

| Command | Effect                                                                                                                                                                                                                     |
| :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/time` | Displays the current EVE time and what time it is in the configured time zones<br>![Discord Bot Response](https://raw.githubusercontent.com/ppfeufer/aa-timezones/master/docs/images/presentation/discordbot-response.jpg) |

## Changelog<a name="changelog"></a>

See [CHANGELOG.md](https://github.com/ppfeufer/aa-timezones/blob/master/CHANGELOG.md)

## Translation Status<a name="translation-status"></a>

[![Translation status](https://weblate.ppfeufer.de/widget/alliance-auth-apps/aa-timezones/multi-auto.svg)](https://weblate.ppfeufer.de/engage/alliance-auth-apps/)

Do you want to help translate this app into your language or improve the existing
translation? - [Join our team of translators][weblate engage]!

## Contributing<a name="contributing"></a>

Do you want to contribute to this project? That's cool!

Please make sure to read the [Contribution Guidelines].\
(I promise, it's not much, just some basics)

<!-- Inline Links -->

[contribution guidelines]: https://github.com/ppfeufer/aa-timezones/blob/master/CONTRIBUTING.md "Contribution Guidelines"
[weblate engage]: https://weblate.ppfeufer.de/engage/alliance-auth-apps/ "Weblate Translations"
