# Contributing<a name="contributing"></a>

______________________________________________________________________

<!-- mdformat-toc start --slug=github --maxlevel=6 --minlevel=1 -->

- [Contributing](#contributing)
  - [Development Environment](#development-environment)
  - [Code Formatting and Linting](#code-formatting-and-linting)
    - [Python](#python)
    - [JavaScript](#javascript)
      - [Minified JS](#minified-js)
    - [CSS](#css)
      - [Minified CSS](#minified-css)
    - [pre-commit](#pre-commit)
  - [Branching and Contributing via Pull Requests](#branching-and-contributing-via-pull-requests)
    - [Tests](#tests)
    - [Checklist](#checklist)
  - [Translation](#translation)

<!-- mdformat-toc end -->

______________________________________________________________________

## Development Environment<a name="development-environment"></a>

To develop and test your change, you will need a development environment on your
local machine. There are many different options to choose from. But please make sure
that you can run pre-commit checks and tox tests on your local machine.

If you are on Windows or Linux, you can use the [AA guide for setting up a dev
environment][aa guide for setting up a dev environment].

## Code Formatting and Linting<a name="code-formatting-and-linting"></a>

### Python<a name="python"></a>

This app is using the [Black code style]. Every commit has to adhere to it.

When making changes to the source code, please always reformat the changed files
to ensure consistent formatting across the code base.

To reformat, run the following from the app's root directory:

```shell
pre-commit run black
```

### JavaScript<a name="javascript"></a>

The JavaScript code follows [ECMAScript 6 (or ES6 for short)][ecmascript 6] or newer
rules. The use of arrow functions is preferred and `this` or `$(this)` should be
prevented. Functions need to be declared before their use and the JavaScript code
should follow `'use strict';`.

Indent size: 4 spaces

A linter configuration is declared as `.eslintrc.json` in the app's root directory.
Do not change this file.

To check that your JavaScript code adheres to the rules, run:

```shell
pre-commit run eslint
```

#### Minified JS<a name="minified-js"></a>

This project uses minified and compressed JavaScript files with source maps created by
[UglifyJS]. Make sure to add/update them as well if you add or change JavaScript.

To do so, run:

```shell
uglifyjs script.js -o script.min.js --source-map "url='script.min.js.map'" --compress --mangle
```

### CSS<a name="css"></a>

The CSS should be written in a modern manner. Color definitions should be in
modern RGB(A) (`rgb(255 255 255)`, `rgba(255 255 255 / 50%)`) for example.

A linter configuration is declared as `.stylelintrc.json` in the app's root
directory. Do not change this file.

Indent size: 4 spaces

To check that your JavaScript code adheres to the rules, run:

```shell
pre-commit run stylelint
```

#### Minified CSS<a name="minified-css"></a>

This project uses minified CSS files with source maps created by [CSSO]. Make sure
to add/update them as well if you add or change CSS.

```shell
csso -i styles.css -o styles.min.css  -s file
```

### pre-commit<a name="pre-commit"></a>

This repository uses [pre-commit] to verify compliance with formatting / linting rules.
To use:

- Install `pre-commit` to your system.
- Run' pre-commit install' inside the app's root directory.
- You're all done! Code will be checked automatically using git hooks.

You can check if your code to commit adheres to the given style by simply running:

```shell script
pre-commit
```

Or to check all files:

```shell script
pre-commit run --all-files
```

The following will be checked by `pre-commit` (among others):

- No trailing whitespaces (excluded are minified js and css, .po and .mo files and
  external libs)
- One, and only one, empty line at the end of every file (excluded are minified js
  and css, .po and .mo files and external libs)
- Line ending is LF
- Python code formatted according to black code style
- Python code blocks in markdown files are formatted to black code style
- Code conforms with flake8
- Code generally adheres to the editor config
- Python code is updated to the minimal Python version
- Python code is updated to the minimal Django version
- Imports in Python code are sorted properly
- Markdown files are formatted properly
- No pylint issues

## Branching and Contributing via Pull Requests<a name="branching-and-contributing-via-pull-requests"></a>

To contribute code via pull request, make sure that you fork the repository and
branch your changes from the `master` branch.

We strongly recommend creating a new branch for every new feature or change you
plan to be submitting as merge request. Please make sure to keep the `master` branch of
your fork in sync with the main repository to avoid conflicts.

Before you start working on a new feature, please open an Issue (Type: Feature
Request) and start a discussion if your idea is generally wanted and considered a
good addition to the app in general.

Please feel free to create your merge request early and while you are still not
finished developing to flag that you are working on a specific topic. Merge requests
that are not yet ready to review should be marked as DRAFT. You can signal others
that your merge request is ready for review by removing the DRAFT flag again.

### Tests<a name="tests"></a>

Please update existing or provide additional unit tests for your changes. Note that
your merge request might fail if it reduces the current level of test coverage.

We are using [Python unittest] with the Django `TestCase` class for all tests. In
addition, we are using some following third party test tools:

- django-webtest / [WebTest] - testing the web UI
- [request-mock] — testing requests with the `requests` library
- [tox] — Running the test suite
- [coverage] — Measuring the test coverage

### Checklist<a name="checklist"></a>

Before you submit a pull request, please make sure that:

- [ ] Your code follows the style guidelines of this project
- [ ] Your changes are supported and covered by tests
- [ ] You have performed a self-review of your own code
- [ ] You have commented on your code, particularly in hard-to-understand areas
- [ ] You have checked your code and corrected any misspellings

## Translation<a name="translation"></a>

This app is fully translation-ready and translations are handled via [Weblate]. If
you like to contribute to the app's translation or improve it, feel free to
register on my [Weblate] instance and start translating.

<!-- Links -->

[aa guide for setting up a dev environment]: https://allianceauth.readthedocs.io/en/latest/development/dev_setup/aa-dev-setup-wsl-vsc-v2.html "AA Guide for Setting up a Dev Environment"
[black code style]: https://black.readthedocs.io/en/latest/l "Black Code Style"
[coverage]: https://coverage.readthedocs.io/en/latest/ "coverage"
[csso]: https://github.com/css/csso "CSSO (CSS Optimizer)"
[ecmascript 6]: https://www.w3schools.com/js/js_es6.asp "JavaScript ECMAScript 6"
[pre-commit]: https://github.com/pre-commit/pre-commit "pre-commit"
[python unittest]: https://docs.python.org/3/library/unittest.html "Python Unittests"
[request-mock]: https://requests-mock.readthedocs.io/en/latest/ "request-mock"
[tox]: https://tox.wiki/en/latest/ "tox"
[uglifyjs]: https://github.com/mishoo/UglifyJS "UglifyJS"
[weblate]: https://weblate.ppfeufer.de/ "Weblate"
[webtest]: https://docs.pylonsproject.org/projects/webtest/en/latest/ "Webtest"
