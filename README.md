# P10_SoftDesk
## Table of contents
- [Table of content](#table-of-content)
- [Foreword](#foreword)
- [Installation](#installation)
- [How to use](#how-to-use)
- [Possible improvements](#possible-improvements)

## Foreword

The aim of this project is to build an API which will be used in several type of platforms.

This API allows users to :
- create projects
- to add users to specifics projects,
- to create issues related to projects
- to create comments related to issues

In order to use it, users have to register first and the connect to the API.

The different endpoints required specific permissions in order to be used.

I have to use Django REST framework to build this API

I also have to follow OWASP top 10 list

You can read [here](https://documenter.getpostman.com/view/19888768/UzXNSwkf#c319d242-22d4-4636-b9d2-1cc7d3a67562) the documentstion of the API :

## Installation

### Clone the code source (using ssh)

    mkdir foo
    git clone git@github.com:jjbochard/P10_SoftDesk.git foo
    cd foo

### Create your virtual environnement

First, install [Python 3.6+](https://www.python.org/downloads/).

Then, create your virtual environnement :

    python3 -m venv <your_venv_name>

Activate it :

- with bash command prompt

        source <your_venv_name>/bin/activate

- or with Windows PowerShell

        .\venv\Scripts\activate

Finally, install required modules

    pip3 install -r requirements.txt

To deactivate your venv :

    deactivate

### Django management commands and run Django

First, apply all migrations to the database :

    django softdesk/manage.py migrate


Then, start the server

    django softdesk/manage.py runserver

### Optionnal : configure your git repository with pre-commit (if you want to fork this project)

You can install pre-commit with python

    pip install pre-commit

You can install the configured pre commit hook with

    pre-commit install

## How to use

You can use [Postman](https://www.postman.com/) in order to test the endpoints

## Possible improvements
