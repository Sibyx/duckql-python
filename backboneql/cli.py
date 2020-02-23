import click

from .structures import Query


@click.group()
def cli():
    pass


@cli.command()
def schema():
    print(Query.schema_json(indent=2))


if __name__ == '__main__':
    cli()
