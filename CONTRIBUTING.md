# Contributing<a name="contributing"></a>

______________________________________________________________________

<!-- mdformat-toc start --slug=github --maxlevel=6 --minlevel=1 -->

- [Contributing](#contributing)
  - [Code Formatting](#code-formatting)
    - [Python](#python)
    - [JavaScript](#javascript)
    - [CSS](#css)
    - [pre-commit](#pre-commit)
  - [Contributing via Pull Requests](#contributing-via-pull-requests)
    - [Checklist](#checklist)
  - [Translation](#translation)

<!-- mdformat-toc end -->

______________________________________________________________________

## Code Formatting<a name="code-formatting"></a>

### Python<a name="python"></a>

This app is utilizing the [Black code style]. Every commit has to adhere to it.

When making changes to the source code, please always reformat the changed files in
order to ensure consistent formatting across the code base.

To reformat run the following from the app's root directory:

```shell
pre-commit run black
```

### JavaScript<a name="javascript"></a>

The JavaScript code follows [ECMAScript 6 (or ES6 for short)][ecmascript 6] or later
rules. The use of arrow functions is preferred and `this` or `$(this)` should be
prevented. Functions need to be declared before their use and the JavaScript code
should follow `'use strict';`.

Indent size: 4 spaces

A linter configuration is declared as `.eslintrc.json` in the app's root directory.

To check that your JavaScript code adheres to the rules, run:

```shell
pre-commit run eslint
```

### CSS<a name="css"></a>

The CSS should be written in a modern manner. Colour definitions should be in RGB(A)
(`rgb(255 255 255)`, `rgba(255 255 255 / 50%)`) for example.

A linter configuration is declared as `.stylelintrc.json` in the app's root directory.

Indent size: 4 spaces

To check that your JavaScript code adheres to the rules, run:

```shell
pre-commit run stylelint
```

### pre-commit<a name="pre-commit"></a>

This repository uses [pre-commit] to verify compliance with formatting / linting rules.
To use:

1. Install `pre-commit` to your system.
1. Run' pre-commit install' inside the app's root directory.
1. You're all done! Code will be checked automatically using git hooks.

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

## Contributing via Pull Requests<a name="contributing-via-pull-requests"></a>

To contribute code via pull request, make sure that you fork the repository and
branch your changes from the `development` branch. Only pull requests towards the
development branch will be considered.

Before you start working on a new feature, please open an Issue (Type: Feature
Request) and start a discussion if your idea is generally wanted and considered a
good addition to the app in general.

### Checklist<a name="checklist"></a>

Before you submit a pull request, please make sure that:

- [ ] Your code follows the style guidelines of this project
- [ ] Your changes are supported and covered by tests
- [ ] You have performed a self-review of your own code
- [ ] You have commented on your code, particularly in hard-to-understand areas
- [ ] You have checked your code and corrected any misspellings

## Translation<a name="translation"></a>

This app is fully translation-ready and translations are handled via [Weblate]. If
you like to contribute to the app's translation or simply improve it, feel free to
register on my [Weblate] instance and start translating.

<!-- Links -->

[black code style]: https://black.readthedocs.io/en/latest/l "Black Code Style"
[ecmascript 6]: https://www.w3schools.com/js/js_es6.asp "JavaScript ECMAScript 6"
[pre-commit]: https://github.com/pre-commit/pre-commit "pre-commit"
[weblate]: https://weblate.ppfeufer.de/ "Weblate"
