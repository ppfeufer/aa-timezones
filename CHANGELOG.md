# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

<!--
GitHub MD Syntax:
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

Highlighting:
https://docs.github.com/assets/cb-41128/mw-1440/images/help/writing/alerts-rendered.webp

> [!NOTE]
> Highlights information that users should take into account, even when skimming.

> [!IMPORTANT]
> Crucial information necessary for users to succeed.

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.
-->

## \[In Development\] - Unreleased

<!--
Section Order:

### Added
### Fixed
### Changed
### Deprecated
### Removed
### Security
-->

### Added

- Integrity checks for CSS and JS files

### Fixed

- Minimized drift in countdown timer

## \[2.2.0\] - 2024-09-16

### Changed

- Dependencies updated
  - `allianceauth`>=4.3.1
- Japanese translation improved
- Lingua codes updated to match Alliance Auth v4.3.1

## \[2.1.0\] - 2024-07-30

### Changed

- French translation updated

### Removed

- Support for Python 3.8 and Python 3.9

## \[2.0.1\] - 2024-05-16

### Changed

- Translations updated

## \[2.0.0\] - 2024-03-16

> \[!NOTE\]
>
> **This version needs at least Alliance Auth v4.0.0!**
>
> Please make sure to update your Alliance Auth instance **before**
> you install this version, otherwise, an update to Alliance Auth will
> be pulled in unsupervised.

### Added

- Compatibility to Alliance Auth v4
  - Bootstrap 5
  - Django 4.2

### Changed

- JS modernized
- CSS modernizes
- Templates changed to Bootstrap 5

### Removed

- Compatibility to Alliance Auth v3

## \[2.0.0-beta.1\] - 2024-02-18

> \[!NOTE\]
>
> **This version needs at least Alliance Auth v4.0.0b1!**
>
> Please make sure to update your Alliance Auth instance **before**
> you install this version, otherwise, an update to Alliance Auth will
> be pulled in unsupervised.

### Added

- Compatibility to Alliance Auth v4
  - Bootstrap 5
  - Django 4.2

### Changed

- JS modernized
- CSS modernizes
- Templates changed to Bootstrap 5

### Removed

- Compatibility to Alliance Auth v3

## \[1.16.2\] - 2023-09-26

> \[!NOTE\]
>
> **This is the last version compatible with Alliance Auth v3.**

### Fixed

- Capitalization for translatable strings
- Translatable strings in dropdown in admin backend

### Changed

- Translations updated
- Test suite updated

## \[1.16.1\] - 2023-09-02

### Changed

- Korean translation improved

## \[1.16.0\] - 2023-08-29

### Added

- Korean translation

## \[1.15.0\] - 2023-08-16

### Added

- Spanish translation

## \[1.14.1\] - 2023-08-13

### Fixed

- Bootstrap CSS fix

## \[1.14.0\] - 2023-08-10

> **Warning**
>
> The update makes use of a feature introduced in Allianceauth v3.6.1, meaning this
> update will pull in Allianceauth v3.6.1 unsupervised. Please make sure to update
> Allianceauth to this version beforehand to avoid any complications.

### Added

- Support public views (see [README])

### Change

- Moved helper functions out of the class

### Removed

- Deprecated `!time` command, use `/time` instead

## \[1.13.2\] - 2023-07-30

### Added

- Bootstrap CSS fix
- Footer to promote help with the app translation

### Change

- German translation improved
- Russian translation improved
- Italian translation improved
- Spanish translation improved
- French translation improved
- Chinese translation improved
- Japanese translation improved
- Korean translation improved

## \[1.13.1\] - 2023-06-16

### Added

- Screenshots for Weblate

### Change

- Show the date before the time in the panels
- JS in the templates modernized
- Translations updated

### Removed

- Unnecessary template block

## \[1.13.0\] - 2023-04-23

### Added

- Ukrainian translation (for upcoming AA update which adds the Ukrainian language)

### Changed

- German translation updated
- Russian translation updated
- Moved the build process to PEP 621 / pyproject.toml

## \[1.12.1\] - 2023-04-13

### Changed

- Code modernization. Using Django decorators in `admin.py`
- Using `allianceauth-app-utils` to get the absolute URL
- German translation updated

## \[1.12.0\] - 2022-09-15

### Added

- Local time to the bot command's output

### Changed

- External JS library updated due to security issue
- CSS and JS moved to their own bundled templates
- Minimum Requirement:
  - Alliance Auth >= 3.0.0

## \[1.11.0\] - 2022-07-11

### Fixed

- A Typo :-)

### Changed

- Minimum Requirement:
  - Alliance Auth >= 2.14.0

## \[1.10.1\] - 2022-06-12

### Added

- Deprecation warning when the `!time` command is used, advising to use `/time` instead

### Fixed

- "Method could be a function" warning

## \[1.10.0\] - 2022-06-07

### Added

- Cog for `allianceauth-discordbot` to implement the `/time` command for Discord
  - **Advice:** Please make sure `aadiscordbot` is listed _before_ `timezones` in
    `INSTALLED_APPS` in your `local.py` to prevent an error from spawning in your
    log file. It will still work, but the error is annoying and might cause
    unnecessary questions in the Alliance Auth support Discord.
