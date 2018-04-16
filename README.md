# Simple Flask skeleton app

## Includes with Vue/Laravel-Mix frontend pipeline and Bulma bootstrap

### What is this

- largely based on some skeletons found on github
- uses Pipenv for virtual environment and local variables (.env file)
- uses laravel-mix with Vue widgets for frontend client
- intended for simple prototyping using separate client/server domains
- includes vue, lodash, axios, moment and bulma as already installed modules

### Commands to use

Specify environment variables
> cp example.env .env

Initialize virtual environment (it shall also read .env)
> pipenv shell

Install required python modules
> pipenv install

Run both mix watch script and python dev sever, in parallel
> ./run dev

Well, that's all that needed, mostly.

### Other useful commands

Run dev server
> flask run

Build and monitor static files
> npm run watch

Launch REPL for tinkering
> ptpython

Also could be done via flask cli
> flask shell

### Project structure

```
.
├── example.env             << environment variables
├── run.py                  << flask entry point
├── webpack.mix.js          << frontend pipeline entry point
└── mix
    ├── __init__.py         << flask configuration
    ├── client
    │   ├── build           << frontend build artifacts
    │   ├── static
    │   └── templates
    └── server
        ├── config.py       << configuration for different environments
        ├── main            << main blueprint
        ├── models.py
        └── user
```
