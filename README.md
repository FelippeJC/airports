<!-- PROJECT SHIELDS -->
![Version](https://img.shields.io/github/tag/FelippeJC/airports.svg)
![Status](https://img.shields.io/github/commit-status/FelippeJC/airports/master/c0e38b0a90a5008e4f3544f3adddeb3d1fdb1386.svg)
![Size](https://img.shields.io/github/repo-size/FelippeJC/airports.svg)
[![License](https://img.shields.io/github/license/FelippeJC/airports.svg?color=blue&logo=license)](http://badges.mit-license.org)

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/felippejc/airports">
    <img src="static/img/travel.ico" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Airports App</h3>

  <p align="center">
    Just a tool for finding info about airports by searching its IATA code.
  </p>
</p>

---

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. For lazyness there's a database in project.

### Prerequisites

You'll need python (version 2.7 is the original of the project) and pip installed.

### How to set up

##### Create a virtual environment

```
virtualenv [foldername]
```

If you're using windows you may have to use this instead

```
python -m virtualenv [foldername]
```

##### Activate the virtual environment 

```
[virtualenv foldername]/Scripts/activate
```

##### Install the requirements

```
pip install requirements.txt
```

##### Set the environment variables

* ``FLASK_APP`` as *the app name*
* ``FLASK_ENV`` as *development*

### Running the app

If it's all setup run the command from the project path:

```
flask run
```

### Setting a database (if needed)

Go with the regular `flask db init`, `flask db migrate`, `flask db upgrade`.
The folder nth has a script to populate the app airports table from a csv.

