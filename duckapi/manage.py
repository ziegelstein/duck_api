import click
from flask.cli import with_appcontext


@click.command("init")
@with_appcontext
def init():
    """Create a new admin user"""
    from duckapi.extensions import db
    from duckapi.models import User

    click.echo("create user")
    user = User(username="demuirg", email="meister@ziegel.me", password="nuttela1", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")
