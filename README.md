# rskit

[![PyPI version](https://badge.fury.io/py/rskit.svg)](https://badge.fury.io/py/rskit)
[![Build Status](https://travis-ci.org/micaleel/rskit.svg?branch=master)](https://travis-ci.org/micaleel/rskit)

Toolkit for building recommender systems

- Provide CLI interface for running recommendation algorithms
- Contains abstractions you can leverage to build custom recommenders


## Installation

```bash
pip install rskit
```


## Development
For development, you may use below to create a Python interpreter that resides in `venv` in the current working directory, and to install all of rskit's dependencies:

```
$ virtualenv venv 
$ source venv/bin/activate
$ pip install -e .
$ pip install -r requirements-dev.txt
$ rskit --help # should work
```

Because the script installs the package as editable, you can make changes in the source tree and use the `rskit` command to immediately validate them. If this does not appear to work, check that you are using a the proper virtual environment, and that the package is indeed installed in editable mode:

```
$ which rskit # should point into your virtualenv
/path/to/my/venv/bin/rskit
$ pip list --local | grep rskit # should point to the source tree
rskit                0.0.1                /project/rskit
```

Please refer to the `Makefile` for supplementary development tasks.
In particular, the following targets may be relevant when validating changes before committing:

```
$ make lint # check rskit's source for code style errors
$ make test # run all tests
```

## Motivation

Our motivation is to simplify and standardise the process of building, benchmarking and deploying recommender systems.

## Contribute

To discuss ideas and to report problems, open an issue or open an issue or send a pull request. All contributions are welcomed. 