- `pytz` to dependencies. Can't rely on other packages for dragging it in

### Changed

- JS modernized (Part 2)
- Management command for the initial timezones imports optimised

## \[1.9.0\] - 2022-03-03

### Added

- Test suite for AA 3.x and Django 4

### Changed

- Switched to `setup.cfg` as config file, since `setup.py` is deprecated now

### Removed

- Deprecated settings

## \[1.8.0\] - 2022-02-28

### Fixed

- \[Compatibility\] AA 3.x / Django 4 :: ImportError: cannot import name
  'ugettext_lazy' from 'django.utils.translation'

## \[1.7.1\] - 2022-02-02

### Changed

- Using `path` in URL config instead of soon-to-be removed `url`

## \[1.7.0\] - 2022-01-12

### Changed

- JavaScript: `const` instead of `let` where ever appropriate

## \[1.6.0\] - 2022-01-10

### Added

- Tests for Python 3.11

### Changed

- Minimum requirements
  - Alliance Auth v2.9.4
- JS options combined into one array instead of three

### Removed

- Backwards compatibility with old timecode style URLs (was deprecated with v1.2.1
  in October 2020)

## \[1.5.0\] - 2021-11-30

### Changed

- Minimum requirements
  - Python 3.7
  - Alliance Auth v2.9.3

## \[1.4.0\] - 2021-11-23

### Added

- Versioned static files to break the browser cache on version changes

### Removed

- tasks.py file, since we don't have tasks in this app

### Updated

- JS files to the newest versions
  - timeago.js
  - moments-timezones script

## \[1.3.6\] - 2021-11-21

### Added

- Test suite

### Changed

- JavaScript modernised

## \[1.3.5\] - 2021-11-17

### Added

- Russian translation (Thanks to -7- \[0RIG\] Neomad Miromme)

## \[1.3.4\] - 2021-07-08

### Added

- Check for compatibility with Python 3.9 and Django 3.2

## \[1.3.3\] - 2021-06-19

### Changed

- Minimize the number of SQL queries to improve performance

## \[1.3.2\] - 2021-03-15

### Fixed

- Month number for March in time selection

## \[1.3.1\] - 2021-01-28

### Changed

- Moved `AA_TIMEZONE_DEFAULT_PANELS` into its own constants file, so it can be used
  by other apps as well.

## \[1.3.0\] - 2021-01-12

### Removed

- Django 2 support

## \[1.2.2\] - 2020-12-16

### Fixed

- Bootstap classes in template

## \[1.2.1\] - 2020-10-09

### Fixed

- Column name in admin view
- Timezones re-added in selector in adjust time mode

### Added

- Summary after time zone import during install

### Changed

- Timestamp is now a real part of the URL instead of a hash added to it. The old
  URLs with the hash are still supported and work as well in case you have links to
  it somewhere ...

### Updated

- German translation

## \[1.2.0\] - 2020-09-27

### Changed

- Settings moved to database instead of `local.py`

## \[1.1.0\] - 2020-09-23

### Checked

- Compatibility with the upcoming changes in Alliance Auth v2.8.0 (Django 3)

### Added

- German translation to UI
- Translations for Russian, Spanish, Korean and Chinese prepared, need translators
  though. So if you want to help out, [feel free to do so here](https://weblate.ppfeufer.de/projects/alliance-auth-apps/aa-timezones/).

## \[1.0.0\] - 2020-09-13

### Changed

- use moment.js provided by AA. No need to provide our own when AA does that for us.
  If you are concerned about using the cloudflare CDN, try using the
  [AA GDPR](https://gitlab.com/soratidus999/aa-gdpr) package

## \[0.1.9\] - 2020-08-01

### Fixed

- Hours, minutes and seconds now have a leading 0 when below 10
- When the countdown is over, it no longer counts into negative

### Changed

- Countdown text "Time left" instead of "Time until"

## \[0.1.8\] - 2020-06-23

### Added

- Time until in "Set Time" mode (#19)

## \[0.1.7\] - 2020-06-11

### Changed

- Menu icon updated to FontAwesome v5, which allianceauth uses since 2.7.2

## \[0.1.6\] - 2020-06-09

### Changed

- Readme updated
- Prepared to be served via Pypi

## \[0.1.5\] - 2020-05-17

### Added

- Set up your own additional time zone panels via `local.py` (see readme)

## \[0.1.4\] - 2020-05-16

### Changed

- Button labels to better reflect what they're doing
- Month numbers into names in the Adjust Time section
- Adjust time buttons are now a bit larger
- Order of information in the time zone panels

## \[0.1.3\] - 2020-05-15

### Added

- UTC offset

### Updated

- moment.js and timeago.js to their latest versions

## \[0.1.2\] - 2020-05-15

### Changed

- TZ panels now have their own template
- The Chinese TZ panel now has also Russia / Siberia

## \[0.1.1\] - 2020-05-14

### Fixed

- Bootstrap template hierarchy

## \[0.1.0\] - 2020-05-14

### Added

- initial version

<!-- Links -->

[readme]: https://github.com/ppfeufer/aa-timezones/blob/master/README.md "README.md"
