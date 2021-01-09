import click
from flask.cli import with_appcontext

from .extensions import db
from flask_qa.models import User,Question

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()