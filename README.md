# Simple Flask configuration with Vue/Laravel-Mix frontend pipeline

### What is this

- largely based on some skeletons found on github
- uses Pipenv for virtual environment and local variables (.env file)
- uses laravel-mix with Vue widgets for frontend client
- intended for simple prototyping using separate client/server domains
- includes vue, lodash, axios, moment and bulma as already installed modules

### Commands to use

Initialize virtual environment and install required modules
> pipenv shell
> pipenv install

Run dev server
> flask run

Build and monitor static files
> npm run watch

Launch REPL for tinkering
> ptpython
> flask shell
