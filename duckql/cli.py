import click

from .structures import Query


@click.group()
def cli():
    pass


@cli.command()
def schema():
    print(Query.schema_json(indent=2))


@cli.command()
@click.argument('filename')
def file(filename):
    my_query = Query.parse_file(filename)
    print(my_query)


if __name__ == '__main__':
    cli()
