#!/usr/bin/env python
"""Flask's command-line utility for administrative tasks."""
import os
import sys

from flask.cli import FlaskGroup

from app import create_app

def main():
    """Run administrative tasks."""
    os.environ.setdefault('FLASK_APP', 'app')
    os.environ.setdefault('FLASK_ENV', 'development')
    app = create_app()
    cli = FlaskGroup(app)
    cli()

if __name__ == '__main__':
    main()
