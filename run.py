#!/usr/bin/env python

from flask.cli import FlaskGroup

from mix.server import create_app, db

import subprocess

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def dev():
    """Run both python and mix, side by side."""
    subprocess.Popen(['flask', 'run'])
    subprocess.run(['npm', 'run', 'watch'])


if __name__ == '__main__':
    cli()
